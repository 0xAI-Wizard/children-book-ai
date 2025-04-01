# Prompt Reference System

---

title: "Prompt Reference System"
version: "1.0"
purpose: "Define standardized cross-referencing between prompts"
last_updated: "2024-03-26"

---

## Reference Structure

### 1. Prompt Headers

All prompts must include the following metadata:

```yaml
---
title: "Prompt Name"
version: "X.Y"
purpose: "Brief description of prompt's role"
dependencies:
  - file: "dependent-file.md"
    version: ">=X.Y"
    sections: ["Required Section Names"]
input_requirements:
  - type: "INPUT_TYPE"
    format: "Format specification"
    validation: "Validation rules"
output_specifications:
  - type: "OUTPUT_TYPE"
    format: "Format specification"
    validation: "Validation rules"
last_updated: "YYYY-MM-DD"
---
```

### 2. Section References

When referencing content from other files:

```markdown
<REFERENCE>
source: "file.md"
section: "Section Name"
version: ">=X.Y"
purpose: "Why this reference is needed"
key_elements:
  - Element 1
  - Element 2
</REFERENCE>
```

### 3. Process Control Blocks

For managing workflow and dependencies:

```markdown
<PROCESS_CONTROL>
stage: "Current Stage Name"
prerequisites:

- "Prerequisite 1"
- "Prerequisite 2"
  next_steps:
- "Next Step 1"
- "Next Step 2"
  decision_points:
- "Decision 1"
- "Decision 2"
  </PROCESS_CONTROL>
```

### 4. Context Tracking

For maintaining context across prompts:

```markdown
<CONTEXT>
story_phase: "Current narrative phase"
active_elements:
  characters: ["Character 1", "Character 2"]
  settings: ["Setting 1", "Setting 2"]
  themes: ["Theme 1", "Theme 2"]
style_context:
  approved_style: "Style name"
  consistent_elements: ["Element 1", "Element 2"]
</CONTEXT>
```

### 5. Quality Verification

For ensuring output quality:

```markdown
<VERIFICATION>
checks:
  - description: "Check description"
    criteria: "Success criteria"
    reference: "Reference document"
consistency:
  - element: "Element to check"
    against: "Reference to check against"
    rules: "Consistency rules"
</VERIFICATION>
```

## Usage Guidelines

1. **Version Control**

- Always specify version requirements
- Use semantic versioning (MAJOR.MINOR)
- Include compatibility requirements

2. **Reference Chain**

- Maintain clear dependency paths
- Document reference purpose
- Validate references exist

3. **Context Preservation**

- Track story and style context
- Maintain character consistency
- Preserve approved decisions

4. **Error Prevention**

- Validate all references
- Check version compatibility
- Verify content consistency

5. **Quality Assurance**

- Implement all verification steps
- Document verification results
- Track consistency across prompts
