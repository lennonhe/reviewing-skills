# Best Practices Checklist

This checklist covers Anthropic's official best practices for Claude Code skills. Each category is worth 25 points for a total of 100 points.

## Metadata (25 points)

### Name Format (8 points)
- [ ] **Lowercase with hyphens** (3 pts): Name uses only lowercase letters and hyphens (e.g., `my-skill-name`)
- [ ] **Gerund form** (3 pts): Name describes an action using -ing form (e.g., `reviewing-skills`, not `skill-reviewer`)
- [ ] **Concise and descriptive** (2 pts): Name clearly indicates purpose without being overly long (2-4 words ideal)

### Description Quality (10 points)
- [ ] **Third-person perspective** (2 pts): Uses third person (e.g., "Reviews skills..." not "Review skills...")
- [ ] **Under 1024 characters** (2 pts): Description stays within character limit
- [ ] **Includes triggers** (3 pts): Explicitly mentions slash commands or trigger patterns
- [ ] **Describes use cases** (3 pts): Explains when and why to use the skill

### Frontmatter Fields (7 points)
- [ ] **Required fields present** (3 pts): `name`, `description`, and `allowed-tools` are defined
- [ ] **Argument hint provided** (2 pts): `argument-hint` field exists if skill accepts arguments
- [ ] **Valid YAML syntax** (2 pts): Frontmatter parses correctly without errors

## Structure (25 points)

### Required Files (8 points)
- [ ] **SKILL.md exists** (5 pts): Primary instruction file is present at root
- [ ] **Proper folder usage** (3 pts): Uses `scripts/` and/or `references/` folders appropriately

### Reference Organization (9 points)
- [ ] **References one level deep** (5 pts): Reference files in `references/` folder, not nested deeper
- [ ] **Appropriate reference content** (4 pts): References contain reusable content, not one-off examples

### Extraneous Files (8 points)
- [ ] **No README files** (3 pts): No README.md or similar documentation files (use SKILL.md instead)
- [ ] **No CHANGELOG files** (2 pts): No version history tracking files
- [ ] **No test/development files** (3 pts): No .git, .DS_Store, __pycache__, test fixtures, etc.

## Content (25 points)

### Body Length (8 points)
- [ ] **Under 500 lines** (5 pts): SKILL.md body (excluding frontmatter) is under 500 lines
- [ ] **Under 300 lines ideal** (3 pts): SKILL.md body is under 300 lines (bonus for exceptional conciseness)

### Conciseness (9 points)
- [ ] **Examples over explanations** (4 pts): Shows concrete examples rather than abstract descriptions
- [ ] **No redundant content** (3 pts): Avoids repeating information or overlapping sections
- [ ] **Direct and actionable** (2 pts): Instructions are clear and immediately actionable

### Progressive Disclosure (8 points)
- [ ] **Layered information** (4 pts): Core instructions in SKILL.md, details in references/
- [ ] **Quick start accessible** (2 pts): Common use cases understandable without reading all references
- [ ] **Deep dives available** (2 pts): References provide comprehensive details when needed

## Code Quality (25 points)

### Error Handling (8 points)
- [ ] **Explicit error messages** (3 pts): Scripts provide clear error messages for common failures
- [ ] **Input validation** (3 pts): Scripts validate inputs before processing
- [ ] **Graceful degradation** (2 pts): Handles missing dependencies or edge cases gracefully

### Path Conventions (7 points)
- [ ] **Forward slashes** (3 pts): All paths use forward slashes (e.g., `scripts/analyzer.py`)
- [ ] **Relative paths** (2 pts): Uses relative paths from skill root, not absolute paths
- [ ] **Cross-platform compatible** (2 pts): Paths work on Windows, macOS, and Linux

### Dependencies (6 points)
- [ ] **Dependencies documented** (3 pts): All required packages/tools listed in SKILL.md or references
- [ ] **Installation instructions** (2 pts): Provides clear instructions for installing dependencies
- [ ] **Optional vs required** (1 pt): Clearly distinguishes between required and optional dependencies

### Code Standards (4 points)
- [ ] **No magic constants** (2 pts): Uses named constants or configuration for values
- [ ] **Consistent style** (2 pts): Code follows consistent formatting and naming conventions

## Scoring Guide

### Overall Status
- **90-100 points (✅ Excellent)**: Exemplary skill, ready for production use
- **75-89 points (⚠️ Good)**: Mostly compliant, minor improvements recommended
- **60-74 points (⚠️ Fair)**: Several issues to address before production use
- **Below 60 points (❌ Needs Work)**: Significant improvements required

### Category Status
- **20-25 points (✅ Pass)**: Category requirements met
- **15-19 points (⚠️ Partial)**: Some issues present but acceptable
- **Below 15 points (❌ Fail)**: Major issues in this category

## Weighting Rationale

- **Metadata**: Critical for discoverability and understanding
- **Structure**: Affects maintainability and Claude's ability to parse
- **Content**: Impacts usability and Claude's execution effectiveness
- **Code Quality**: Ensures reliability and cross-platform compatibility

## Notes

- Not all criteria apply equally to every skill type
- Consider skill's specific use case when applying checklist
- Edge cases may warrant exceptions with justification
- Best practices evolve - verify against latest Anthropic documentation
