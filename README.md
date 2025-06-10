# Expense Tracker


#### Description:

**Expense Tracker ** is a terminal-based Python application that allows users to manage their daily expenses with ease. It provides an intuitive interface for adding, viewing, searching, and deleting expenses, along with calculating the total amount spent. The project is built using Python and leverages third-party libraries like `rich` and `pyfiglet` for enhanced user experience through colorful tables and ASCII banners.

---

## Features

- **Add Expense**: Record a new expense by entering the amount, category, and description.
- **View Expenses**: Display all expenses in a well-formatted table using the `rich` library.
- **Total Expenses**: Calculate and display the sum of all expenses added.
- **Search Expenses**: Find expenses by keyword in the category or description.
- **Delete Expense**: Remove an expense by entering its unique ID.
- **User Interface**: Clean and visually appealing terminal output with ASCII art and styled tables.

---

## Files Overview

- `project.py`: Contains all the application logic including:
    - `main()` – Entry point for running the program.
    - `add_expense()` – Adds an expense to the global list.
    - `view_expenses()` – Displays all expenses using a formatted table.
    - `total_expenses()` – Calculates total expense amount.
    - `search_expenses()` – Finds matching expenses based on keyword.
    - `delete_expense()` – Deletes an expense by its ID.
    - `print_expenses_table()` – Helper function for displaying expenses in a `rich` table format.

- `test_project.py`: Contains unit tests for the core functionalities using `pytest`. Includes tests for:
    - `add_expense()`
    - `view_expenses()`
    - `total_expenses()`
    - `search_expenses()`
    - `delete_expense()`

- `requirements.txt`: Lists the external dependencies required to run the application.

- `README.md`: This documentation file, explaining the purpose, structure, and functionality of the project.

---

## Design Choices

- The decision to use a ** global list ** (`expenses`) made it simple to manage state within the app without database complexity.
- The **`rich` library ** was chosen to make the terminal output much more user-friendly and visually appealing.
- ASCII art from **`pyfiglet`** enhances the presentation and adds a polished feel to the command-line interface.
- Functions were kept simple and modular to aid readability and ease of testing.
- All test cases use `pytest` with a `clean_slate` fixture to avoid state leakage across tests.

---

## How to Run

1. Install dependencies:

    ```bash
    pip install - r requirements.txt

2. Run the Application:

    ```bash
    python project.py

3. (Optional) Run the Test:

    ```bash
    pytest test_project.py
# Python-projects
# python-budgetBuddy
