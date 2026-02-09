# Reviewing Skills - Claude Code Plugin

A Claude Code plugin for reviewing skills against Anthropic's official best practices.

## Overview

The **Reviewing Skills** plugin helps ensure your Claude Code skills follow best practices for structure, content, metadata, and code quality. Point it at a plugin directory and it reviews all skills listed in `plugin.json`, generating detailed compliance reports with actionable recommendations.

## Installation

### Via Marketplace (Recommended)

```bash
# Add Lennon's plugin marketplace
claude plugin marketplace add LennonHe/lennon-claude-code-plugins

# Install this plugin
claude plugin install reviewing-skills@lennon-claude-code-plugins
```

### Direct Installation

```bash
# Install directly from GitHub
claude plugin install https://github.com/LennonHe/reviewing-skills.git
```

## Usage

### Review All Skills in a Plugin

```
/review-skill './path/to/my-plugin'
```

The plugin path must contain a `.claude-plugin/plugin.json` file that lists the skills to review.

**Example plugin.json structure:**

```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "description": "My Claude Code plugin",
  "skills": [
    "skills/my-first-skill",
    "skills/my-second-skill"
  ]
}
```

### No Argument

```
/review-skill
```

Shows an error with usage instructions. A plugin path is required.

## What Gets Reviewed

The plugin discovers all skills from `plugin.json` and evaluates each one across four categories (25 points each):

### 1. Metadata (25 points)
- **Name Format**: Lowercase with hyphens, gerund form (e.g., `reviewing-skills`)
- **Description Quality**: Third-person, under 1024 chars, includes triggers
- **Frontmatter Fields**: Required fields present and valid YAML

### 2. Structure (25 points)
- **Required Files**: SKILL.md at root, proper folder organization
- **Reference Organization**: References one level deep, appropriate content
- **Extraneous Files**: No README, CHANGELOG, or development files

### 3. Content (25 points)
- **Body Length**: SKILL.md under 500 lines (300 ideal)
- **Conciseness**: Examples over explanations, no redundancy
- **Progressive Disclosure**: Core info in SKILL.md, details in references

### 4. Code Quality (25 points)
- **Error Handling**: Explicit error messages, input validation
- **Path Conventions**: Forward slashes, relative paths, cross-platform
- **Dependencies**: Documented with installation instructions

## Review Output

The plugin generates a comprehensive report including:

1. **Plugin Summary**: Overview table of all skills with scores and status
2. **Per-Skill Reports**: Detailed findings for each skill in the plugin
3. **Prioritized Recommendations**: Critical, High, Medium, Low priority per skill
4. **Cross-Skill Observations**: Common patterns or issues across skills

### Scoring Guide

- **90-100 points (Excellent)**: Ready for production use
- **75-89 points (Good)**: Minor improvements recommended
- **60-74 points (Fair)**: Several issues to address
- **Below 60 points (Needs Work)**: Significant improvements required

## Example Review Workflow

1. **Organize your plugin** with `.claude-plugin/plugin.json` listing your skills
2. **Run the review**: `/review-skill './my-plugin'`
3. **Review the report**: Check per-skill scores and recommendations
4. **Make improvements**: Address critical and high priority issues
5. **Re-run review**: Verify improvements across all skills
6. **Package and publish**: Once satisfied with scores

## Dependencies

- **Python 3.7+** (for automated metrics collection)
- No additional Python packages required (uses only standard library)

## Tips

- **Review before packaging**: Check skills while in development, not after installation
- **Focus on high-impact issues**: Prioritize critical and high severity recommendations
- **Consider context**: Some best practices may not apply to all skill types
- **Iterate**: Run multiple reviews as you make improvements
- **Use as a checklist**: Reference the best practices checklist during development

## Common Issues and Fixes

### Issue: Name uses underscores
- `skill_name`
- `skill-name`

### Issue: Description in first person
- "Review skills against best practices"
- "Reviews skills against best practices"

### Issue: SKILL.md over 500 lines
Move detailed content to `references/` folder

### Issue: Backslashes in paths
- `scripts\analyzer.py`
- `scripts/analyzer.py`

## Troubleshooting

### "Error: No plugin path provided"
- You must provide a path to a plugin directory: `/review-skill './my-plugin'`

### "Error: plugin.json not found"
- Ensure the path points to a plugin root directory
- The directory must contain `.claude-plugin/plugin.json`

### "Error: Invalid plugin.json"
- Verify `plugin.json` has required fields: `name`, `version`, `skills`
- The `skills` field must be a non-empty array of skill paths

### "Error: Path does not exist"
- Verify the plugin path you provided exists
- Use forward slashes even on Windows: `./my-plugin` not `.\my-plugin`

### "Error: SKILL.md not found"
- Check that each skill path in `plugin.json` points to a valid skill directory
- Each skill directory must contain a SKILL.md file at its root

### "Warning: Could not read file"
- Check file permissions
- Ensure files are readable and not corrupted

### Script execution errors
- Verify Python 3.7+ is installed: `python --version`
- Check that the script path is correct

## License

MIT License - See LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## Support

This plugin was created following Anthropic's plugin creation best practices. If you encounter any issues or have suggestions for improvement, please [open an issue](https://github.com/LennonHe/reviewing-skills/issues).

## Related Resources

- [Anthropic's Skill Creator Guide](https://docs.anthropic.com/claude/docs/skills)
- [Claude Code Documentation](https://docs.anthropic.com/claude/docs/claude-code)
