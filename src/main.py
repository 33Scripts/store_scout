from utils import load_data
from recommendation import search_category, display_category_items


def main():
    """Main entry point for Store Scout.

    Loads product data, displays an introductory message along with available categories,
    and continuously prompts the user for input to display matching products.
    """
    data = load_data()
    if not data:
        print("No data found.")
        return

    # ASCII art and welcome message
    ascii_art = r"""
  ____  _                   ____                  _   
/ ___|| |_ ___  _ __ ___  / ___|  ___ ___  _   _| |_ 
\___ \| __/ _ \| '__/ _ \ \___ \ / __/ _ \| | | | __|
 ___) | || (_) | | |  __/  ___) | (_| (_) | |_| | |_ 
|____/ \__\___/|_|  \___| |____/ \___\___/ \__,_|\__|
    """.lstrip("\n")
    print(ascii_art)
    print("Welcome to Store Scout!")
    print("This tool helps you find products by category.\n")

    # Display available categories
    available_categories = [cat.capitalize() for cat in data.keys()]
    print("Available categories:", ", ".join(available_categories))
    
    # Define prompt message for user input
    prompt_message = """
Enter one of the following:
- Category name (or beginning letters)
- "all" to list all items
- "help" to see available categories
- "exit" to quit
> """

    while True:
        # Prompt user for input
        user_input = input(prompt_message).strip().lower()

        # Validate input
        if not user_input:
            input("Please enter a valid input. Press Enter to continue.")
            continue

        # Show available categories
        if user_input == "help":
            print("Available categories:", ", ".join(available_categories))
            continue

        # Show all categories with pagination per category
        elif user_input == "all":
            # Display products from all categories one by one with pagination for each
            categories = list(data.keys())
            for idx, category in enumerate(categories):
                print(f"\n=== Category: {category.capitalize()} ===")
                display_category_items(data, category)
                # Prompt to continue if more categories exist
                if idx < len(categories) - 1:
                    cont = input("Press Enter to view the next category, or type 'q' to quit: ").strip().lower()
                    if cont == "q":
                        break
            continue
        
        # Exit the program
        elif user_input == "exit":
            break

        # Search for matching categories using user input
        matches = search_category(data, user_input)
        if len(matches) == 0:
            input("No matching categories found. Please try again. Press Enter to continue.")
            continue
        elif len(matches) == 1:
            # Single match found, display products for that category
            display_category_items(data, matches[0])
        else:
            # Multiple matches found, ask user to select a category
            print("Multiple categories found:")
            for idx, cat in enumerate(matches):
                print(f"{idx + 1}. {cat.capitalize()}")
            try:
                choice = int(input("Select a category by entering its number: "))
                if 1 <= choice <= len(matches):
                    display_category_items(data, matches[choice - 1])
                else:
                    input("Invalid selection. Please try again. Press Enter to continue.")
                    continue
            except ValueError:
                input("Invalid input. Please enter a number. Press Enter to continue.")
                continue

        # Ask if the user wants to search again
        if input("Would you like to search for another category? (Y/n): ").strip().lower() == "n":
            break

    print("\nThank you for using Store Scout.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nThank you for using Store Scout.")
