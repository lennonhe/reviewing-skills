---
name: reviewing-skills
description: Reviews Claude Code skills against Anthropic's best practices. Analyzes skill structure, metadata, content quality, and code conventions. Generates a structured compliance report with prioritized recommendations. Triggers - '/review-skill' (reviews ./learning-esl-vocabulary by default) or '/review-skill path/to/skill' (reviews specific skill path).
argument-hint: "'path/to/skill'" (optional)
allowed-tools:
  - Read
  - Glob
  - Bash
---

# Reviewing Skills

This skill reviews Claude Code skills against Anthropic's official best practices to ensure they follow guidelines for conciseness, structure, progressive disclosure, and code quality.

## Trigger Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/review-skill` | Review the learning-esl-vocabulary skill (default path: ./learning-esl-vocabulary) | `/review-skill` |
| `/review-skill 'path'` | Review a specific skill at the given path | `/review-skill './my-custom-skill'` |

## Review Workflow

Follow these steps to conduct a comprehensive skill review:

### 1. Parse Arguments and Set Target Path

- If no argument provided: use default path `./learning-esl-vocabulary`
- If argument provided: use the specified path
- Verify the path exists and contains a SKILL.md file
- Normalize path to forward slashes for consistency

### 2. Collect Skill Metrics

Run the skill analyzer script to gather automated metrics:

```bash
python reviewing-skills/scripts/skill-analyzer.py <target-path>
```

This provides:
- SKILL.md line counts (total and body)
- Frontmatter validation results
- File structure analysis
- Name/description constraint checks

### 3. Manual Review Against Checklist

Read `references/best-practices-checklist.md` and evaluate the skill across four categories:

- **Metadata (25 points)**: Name format, description quality, frontmatter fields
- **Structure (25 points)**: File organization, reference depth, extraneous files
- **Content (25 points)**: Body length, conciseness, progressive disclosure
- **Code Quality (25 points)**: Error handling, path conventions, dependencies

For each criterion:
- ✅ **Pass**: Fully compliant
- ⚠️ **Partial**: Mostly compliant with minor issues
- ❌ **Fail**: Non-compliant or missing

### 4. Identify Issues and Recommendations

Cross-reference findings with `references/common-issues.md` to:
- Identify common anti-patterns
- Generate specific, actionable recommendations
- Prioritize by severity: Critical, High, Medium, Low

### 5. Generate Review Report

Use `references/review-report-template.md` to create a structured report containing:

1. **Executive Summary**: Overall compliance score and status
2. **Category Breakdown**: Detailed findings per category with pass/fail status
3. **Prioritized Recommendations**: Actionable improvements ranked by severity
4. **Detailed Findings**: Line-by-line issues with file references

Save the report to the skill's directory as `skill-review-report.md`.

## Output Format

The review report should follow this structure:

```markdown
# Skill Review Report: [Skill Name]

**Review Date**: YYYY-MM-DD
**Skill Path**: path/to/skill
**Overall Score**: XX/100

## Summary

| Category | Status | Score | Issues |
|----------|--------|-------|--------|
| Metadata | ✅/⚠️/❌ | XX/25 | N |
| Structure | ✅/⚠️/❌ | XX/25 | N |
| Content | ✅/⚠️/❌ | XX/25 | N |
| Code Quality | ✅/⚠️/❌ | XX/25 | N |

## Recommendations

### Critical Priority
- [Specific actionable recommendation]

### High Priority
- [Specific actionable recommendation]

### Medium Priority
- [Specific actionable recommendation]

### Low Priority
- [Specific actionable recommendation]

## Detailed Findings

### Metadata
[Detailed analysis...]

### Structure
[Detailed analysis...]

### Content
[Detailed analysis...]

### Code Quality
[Detailed analysis...]
```

## Reference Files

- **Best Practices Checklist**: `references/best-practices-checklist.md` - Complete review criteria
- **Review Report Template**: `references/review-report-template.md` - Output format guide
- **Common Issues**: `references/common-issues.md` - Frequently encountered problems and fixes

## Notes

- Default target is `./learning-esl-vocabulary` (source folder, not `.claude/skills/`)
- Reviews source files before packaging, not installed versions
- Automated metrics complement manual review but don't replace it
- Focus on actionable recommendations, not just compliance checking
- Consider skill's specific use case when applying best practices
