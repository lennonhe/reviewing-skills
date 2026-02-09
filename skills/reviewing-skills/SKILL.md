---
name: reviewing-skills
description: Reviews all skills in a Claude Code plugin against Anthropic's best practices. Analyzes skill structure, metadata, content quality, and code conventions for each skill listed in plugin.json. Generates a structured compliance report with prioritized recommendations. Triggers - '/review-skill path/to/plugin' (reviews all skills in the given plugin).
argument-hint: "'path/to/plugin'" (required)
allowed-tools:
  - Read
  - Glob
  - Bash
---

# Reviewing Skills

This skill reviews all skills within a Claude Code plugin against Anthropic's official best practices to ensure they follow guidelines for conciseness, structure, progressive disclosure, and code quality.

## Trigger Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/review-skill 'path'` | Review all skills in a plugin at the given path | `/review-skill './my-plugin'` |

## Review Workflow

Follow these steps to conduct a comprehensive plugin review:

### 1. Parse Arguments and Discover Skills

- If no argument provided: display an error message:
  > Error: No plugin path provided. Usage: `/review-skill 'path/to/plugin'`
  Then stop execution.
- If argument provided:
  1. Verify the path exists
  2. Look for `.claude-plugin/plugin.json` at the given path
  3. Read `plugin.json` and parse the `"skills"` array to discover skill paths
  4. Resolve each skill path relative to the plugin root
  5. Verify each skill path exists and contains a SKILL.md file

### 2. Collect Skill Metrics

Run the skill analyzer script against the plugin to gather automated metrics for all skills:

```bash
python reviewing-skills/scripts/skill-analyzer.py <plugin-path>
```

This provides per-skill:
- SKILL.md line counts (total and body)
- Frontmatter validation results
- File structure analysis
- Name/description constraint checks

Plus plugin-level metadata (name, version, skills count).

### 3. Manual Review Against Checklist

For each skill discovered in the plugin, read `references/best-practices-checklist.md` and evaluate across four categories:

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
- Identify common anti-patterns across all skills in the plugin
- Generate specific, actionable recommendations per skill
- Prioritize by severity: Critical, High, Medium, Low

### 5. Generate Review Report

Use `references/review-report-template.md` to create a structured report containing:

1. **Plugin Summary**: Plugin name, version, number of skills, and overall compliance
2. **Per-Skill Reports**: For each skill in the plugin:
   - Executive summary with overall compliance score and status
   - Category breakdown with detailed findings and pass/fail status
   - Prioritized recommendations ranked by severity
   - Detailed findings with line-by-line issues and file references
3. **Cross-Skill Observations**: Common patterns or issues found across multiple skills

Save the report to the plugin's directory as `plugin-review-report.md`.

## Output Format

The review report should follow this structure:

```markdown
# Plugin Review Report: [Plugin Name]

**Review Date**: YYYY-MM-DD
**Plugin Path**: path/to/plugin
**Plugin Version**: X.Y.Z
**Skills Reviewed**: N

## Plugin Summary

| Skill | Overall Score | Status | Critical | High | Medium | Low |
|-------|---------------|--------|----------|------|--------|-----|
| skill-name-1 | XX/100 | ✅/⚠️/❌ | N | N | N | N |
| skill-name-2 | XX/100 | ✅/⚠️/❌ | N | N | N | N |

---

## Skill: [skill-name-1]

**Skill Path**: path/to/skill
**Overall Score**: XX/100

### Summary

| Category | Status | Score | Issues |
|----------|--------|-------|--------|
| Metadata | ✅/⚠️/❌ | XX/25 | N |
| Structure | ✅/⚠️/❌ | XX/25 | N |
| Content | ✅/⚠️/❌ | XX/25 | N |
| Code Quality | ✅/⚠️/❌ | XX/25 | N |

### Recommendations

#### Critical Priority
- [Specific actionable recommendation]

#### High Priority
- [Specific actionable recommendation]

#### Medium Priority
- [Specific actionable recommendation]

#### Low Priority
- [Specific actionable recommendation]

### Detailed Findings

#### Metadata
[Detailed analysis...]

#### Structure
[Detailed analysis...]

#### Content
[Detailed analysis...]

#### Code Quality
[Detailed analysis...]

---

## Skill: [skill-name-2]

[Same structure as above, repeated for each skill]

---

## Cross-Skill Observations

- [Common patterns or recurring issues across skills]
- [Plugin-level structural observations]
```

## Reference Files

- **Best Practices Checklist**: `references/best-practices-checklist.md` - Complete review criteria
- **Review Report Template**: `references/review-report-template.md` - Output format guide
- **Common Issues**: `references/common-issues.md` - Frequently encountered problems and fixes

## Notes

- The plugin path must contain `.claude-plugin/plugin.json` listing the skills to review
- Each skill path in `plugin.json` is resolved relative to the plugin root
- Reviews source files before packaging, not installed versions
- Automated metrics complement manual review but don't replace it
- Focus on actionable recommendations, not just compliance checking
- Consider each skill's specific use case when applying best practices
