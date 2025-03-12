import json
import os
from runway_book_generator import extract_prompts_from_markdown


def extract_and_save_prompts(markdown_file, output_file="prompts.json"):
    """
    Extract prompts from markdown and save to a JSON file for editing

    Args:
        markdown_file (str): Path to the markdown file
        output_file (str): Path to save the extracted prompts
    """
    # Extract prompts from markdown
    prompts = extract_prompts_from_markdown(markdown_file)

    if not prompts:
        print("No prompts found in the markdown file.")
        return

    # Save to JSON file
    with open(output_file, "w") as f:
        json.dump(prompts, f, indent=2)

    print(f"Successfully extracted {len(prompts)} prompts and saved to {output_file}")
    print(
        "You can now edit the prompts in this file and then use load_and_generate.py to generate illustrations"
    )


if __name__ == "__main__":
    markdown_file = "daughters_custom_book_project.md"
    extract_and_save_prompts(markdown_file)
