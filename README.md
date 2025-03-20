# Store Scout

Store Scout is a Python-based product recommendation system that allows users to search for products by category. It loads product data from a JSON file, supports partial matching, and features pagination for easy navigation through product listings.

## Features

- **Category Search:** Find products by entering a full category name or just the beginning letters.
- **Multiple Options:** If multiple categories match, the user can choose which one to view.
- **Pagination:** Navigate through products with "next," "previous," and "quit" options when there are many items.
- **All Categories:** View all categories one by one.
- **User-Friendly:** Clear prompts and help commands guide the user.
- **Easy Data Modification:** Update or expand the product data easily by editing the JSON file.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/33Scripts/store_scout.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd store_scout
   ```

3. **Set Up Environment:**

   Ensure you have Python 3.8 or later installed.
   This project uses [Poetry](https://python-poetry.org/).
   If you don't have Poetry installed, install it with:
   ```bash
   pip install poetry
   ```
   Even though no third-party dependencies are required, you can set up the environment with:
   ```bash
   poetry install
   ```

5. **Run the Application:**

   ```bash
   python src/main.py
   ```

## Usage

- Follow the on-screen prompts to search for product categories.
- Enter `"all"` to list products from all categories.
- Use `"help"` to see the list of available categories at any time.
- When viewing products, use:
  - **N** for the next page,
  - **P** for the previous page,
  - **Q** to quit pagination.

## License

This project is licensed under the [MIT License](LICENSE).
