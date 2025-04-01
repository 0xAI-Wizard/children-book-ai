# Children's Book Creator System - Master Index

---

title: "Children's Book Creator System - File Index and Relationship Map"
version: 1.0
purpose: "Master index for navigating all related prompts, examples, and templates"
last_updated: "2023-03-24"

---

## Overview

This repository contains a complete system for AI-assisted children's book creation, including:

- Process guidance prompts
- Character description templates
- Illustration prompts
- Story creation workflows
- Example projects

## File Structure and Relationships

### 1. Main Process Prompt

- `/prompts/story-generation/custom_childrens_book_agent_prompt.md` - The main AI agent process prompt

### 2. Illustration Guidance

- `/prompts/illustrations/illustration-generation.md` - How to generate consistent illustrations
- `/prompts/illustrations/illustration-description-generation.md` - How to create detailed illustration descriptions

### 3. Template Files

- `/kaleas-book-prototype/book_creation_tracking_template.md` - Tracking template for book projects

### 4. Example Content

- `/kaleas-book-prototype/character-description.md` - Example character descriptions
- `/kaleas-book-prototype/kaleas-book-content.md` - Example story content with illustrations
- `/kaleas-book-prototype/daughters_custom_book_project.md` - Example of a completed project
- `/samples/sample_conversation_demonstration.md` - Example agent-client conversation

## Process Flow

1. Begin with the main process prompt (`custom_childrens_book_agent_prompt.md`)
2. Use the tracking template (`book_creation_tracking_template.md`) to document the project
3. Create detailed character descriptions following the format in `character-description.md`
4. Develop the story content with illustration descriptions
5. Use `illustration-description-generation.md` to create detailed illustration prompts
6. Generate illustrations following `illustration-generation.md` guidance

## Key File Relationships

```
custom_childrens_book_agent_prompt.md
├── book_creation_tracking_template.md (output tracking)
├── character-description.md (character description format)
└── illustration guidance
    ├── illustration-description-generation.md (creating detailed art prompts)
    └── illustration-generation.md (generating consistent art)
```

## Example Projects

See the complete example "Kalea's Traveling Heart" in the `/kaleas-book-prototype/` directory, which demonstrates all aspects of the book creation process.

## Reference Guides

When using this system, the AI should reference all relevant files for each stage of the process:

1. **Initial consultation** → Main prompt for client questions
2. **Story concepts** → Example story concepts in sample conversations
3. **Character descriptions** → Character description template
4. **Illustration guidance** → Illustration guidance files
5. **Project tracking** → Book creation tracking template
