# Reviewing Skills - Claude Code Plugin

A Claude Code plugin for reviewing skills against Anthropic's official best practices.

## Overview

The **Reviewing Skills** plugin helps ensure your Claude Code skills follow best practices for structure, content, metadata, and code quality. It generates detailed compliance reports with actionable recommendations.

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

### Review a Skill

```
/review-skill
/review-skill './path/to/your-skill'
```

## What Gets Reviewed

The plugin evaluates four categories (25 points each):

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

1. **Executive Summary**: Overall score and status
2. **Summary Table**: Scores by category with issue counts
3. **Prioritized Recommendations**: Critical, High, Medium, Low priority
4. **Detailed Findings**: Line-by-line analysis with file references

### Scoring Guide

- **90-100 points (✅ Excellent)**: Ready for production use
- **75-89 points (⚠️ Good)**: Minor improvements recommended
- **60-74 points (⚠️ Fair)**: Several issues to address
- **Below 60 points (❌ Needs Work)**: Significant improvements required

## Example Review Workflow

1. **Create your skill** in a source folder (e.g., `my-skill/`)
2. **Run the review**: `/review-skill './my-skill'`
3. **Review the report**: Check scores and recommendations
4. **Make improvements**: Address critical and high priority issues
5. **Re-run review**: Verify improvements
6. **Package and install**: Once satisfied with the score

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
❌ `skill_name`
✅ `skill-name`

### Issue: Description in first person
❌ "Review skills against best practices"
✅ "Reviews skills against best practices"

### Issue: SKILL.md over 500 lines
💡 Move detailed content to `references/` folder

### Issue: Backslashes in paths
❌ `scripts\analyzer.py`
✅ `scripts/analyzer.py`

## Troubleshooting

### "Error: Path does not exist"
- Verify the path you provided exists
- Use forward slashes even on Windows: `./my-skill` not `.\my-skill`

### "Error: SKILL.md not found"
- Ensure you're pointing to the skill source folder
- The folder must contain a SKILL.md file at its root

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
