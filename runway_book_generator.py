import requests
import json
import os
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
API_KEY = os.getenv("RUNWAY_API_KEY")

# RunwayML API endpoints
RUNWAY_API_URL = "https://api.runwayml.com/v1/inference"


def generate_book_illustration(prompt, page_number, style="dreamshaper"):
    """
    Generate an illustration using RunwayML API

    Args:
        prompt (str): The description of the image to generate
        page_number (int or str): The page number for file naming
        style (str): Model style to use (default: dreamshaper)

    Returns:
        str: Path to the downloaded image
    """
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

    payload = {
        "prompt": prompt,
        "model": style,
        "negative_prompt": "deformed, ugly, disfigured, poor anatomy, bad proportions, distorted face",
        "num_outputs": 1,
        "width": 768,
        "height": 768,
        "steps": 30,
        "guidance_scale": 7.5,
    }

    print(f"Generating image for page {page_number}...")

    try:
        response = requests.post(RUNWAY_API_URL, headers=headers, json=payload)
        response.raise_for_status()

        result = response.json()
        image_url = result["output"][0]

        # Download the image
        image_response = requests.get(image_url)
        image_response.raise_for_status()

        # Create output directory if it doesn't exist
        os.makedirs("book_illustrations", exist_ok=True)

        # Format page number for filename
        if page_number == "cover":
            output_path = f"book_illustrations/cover.png"
        else:
            output_path = f"book_illustrations/page_{int(page_number):02d}.png"

        # Save the image
        with open(output_path, "wb") as f:
            f.write(image_response.content)

        print(f"Image saved to {output_path}")
        return output_path

    except requests.exceptions.RequestException as e:
        print(f"Error generating image: {e}")
        return None


def extract_prompts_from_markdown(markdown_file):
    """
    Extract illustration prompts from the book project markdown file

    Args:
        markdown_file (str): Path to the markdown file

    Returns:
        list: List of dictionaries containing page numbers and prompts
    """
    prompts = []
    current_page = None
    in_illustration_section = False
    page_description = {}

    with open(markdown_file, "r") as f:
        lines = f.readlines()

    for line in lines:
        # Check if we're in the illustration specifications section
        if "## 6. Illustration Specifications" in line:
            in_illustration_section = True
            continue

        if in_illustration_section:
            # Check for page headers
            if line.strip().startswith("#### Page ") or line.strip().startswith(
                "#### Cover"
            ):
                # Save previous page if exists
                if current_page and page_description:
                    prompt = craft_prompt_from_description(page_description)
                    prompts.append({"page": current_page, "prompt": prompt})

                # Start new page
                if "Cover" in line:
                    current_page = "cover"
                else:
                    current_page = int(line.strip().replace("#### Page ", "").strip())

                page_description = {}
                continue

            # Extract key details
            if line.strip().startswith("- **Description**:"):
                page_description["description"] = line.split(":", 1)[1].strip()
            elif line.strip().startswith("- **Key Elements**:"):
                page_description["key_elements"] = line.split(":", 1)[1].strip()
            elif line.strip().startswith("- **Characters**:"):
                page_description["characters"] = line.split(":", 1)[1].strip()
            elif line.strip().startswith("- **Setting/Background**:"):
                page_description["setting"] = line.split(":", 1)[1].strip()
            elif line.strip().startswith("- **Actions/Emotions**:"):
                page_description["emotions"] = line.split(":", 1)[1].strip()
            elif line.strip().startswith("- **Special Notes**:"):
                page_description["notes"] = line.split(":", 1)[1].strip()
            elif line.strip().startswith("- **Text**:"):
                page_description["text"] = line.split(":", 1)[1].strip()

    # Add the last page
    if current_page and page_description:
        prompt = craft_prompt_from_description(page_description)
        prompts.append({"page": current_page, "prompt": prompt})

    return prompts


def craft_prompt_from_description(description):
    """
    Craft a RunwayML-optimized prompt from the page description

    Args:
        description (dict): Dictionary containing page description elements

    Returns:
        str: Optimized prompt for RunwayML
    """
    prompt_parts = [
        "Realistic children's book illustration with warm friendly details",
        "bright colors featuring reds and pinks",
        "clear, simple details appropriate for a toddler's book",
    ]

    if "description" in description:
        prompt_parts.append(description["description"])

    if "characters" in description:
        prompt_parts.append(f"Characters: {description['characters']}")

    if "setting" in description:
        prompt_parts.append(f"Setting: {description['setting']}")

    if "emotions" in description:
        prompt_parts.append(f"Mood: {description['emotions']}")

    if "key_elements" in description:
        prompt_parts.append(f"Including: {description['key_elements']}")

    if "notes" in description:
        prompt_parts.append(description["notes"])

    # Join all parts with commas
    return ", ".join(prompt_parts)


def generate_all_book_illustrations(markdown_file):
    """
    Generate all illustrations for the book project

    Args:
        markdown_file (str): Path to the markdown file
    """
    prompts = extract_prompts_from_markdown(markdown_file)

    if not prompts:
        print("No illustration descriptions found in the markdown file.")
        return

    print(f"Found {len(prompts)} illustration descriptions.")

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


def generate_single_illustration(markdown_file, page_number):
    """
    Generate a single illustration by page number

    Args:
        markdown_file (str): Path to the markdown file
        page_number (int or str): The page to generate (use "cover" for cover)
    """
    prompts = extract_prompts_from_markdown(markdown_file)

    # Find the prompt for the requested page
    selected_prompt = None
    for item in prompts:
        if str(item["page"]) == str(page_number):
            selected_prompt = item["prompt"]
            break

    if selected_prompt:
        print(f"\nGenerating illustration for page {page_number}:")
        print(f"Prompt: {selected_prompt}\n")

        generate_book_illustration(selected_prompt, page_number)
    else:
        print(f"No illustration description found for page {page_number}.")


def view_available_pages(markdown_file):
    """
    View all available pages that have illustration descriptions

    Args:
        markdown_file (str): Path to the markdown file
    """
    prompts = extract_prompts_from_markdown(markdown_file)

    if not prompts:
        print("No illustration descriptions found in the markdown file.")
        return

    print("\nAvailable pages for illustration generation:")
    for item in prompts:
        print(f"- Page {item['page']}")


def interactive_menu():
    """
    Display an interactive menu for the user
    """
    markdown_file = "daughters_custom_book_project.md"

    while True:
        print("\n=== Kalea's Book Illustration Generator ===")
        print("1. Generate all illustrations")
        print("2. Generate a single illustration")
        print("3. View available pages")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            generate_all_book_illustrations(markdown_file)
        elif choice == "2":
            page = input("Enter page number (or 'cover' for cover): ")
            generate_single_illustration(markdown_file, page)
        elif choice == "3":
            view_available_pages(markdown_file)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


# Main execution
if __name__ == "__main__":
    # Check if API key is set
    if not API_KEY:
        print("Error: RUNWAY_API_KEY not found in .env file")
        print("Please create a .env file with your RunwayML API key")
        exit(1)

    # Run the interactive menu
    interactive_menu()
