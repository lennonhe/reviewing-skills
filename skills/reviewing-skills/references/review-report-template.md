# Review Report Template

Use this template to structure the skill review output. Replace placeholders with actual findings.

---

# Skill Review Report: [Skill Name]

**Review Date**: YYYY-MM-DD
**Skill Path**: `path/to/skill`
**Overall Score**: XX/100
**Status**: ✅ Excellent / ⚠️ Good / ⚠️ Fair / ❌ Needs Work

## Executive Summary

[2-3 sentence summary of overall compliance, major strengths, and primary concerns]

## Summary Table

| Category | Status | Score | Critical Issues | High Issues | Medium Issues | Low Issues |
|----------|--------|-------|-----------------|-------------|---------------|------------|
| Metadata | ✅/⚠️/❌ | XX/25 | N | N | N | N |
| Structure | ✅/⚠️/❌ | XX/25 | N | N | N | N |
| Content | ✅/⚠️/❌ | XX/25 | N | N | N | N |
| Code Quality | ✅/⚠️/❌ | XX/25 | N | N | N | N |
| **Total** | **✅/⚠️/❌** | **XX/100** | **N** | **N** | **N** | **N** |

## Recommendations

### 🔴 Critical Priority
*Issues that prevent proper skill functionality or violate core requirements*

- [ ] **[Issue Title]**: [Specific actionable recommendation]
  - **File**: `path/to/file:line`
  - **Current**: [What exists now]
  - **Expected**: [What should exist]
  - **Impact**: [Why this matters]

### 🟠 High Priority
*Issues that significantly impact usability or maintainability*

- [ ] **[Issue Title]**: [Specific actionable recommendation]
  - **File**: `path/to/file:line`
  - **Current**: [What exists now]
  - **Expected**: [What should exist]
  - **Impact**: [Why this matters]

### 🟡 Medium Priority
*Issues that affect quality but don't block functionality*

- [ ] **[Issue Title]**: [Specific actionable recommendation]
  - **File**: `path/to/file:line`
  - **Current**: [What exists now]
  - **Expected**: [What should exist]
  - **Impact**: [Why this matters]

### 🟢 Low Priority
*Minor improvements and polish*

- [ ] **[Issue Title]**: [Specific actionable recommendation]
  - **File**: `path/to/file:line`
  - **Current**: [What exists now]
  - **Expected**: [What should exist]
  - **Impact**: [Why this matters]

## Detailed Findings

### Metadata (XX/25) - ✅/⚠️/❌

#### Name Format (X/8)
- ✅/⚠️/❌ **Lowercase with hyphens** (X/3): [Findings]
- ✅/⚠️/❌ **Gerund form** (X/3): [Findings]
- ✅/⚠️/❌ **Concise and descriptive** (X/2): [Findings]

#### Description Quality (X/10)
- ✅/⚠️/❌ **Third-person perspective** (X/2): [Findings]
- ✅/⚠️/❌ **Under 1024 characters** (X/2): [Findings - actual count: N chars]
- ✅/⚠️/❌ **Includes triggers** (X/3): [Findings]
- ✅/⚠️/❌ **Describes use cases** (X/3): [Findings]

#### Frontmatter Fields (X/7)
- ✅/⚠️/❌ **Required fields present** (X/3): [Findings]
- ✅/⚠️/❌ **Argument hint provided** (X/2): [Findings]
- ✅/⚠️/❌ **Valid YAML syntax** (X/2): [Findings]

**Category Notes**: [Additional context or observations]

---

### Structure (XX/25) - ✅/⚠️/❌

#### Required Files (X/8)
- ✅/⚠️/❌ **SKILL.md exists** (X/5): [Findings]
- ✅/⚠️/❌ **Proper folder usage** (X/3): [Findings]

#### Reference Organization (X/9)
- ✅/⚠️/❌ **References one level deep** (X/5): [Findings - list any nested files]
- ✅/⚠️/❌ **Appropriate reference content** (X/4): [Findings]

#### Extraneous Files (X/8)
- ✅/⚠️/❌ **No README files** (X/3): [Findings - list any found]
- ✅/⚠️/❌ **No CHANGELOG files** (X/2): [Findings - list any found]
- ✅/⚠️/❌ **No test/development files** (X/3): [Findings - list any found]

**File Structure**:
```
skill-name/
├── SKILL.md (XXX lines)
├── references/
│   ├── file1.md (XXX lines)
│   └── file2.md (XXX lines)
└── scripts/
    ├── script1.py (XXX lines)
    └── script2.sh (XXX lines)
```

**Category Notes**: [Additional context or observations]

---

### Content (XX/25) - ✅/⚠️/❌

#### Body Length (X/8)
- ✅/⚠️/❌ **Under 500 lines** (X/5): [Findings - actual count: N lines]
- ✅/⚠️/❌ **Under 300 lines ideal** (X/3): [Findings - actual count: N lines]

#### Conciseness (X/9)
- ✅/⚠️/❌ **Examples over explanations** (X/4): [Findings with specific line references]
- ✅/⚠️/❌ **No redundant content** (X/3): [Findings with specific sections]
- ✅/⚠️/❌ **Direct and actionable** (X/2): [Findings]

#### Progressive Disclosure (X/8)
- ✅/⚠️/❌ **Layered information** (X/4): [Findings - describe information hierarchy]
- ✅/⚠️/❌ **Quick start accessible** (X/2): [Findings]
- ✅/⚠️/❌ **Deep dives available** (X/2): [Findings - list reference topics]

**Category Notes**: [Additional context or observations]

---

### Code Quality (XX/25) - ✅/⚠️/❌

#### Error Handling (X/8)
- ✅/⚠️/❌ **Explicit error messages** (X/3): [Findings with file references]
- ✅/⚠️/❌ **Input validation** (X/3): [Findings with file references]
- ✅/⚠️/❌ **Graceful degradation** (X/2): [Findings]

#### Path Conventions (X/7)
- ✅/⚠️/❌ **Forward slashes** (X/3): [Findings - list any backslashes found]
- ✅/⚠️/❌ **Relative paths** (X/2): [Findings - list any absolute paths]
- ✅/⚠️/❌ **Cross-platform compatible** (X/2): [Findings]

#### Dependencies (X/6)
- ✅/⚠️/❌ **Dependencies documented** (X/3): [Findings - list all dependencies]
- ✅/⚠️/❌ **Installation instructions** (X/2): [Findings]
- ✅/⚠️/❌ **Optional vs required** (X/1): [Findings]

#### Code Standards (X/4)
- ✅/⚠️/❌ **No magic constants** (X/2): [Findings with file references]
- ✅/⚠️/❌ **Consistent style** (X/2): [Findings]

**Category Notes**: [Additional context or observations]

---

## Appendix

### Automated Metrics
```json
{
  "skill_md_total_lines": 0,
  "skill_md_body_lines": 0,
  "description_length": 0,
  "frontmatter_valid": true/false,
  "files": [
    {"path": "...", "lines": 0}
  ]
}
```

### Review Methodology
- Automated metrics collected via `skill-analyzer.py`
- Manual review against `best-practices-checklist.md`
- Cross-referenced with `common-issues.md`
- Scoring based on official Anthropic guidelines

### Next Steps
1. [Action item based on critical priority recommendations]
2. [Action item based on high priority recommendations]
3. [Schedule follow-up review if needed]

---

*Review conducted by Claude Code Reviewing Skills v1.0*
