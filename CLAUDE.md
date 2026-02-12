# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Claude Code plugin for reviewing skills against Anthropic's official best practices. It analyzes skill structure, metadata, content quality, and code conventions for Claude Code plugins.

**Key Components:**
- `/review-skill` - Main skill that reviews all skills in a Claude Code plugin
- `skill-analyzer.py` - Python script that provides automated metrics collection
- Reference files - Best practices checklist, common issues, and report templates

## Development Commands

### Testing the Skill Analyzer

```bash
# Analyze a plugin (requires .claude-plugin/plugin.json)
python skills/reviewing-skills/scripts/skill-analyzer.py ./path/to/plugin

# Analyze a single skill (fallback mode)
python skills/reviewing-skills/scripts/skill-analyzer.py ./path/to/skill
```

The script outputs JSON with per-skill metrics including line counts, frontmatter validation, file structure analysis, and name/description checks.

### Testing the Skill Locally

Test the `/review-skill` command by pointing it at a local plugin directory:
```
/review-skill './path/to/my-plugin'
```

The plugin must contain `.claude-plugin/plugin.json` with a `skills` array listing skill paths.

## Architecture

### Skill Review Workflow

1. **Parse Arguments** - Validate plugin path and discover skills from `plugin.json`
2. **Collect Metrics** - Run `skill-analyzer.py` for automated analysis
3. **Manual Review** - Evaluate against `best-practices-checklist.md` (4 categories × 25 points)
4. **Identify Issues** - Cross-reference with `common-issues.md` for patterns
5. **Generate Report** - Use `review-report-template.md` structure, save as `plugin-review-report.md`

### Review Categories (100 points total)

- **Metadata (25 pts)** - Name format, description quality, frontmatter fields
- **Structure (25 pts)** - File organization, reference depth, extraneous files
- **Content (25 pts)** - Body length, conciseness, progressive disclosure
- **Code Quality (25 pts)** - Error handling, path conventions, dependencies

### Key Files

- `skills/reviewing-skills/SKILL.md` - Main skill definition with frontmatter and instructions
- `skills/reviewing-skills/scripts/skill-analyzer.py` - Python script (Python 3.7+, stdlib only)
- `skills/reviewing-skills/references/best-practices-checklist.md` - Complete 100-point rubric
- `skills/reviewing-skills/references/common-issues.md` - Anti-patterns and quick fixes
- `skills/reviewing-skills/references/review-report-template.md` - Output format guide

## Path Conventions

- Always use forward slashes in paths (cross-platform compatibility)
- Use relative paths from skill root, never absolute paths
- The analyzer script normalizes all paths to forward slashes in output

## Dependencies

- **Python 3.7+** required for `skill-analyzer.py`
- No external Python packages needed (uses standard library only)
- Skills are designed to work with Claude Code's built-in tools: Read, Glob, Bash

## Scoring Guide

- **90-100 (Excellent ✅)** - Ready for production
- **75-89 (Good ⚠️)** - Minor improvements recommended
- **60-74 (Fair ⚠️)** - Several issues to address
- **Below 60 (Needs Work ❌)** - Significant improvements required
