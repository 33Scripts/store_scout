def search_category(data, user_input):
    """Search for matching categories based on user input.

    If the input is "all", returns all categories.
    First checks for an exact match, then for categories starting with the input.

    Args:
        data (dict): The product data dictionary.
        user_input (str): The user's search input.

    Returns:
        list: A list of matching category names.
    """
    categories = list(data.keys())
    if user_input == "all":
        return categories

    # Check for an exact match
    exact_matches = [cat for cat in categories if cat.lower() == user_input]
    if exact_matches:
        return exact_matches

    # If no exact match, find categories that start with the input
    partial_matches = [cat for cat in categories if cat.lower().startswith(user_input)]
    return partial_matches


def display_category_items(data, category, page_size=5):
    """Display products for a given category with optional pagination.

    If the number of products exceeds the page size, the function paginates the results,
    allowing navigation through pages. Otherwise, it prints all products at once.

    Args:
        data (dict): The product data dictionary.
        category (str): The category to display.
        page_size (int): Number of products to display per page. Defaults to 5.
    """
    products = data.get(category, [])
    if not products:
        print(f"No products found in category '{category}'.")
        return

    total_products = len(products)

    # If products fit on one page, display them all at once
    if total_products <= page_size:
        print(f"\nProducts in '{category.capitalize()}' category:")
        for product in products:
            print("--------------------------")
            print(f"Name: {product['name']}")
            print(f"Price: {product['price']}")
            print(f"Rating: {product['rating']}")
            print(f"Description: {product['description']}")
            print("--------------------------")
        return

    # Calculate total pages and initialize current page
    total_pages = (total_products + page_size - 1) // page_size
    current_page = 1

    while True:
        start = (current_page - 1) * page_size
        end = start + page_size
        print(f"\nProducts in '{category.capitalize()}' category (Page {current_page}/{total_pages}):")
        for product in products[start:end]:
            print("--------------------------")
            print(f"Name: {product['name']}")
            print(f"Price: {product['price']}")
            print(f"Rating: {product['rating']}")
            print(f"Description: {product['description']}")
            print("--------------------------")

        # Build allowed navigation options based on current page
        allowed_options = {}
        print("\nNavigation options:")
        if current_page > 1:
            allowed_options["p"] = "Previous page"
            print("P - Previous page")
        if current_page < total_pages:
            allowed_options["n"] = "Next page"
            print("N - Next page")
        allowed_options["q"] = "Quit pagination"
        print("Q - Quit pagination")

        # Only accept allowed options
        choice = input("Enter your choice: ").strip().lower()
        if choice not in allowed_options:
            input("Invalid choice. Please enter one of the allowed options. Press Enter to continue.")
            continue

        if choice == "n":
            current_page += 1
        elif choice == "p":
            current_page -= 1
        elif choice == "q":
            break
