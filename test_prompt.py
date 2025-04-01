import os
import requests
import json
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def generate_image(prompt, output_filename="test_illustration.png"):
    """
    Generate an image using OpenAI's DALL-E API

    Args:
        prompt (str): The text prompt for the image
        output_filename (str): Where to save the generated image
    """
    # API key for OpenAI
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("Error: OPENAI_API_KEY not found in .env file")
        return False

    # Create OpenAI client
    client = OpenAI(api_key=api_key)

    # Make request to OpenAI DALL-E API
    try:
        print(f"Generating image with prompt: {prompt[:60]}...")

        # Generate the image using DALL-E
        response = client.images.generate(
            model="dall-e-3", prompt=prompt, n=1, size="1024x1024"
        )

        # Get the image URL from the response
        image_url = response.data[0].url

        # Download the image
        image_response = requests.get(image_url)
        image_response.raise_for_status()

        # Save the image
        with open(output_filename, "wb") as f:
            f.write(image_response.content)

        print(f"Image successfully generated and saved to {output_filename}")
        return True

    except Exception as e:
        print(f"Error: {e}")
        return False


if __name__ == "__main__":
    # Example test prompt for Kalea's book cover
    test_prompt = """
    Realistic children's book illustration, warm friendly style,
    a smiling 2.5-year-old girl named Kalea holding a bright red box with her name on it,
    her dog and two cats (one black, one gray) are peeking around her,
    bright colors featuring reds and pinks, clear simple details appropriate for a toddler's book,
    excitement and anticipation mood, glimpses of treasures visible in the open box
    """

    # Clean up the prompt (remove extra whitespace)
    test_prompt = " ".join(test_prompt.split())

    # Generate the test illustration
    generate_image(test_prompt)
