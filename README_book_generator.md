# Kalea's Book Illustration Generator

This tool automatically generates illustrations for Kalea's custom children's book using RunwayML's AI image generation API with the Dreamshaper model.

## Setup Instructions

1. **Install Python Requirements**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API Key**:

   - Edit the `.env` file and replace `your_api_key_here` with your actual RunwayML API key
   - Your API key can be found in your RunwayML account settings under "API Keys"

3. **Prepare Markdown File**:
   - Make sure your book project file (`daughters_custom_book_project.md`) is in the same directory
   - The tool will automatically extract illustration descriptions from the "Illustration Specifications" section

## Usage

Run the script with the following command:

```bash
python runway_book_generator.py
```

### Interactive Menu Options

The tool provides an interactive menu with the following options:

1. **Generate All Illustrations**:

   - Processes all pages in the book project
   - Shows you each prompt and asks for confirmation before generating
   - Saves images to the "book_illustrations" folder

2. **Generate a Single Illustration**:

   - Generate just one specific page illustration
   - Useful for re-doing a single page that needs adjustments

3. **View Available Pages**:

   - See a list of all pages that have illustration descriptions

4. **Exit**:
   - Quit the program

## Output

All generated illustrations will be saved to the "book_illustrations" folder with filenames:

- `cover.png` for the book cover
- `page_01.png`, `page_02.png`, etc. for each page

## Important Notes

- The default image resolution is 768x768 pixels
- Each image generation consumes RunwayML credits
- There's a short pause between API calls to avoid rate limiting
- For best results, review the generated prompts before confirming generation
- You can manually adjust prompt text in the code if needed

## Troubleshooting

- If you see an "API key not found" error, make sure your `.env` file is correctly configured
- If you encounter API errors, check your RunwayML account to ensure you have available credits
