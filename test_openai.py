import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

if __name__ == "__main__":
    if not api_key:
        print("Error: OPENAI_API_KEY not found in .env file")
        exit(1)

    # Set the OpenAI API key
    openai.api_key = api_key

    print("Testing OpenAI API connection...")

    try:
        # Simple test - get models list
        response = openai.models.list()

        # Print the first few models
        print("Connection successful! Available models:")
        for model in response.data[:5]:  # Show just first 5
            print(f"- {model.id}")
        print("...")

        print("\nOpenAI API connection is working correctly.")
    except Exception as e:
        print(f"Error connecting to OpenAI API: {e}")
