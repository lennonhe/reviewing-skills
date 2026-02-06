# Common Issues and Fixes

Quick reference for frequently encountered problems when reviewing skills.

## Metadata Issues

### Issue: Name Uses Underscores or CamelCase
**Example**: `skill_name`, `SkillName`
**Fix**: Use lowercase with hyphens: `skill-name`
**Severity**: High

### Issue: Name Not in Gerund Form
**Example**: `skill-reviewer`, `code-formatter`
**Fix**: Use -ing form: `reviewing-skills`, `formatting-code`
**Severity**: Medium

### Issue: Description in First Person
**Example**: "Review skills against best practices"
**Fix**: Use third person: "Reviews skills against best practices"
**Severity**: High

### Issue: Description Missing Triggers
**Example**: "Analyzes code quality and style"
**Fix**: Add triggers: "Analyzes code quality and style. Use '/analyze' to check current file or '/analyze path/to/file' for specific files."
**Severity**: High

### Issue: Description Over 1024 Characters
**Example**: Long paragraph with excessive detail
**Fix**: Move details to SKILL.md body, keep description concise
**Severity**: Critical (Claude may truncate or ignore)

### Issue: Missing argument-hint
**Example**: Skill accepts arguments but no hint provided
**Fix**: Add frontmatter field: `argument-hint: "'file-path'"`
**Severity**: Medium

## Structure Issues

### Issue: README.md at Root
**Example**: `skill-name/README.md`
**Fix**: Remove README.md, use SKILL.md for all documentation
**Severity**: Medium
**Rationale**: Redundant with SKILL.md, Claude only reads SKILL.md

### Issue: CHANGELOG.md Present
**Example**: `skill-name/CHANGELOG.md`
**Fix**: Remove CHANGELOG.md, use git history for versioning
**Severity**: Low
**Rationale**: Skills should be self-contained, versioning handled externally

### Issue: Nested Reference Folders
**Example**: `references/api-docs/endpoints/auth.md`
**Fix**: Flatten to: `references/api-auth-endpoints.md`
**Severity**: Medium
**Rationale**: Claude performs better with shallow hierarchies

### Issue: Development Files Committed
**Example**: `.git/`, `__pycache__/`, `.DS_Store`, `test_fixtures/`
**Fix**: Remove from skill package, add to .gitignore
**Severity**: High
**Rationale**: Bloats skill size, exposes unnecessary internals

### Issue: Scripts Not in scripts/ Folder
**Example**: `skill-name/analyze.py` (at root)
**Fix**: Move to: `skill-name/scripts/analyze.py`
**Severity**: Medium

## Content Issues

### Issue: SKILL.md Over 500 Lines
**Example**: 800-line SKILL.md with embedded documentation
**Fix**: Extract documentation to `references/`, keep SKILL.md under 500 lines
**Severity**: High
**Rationale**: Claude processes shorter files more effectively

### Issue: Excessive Explanatory Text
**Example**:
```
The grep command is a powerful tool that searches for patterns...
To use grep, you need to understand regular expressions...
```
**Fix**: Show example instead:
```
Search for patterns:
grep -r "pattern" path/to/files
```
**Severity**: Medium

### Issue: Redundant Sections
**Example**: Same workflow described in Overview, Instructions, and Examples sections
**Fix**: Consolidate into single clear section
**Severity**: Medium

### Issue: Missing Progressive Disclosure
**Example**: All details in SKILL.md, no references
**Fix**: Move detailed info to `references/`, keep SKILL.md high-level
**Severity**: Medium

### Issue: No Quick Start
**Example**: Must read all references to understand basic usage
**Fix**: Add quick examples in SKILL.md, detailed explanations in references
**Severity**: High

## Code Quality Issues

### Issue: Backslashes in Paths
**Example**: `scripts\analyzer.py` (Windows-style)
**Fix**: Use forward slashes: `scripts/analyzer.py`
**Severity**: High
**Rationale**: Cross-platform compatibility

### Issue: Absolute Paths
**Example**: `/Users/name/project/skill/scripts/run.py`
**Fix**: Use relative paths: `scripts/run.py`
**Severity**: Critical
**Rationale**: Breaks on other machines

### Issue: No Error Handling
**Example**:
```python
def process_file(path):
    with open(path) as f:
        return f.read()
```
**Fix**:
```python
def process_file(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {path}")
        return None
    except PermissionError:
        print(f"Error: Permission denied: {path}")
        return None
```
**Severity**: High

### Issue: No Input Validation
**Example**:
```python
def analyze(skill_path):
    # Assumes skill_path is valid
    return analyze_skill(skill_path)
```
**Fix**:
```python
def analyze(skill_path):
    if not os.path.exists(skill_path):
        raise ValueError(f"Path does not exist: {skill_path}")
    if not os.path.isdir(skill_path):
        raise ValueError(f"Path is not a directory: {skill_path}")
    if not os.path.exists(os.path.join(skill_path, "SKILL.md")):
        raise ValueError(f"No SKILL.md found in: {skill_path}")
    return analyze_skill(skill_path)
```
**Severity**: High

### Issue: Magic Constants
**Example**:
```python
if len(body) > 500:
    print("Too long")
```
**Fix**:
```python
MAX_BODY_LINES = 500
if len(body) > MAX_BODY_LINES:
    print(f"Body exceeds {MAX_BODY_LINES} lines")
```
**Severity**: Medium

### Issue: Undocumented Dependencies
**Example**: Script imports `yaml`, `requests` without mentioning in SKILL.md
**Fix**: Add to SKILL.md:
```markdown
## Dependencies
- Python 3.7+
- `pip install pyyaml requests`
```
**Severity**: High

### Issue: Platform-Specific Commands
**Example**: Shell script uses `sed -i` (doesn't work on macOS)
**Fix**: Use `sed -i.bak` or Python script for cross-platform compatibility
**Severity**: High

## Anti-Patterns

### Anti-Pattern: "God Skill"
**Description**: Single skill tries to do too many unrelated things
**Example**: Skill that reviews code, formats files, runs tests, and generates documentation
**Fix**: Split into focused skills: `reviewing-code`, `formatting-code`, `running-tests`, `generating-docs`
**Severity**: High

### Anti-Pattern: Tutorial in SKILL.md
**Description**: SKILL.md teaches concepts instead of providing actionable instructions
**Example**: "What is a REST API? REST stands for..."
**Fix**: Assume prerequisite knowledge or move tutorial to `references/background.md`
**Severity**: Medium

### Anti-Pattern: Copy-Paste Instructions
**Description**: Instructions tell Claude to copy-paste code
**Example**: "Copy this code into your file: [code block]"
**Fix**: Provide clear requirements and let Claude implement
**Severity**: Low

### Anti-Pattern: Hardcoded User Preferences
**Description**: Skill assumes specific tools, styles, or workflows
**Example**: "Always use tabs for indentation"
**Fix**: Detect project style or make configurable
**Severity**: Medium

### Anti-Pattern: Brittle Parsing
**Description**: Code assumes exact formatting without validation
**Example**: Splitting on "Line 5:" without checking if it exists
**Fix**: Use robust parsing with error handling
**Severity**: High

## Quick Fixes Checklist

Before finalizing a skill, verify:

- [ ] Name is lowercase-with-hyphens and uses gerund form
- [ ] Description is third-person, under 1024 chars, includes triggers
- [ ] No README.md or CHANGELOG.md files
- [ ] References are one level deep (not nested)
- [ ] SKILL.md body is under 500 lines
- [ ] All paths use forward slashes
- [ ] No absolute paths
- [ ] Dependencies documented with installation instructions
- [ ] Scripts have error handling and input validation
- [ ] No magic constants
- [ ] Examples prioritized over explanations
- [ ] Progressive disclosure: SKILL.md high-level, references detailed

## Reference

For complete criteria, see:
- `best-practices-checklist.md` - Full scoring rubric
- `review-report-template.md` - Output format guide
