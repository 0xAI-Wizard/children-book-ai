from runway_book_generator import generate_book_illustration

if __name__ == "__main__":
    # Example test prompt for Kalea's book cover
    test_prompt = """
    Realistic children's book illustration, warm friendly style,
    a smiling 2.5-year-old girl named Kalea holding a bright red box with her name on it,
    her dog and two cats (one black, one gray) are peeking around her,
    bright colors featuring reds and pinks, clear simple details appropriate for a toddler's book,
    excitement and anticipation mood, glimpses of treasures visible in the open box
    """

    # Generate a test illustration for the cover
    generate_book_illustration(test_prompt, "test_cover")
