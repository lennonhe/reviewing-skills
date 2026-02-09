#!/usr/bin/env python3
"""
Skill Analyzer - Automated metrics collection for skill reviews.

Usage:
    python skill-analyzer.py <path-to-plugin>
    python skill-analyzer.py <path-to-skill>   (fallback for single skill)

Output:
    JSON object with skill/plugin metrics
"""

import sys
import os
import json
import re
from pathlib import Path
from typing import Dict, List, Any, Optional

# Constants
MAX_BODY_LINES = 500
IDEAL_BODY_LINES = 300
MAX_DESCRIPTION_LENGTH = 1024
EXTRANEOUS_FILES = [
    'README.md', 'README.txt', 'CHANGELOG.md', 'CHANGELOG.txt',
    '.git', '.DS_Store', '__pycache__', '.pytest_cache',
    'node_modules', '.vscode', '.idea'
]


def parse_frontmatter(content: str) -> tuple[Optional[Dict], str]:
    """
    Parse YAML frontmatter from SKILL.md.

    Returns:
        Tuple of (frontmatter_dict, body_content)
    """
    if not content.startswith('---'):
        return None, content

    parts = content.split('---', 2)
    if len(parts) < 3:
        return None, content

    frontmatter_text = parts[1].strip()
    body = parts[2].strip()

    # Simple YAML parser (handles basic key: value pairs)
    frontmatter = {}
    current_key = None
    current_list = []

    for line in frontmatter_text.split('\n'):
        line = line.rstrip()

        # List item
        if line.strip().startswith('- '):
            if current_key and isinstance(frontmatter.get(current_key), list):
                frontmatter[current_key].append(line.strip()[2:])
            elif current_key:
                current_list.append(line.strip()[2:])
        # Key: value
        elif ':' in line and not line.startswith(' '):
            if current_key and current_list:
                frontmatter[current_key] = current_list
                current_list = []

            key, value = line.split(':', 1)
            current_key = key.strip()
            value = value.strip()

            if value:
                frontmatter[current_key] = value
            else:
                frontmatter[current_key] = []

    # Handle last list
    if current_key and current_list:
        frontmatter[current_key] = current_list

    return frontmatter, body


def count_lines(file_path: Path) -> int:
    """Count lines in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return len(f.readlines())
    except Exception as e:
        print(f"Warning: Could not read {file_path}: {e}", file=sys.stderr)
        return 0


def validate_name(name: str) -> Dict[str, Any]:
    """Validate skill name format."""
    issues = []

    # Check lowercase and hyphens only
    if not re.match(r'^[a-z]+(-[a-z]+)*$', name):
        issues.append("Name should use lowercase letters and hyphens only")

    # Check for gerund form (-ing)
    if not name.endswith('ing') and not any(part.endswith('ing') for part in name.split('-')):
        issues.append("Name should use gerund form (ending in -ing)")

    # Check length (2-4 words ideal)
    word_count = len(name.split('-'))
    if word_count > 5:
        issues.append(f"Name has {word_count} words, consider reducing to 2-4 words")

    return {
        'valid': len(issues) == 0,
        'issues': issues
    }


def validate_description(description: str) -> Dict[str, Any]:
    """Validate skill description."""
    issues = []
    length = len(description)

    # Check length
    if length > MAX_DESCRIPTION_LENGTH:
        issues.append(f"Description is {length} characters (max: {MAX_DESCRIPTION_LENGTH})")

    # Check third-person perspective (simple heuristic)
    first_word = description.split()[0].lower() if description else ""
    if first_word in ['use', 'run', 'execute', 'create', 'generate', 'analyze']:
        issues.append("Description should use third-person perspective (e.g., 'Uses', 'Runs', 'Analyzes')")

    # Check for trigger mention
    trigger_keywords = ['/review', 'trigger', 'command', 'invoke']
    has_triggers = any(keyword in description.lower() for keyword in trigger_keywords)
    if not has_triggers:
        issues.append("Description should mention trigger commands or usage patterns")

    return {
        'valid': len(issues) == 0,
        'length': length,
        'issues': issues
    }


def scan_files(skill_path: Path) -> Dict[str, Any]:
    """Scan skill directory for file structure."""
    files = []
    extraneous = []
    references_nested = []

    for item in skill_path.rglob('*'):
        if item.is_file():
            rel_path = item.relative_to(skill_path)
            rel_path_str = str(rel_path).replace('\\', '/')

            # Check for extraneous files
            if any(ex in str(rel_path) for ex in EXTRANEOUS_FILES):
                extraneous.append(rel_path_str)
                continue

            # Check for nested references
            if rel_path_str.startswith('references/') and '/' in rel_path_str[11:]:
                references_nested.append(rel_path_str)

            line_count = count_lines(item)
            files.append({
                'path': rel_path_str,
                'lines': line_count
            })

    return {
        'files': files,
        'extraneous': extraneous,
        'references_nested': references_nested
    }


def analyze_skill(skill_path: str) -> Dict[str, Any]:
    """
    Analyze a skill and return metrics.

    Args:
        skill_path: Path to skill directory

    Returns:
        Dictionary with analysis results
    """
    skill_path = Path(skill_path)

    if not skill_path.exists():
        return {
            'error': f"Path does not exist: {skill_path}"
        }

    if not skill_path.is_dir():
        return {
            'error': f"Path is not a directory: {skill_path}"
        }

    skill_md = skill_path / 'SKILL.md'
    if not skill_md.exists():
        return {
            'error': f"SKILL.md not found in: {skill_path}"
        }

    # Read SKILL.md
    try:
        with open(skill_md, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {
            'error': f"Could not read SKILL.md: {e}"
        }

    # Parse frontmatter
    frontmatter, body = parse_frontmatter(content)

    # Count lines
    total_lines = len(content.split('\n'))
    body_lines = len(body.split('\n'))

    # Validate frontmatter
    frontmatter_valid = frontmatter is not None
    required_fields = ['name', 'description', 'allowed-tools']
    missing_fields = [f for f in required_fields if not frontmatter or f not in frontmatter]

    # Validate name and description
    name_validation = {}
    description_validation = {}

    if frontmatter:
        if 'name' in frontmatter:
            name_validation = validate_name(frontmatter['name'])
        if 'description' in frontmatter:
            description_validation = validate_description(frontmatter['description'])

    # Scan files
    file_scan = scan_files(skill_path)

    # Build result
    result = {
        'skill_path': str(skill_path),
        'skill_md': {
            'total_lines': total_lines,
            'body_lines': body_lines,
            'body_under_500': body_lines < MAX_BODY_LINES,
            'body_under_300': body_lines < IDEAL_BODY_LINES
        },
        'frontmatter': {
            'valid': frontmatter_valid,
            'missing_fields': missing_fields,
            'name': frontmatter.get('name') if frontmatter else None,
            'description': frontmatter.get('description') if frontmatter else None,
            'allowed_tools': frontmatter.get('allowed-tools') if frontmatter else None,
            'argument_hint': frontmatter.get('argument-hint') if frontmatter else None
        },
        'name_validation': name_validation,
        'description_validation': description_validation,
        'files': file_scan['files'],
        'structure': {
            'extraneous_files': file_scan['extraneous'],
            'references_nested': file_scan['references_nested'],
            'has_scripts_folder': any(f['path'].startswith('scripts/') for f in file_scan['files']),
            'has_references_folder': any(f['path'].startswith('references/') for f in file_scan['files'])
        }
    }

    return result


def validate_plugin_json(plugin_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validate plugin.json metadata.

    Args:
        plugin_data: Parsed plugin.json contents

    Returns:
        Dictionary with validation results
    """
    issues = []

    if 'name' not in plugin_data:
        issues.append("Missing required field: 'name'")

    if 'version' not in plugin_data:
        issues.append("Missing required field: 'version'")

    if 'skills' not in plugin_data:
        issues.append("Missing required field: 'skills'")
    elif not isinstance(plugin_data['skills'], list):
        issues.append("'skills' must be an array")
    elif len(plugin_data['skills']) == 0:
        issues.append("'skills' array is empty")

    return {
        'valid': len(issues) == 0,
        'issues': issues
    }


def analyze_plugin(plugin_path: str) -> Dict[str, Any]:
    """
    Analyze all skills in a Claude Code plugin.

    Reads .claude-plugin/plugin.json, discovers skill paths,
    and runs analyze_skill() for each one.

    Args:
        plugin_path: Path to plugin root directory

    Returns:
        Dictionary with plugin metadata and per-skill results
    """
    plugin_path = Path(plugin_path)
    plugin_json_path = plugin_path / '.claude-plugin' / 'plugin.json'

    if not plugin_json_path.exists():
        return {
            'error': f"plugin.json not found at: {plugin_json_path}"
        }

    # Read and parse plugin.json
    try:
        with open(plugin_json_path, 'r', encoding='utf-8') as f:
            plugin_data = json.load(f)
    except json.JSONDecodeError as e:
        return {
            'error': f"Invalid JSON in plugin.json: {e}"
        }
    except Exception as e:
        return {
            'error': f"Could not read plugin.json: {e}"
        }

    # Validate plugin.json
    validation = validate_plugin_json(plugin_data)
    if not validation['valid']:
        return {
            'error': f"Invalid plugin.json: {'; '.join(validation['issues'])}",
            'validation': validation
        }

    # Extract plugin metadata
    plugin_metadata = {
        'name': plugin_data.get('name'),
        'version': plugin_data.get('version'),
        'description': plugin_data.get('description'),
        'skills_count': len(plugin_data.get('skills', []))
    }

    # Analyze each skill
    skill_results = []
    for skill_entry in plugin_data['skills']:
        # skill_entry can be a string path or an object with a "path" key
        if isinstance(skill_entry, str):
            skill_rel_path = skill_entry
        elif isinstance(skill_entry, dict) and 'path' in skill_entry:
            skill_rel_path = skill_entry['path']
        else:
            skill_results.append({
                'error': f"Invalid skill entry in plugin.json: {skill_entry}"
            })
            continue

        skill_abs_path = plugin_path / skill_rel_path
        result = analyze_skill(str(skill_abs_path))
        result['plugin_relative_path'] = skill_rel_path
        skill_results.append(result)

    return {
        'plugin_path': str(plugin_path),
        'plugin': plugin_metadata,
        'plugin_json_validation': validation,
        'skills': skill_results
    }


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python skill-analyzer.py <path-to-plugin>", file=sys.stderr)
        print("\nAnalyzes all skills in a Claude Code plugin and outputs metrics in JSON format.", file=sys.stderr)
        print("The path should point to a plugin root containing .claude-plugin/plugin.json.", file=sys.stderr)
        print("\nFalls back to single-skill analysis if no plugin.json is found.", file=sys.stderr)
        sys.exit(1)

    target_path = sys.argv[1]
    plugin_json_path = Path(target_path) / '.claude-plugin' / 'plugin.json'

    if plugin_json_path.exists():
        result = analyze_plugin(target_path)
    else:
        # Fallback: analyze as a single skill directory
        result = analyze_skill(target_path)

    # Output JSON
    print(json.dumps(result, indent=2))

    # Exit with error code if analysis failed
    if 'error' in result:
        sys.exit(1)


if __name__ == '__main__':
    main()
