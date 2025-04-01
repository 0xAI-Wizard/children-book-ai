import json
import time
from runway_book_generator import generate_book_illustration


def load_and_generate_illustrations(prompts_file="prompts.json"):
    """
    Load prompts from JSON file and generate illustrations

    Args:
        prompts_file (str): Path to the JSON file with prompts
    """
    # Load prompts from JSON
    try:
        with open(prompts_file, "r") as f:
            prompts = json.load(f)
    except FileNotFoundError:
        print(f"Error: Could not find {prompts_file}")
        print("Run edit_prompts.py first to extract prompts from the markdown file.")
        return
    except json.JSONDecodeError:
        print(f"Error: {prompts_file} is not valid JSON")
        return

    if not prompts:
        print("No prompts found in the JSON file.")
        return

    print(f"Found {len(prompts)} prompts in {prompts_file}")

    # Generate illustrations for each prompt
    for item in prompts:
        page = item["page"]
        prompt = item["prompt"]

        print(f"\nGenerating illustration for page {page}:")
        print(f"Prompt: {prompt}\n")

        # Add a confirmation step
        proceed = input("Generate this illustration? (y/n): ")
        if proceed.lower() == "y":
            generate_book_illustration(prompt, page)

            # Wait a bit between API calls to avoid rate limiting
            time.sleep(2)
        else:
            print("Skipping this illustration.")


if __name__ == "__main__":
    load_and_generate_illustrations()
