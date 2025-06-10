import os
import pyfiglet

from rich.console import Console
from rich.table import Table

console = Console()

ascii_banner = pyfiglet.figlet_format("Welcome to Budget Buddy!")
print(ascii_banner)


expenses = []


def print_expenses_table(expense_list):
    """
    Takes a list of expense dictionaries and prints them in a formatted table.
    """

    table = Table(title="Expense Report", show_header=True,
                  header_style="bold magenta")

    table.add_column("ID", style="dim", width=4)
    table.add_column("Amount", justify="right", style="green")
    table.add_column("Category", style="cyan")
    table.add_column("Description", min_width=20, style="yellow")

    for expense in expense_list:
        table.add_row(
            str(expense['id']),
            f"${expense['amount']:.2f}",
            expense['category'],
            expense['description']
        )

    console.print(table)


def add_expense(amount: float, category: str, description: str):
    """Add an expense to the tracker."""
    expense = {
        "id": len(expenses) + 1,
        "amount": amount,
        "category": category,
        "description": description
    }
    expenses.append(expense)

    console.print(
        f"✅ Expense added: [bold green]${amount:.2f}[/bold green] "
        f"[cyan]({category})[/cyan] - [italic][yellow]{description}[/yellow][/italic]"
    )


def view_expenses():
    """Display all expenses using the new table function."""
    print_expenses_table(expenses)


def total_expenses():
    """Calculate the total of all expenses."""
    total = sum(expense["amount"] for expense in expenses)
    console.print(f"Total expenses: [bold green]${total:.2f}[/bold green]")
    return total


def search_expenses(keyword: str):
    """Search expenses and display results in a table."""
    results = [
        expense for expense in expenses
        if keyword.lower() in expense["description"].lower() or
        keyword.lower() in expense["category"].lower()
    ]
    print_expenses_table(results)
    return results


def delete_expense(expense_id: int):
    """Delete an expense by its ID."""
    expense_to_delete = next(
        (exp for exp in expenses if exp["id"] == expense_id), None)

    if expense_to_delete:
        expenses.remove(expense_to_delete)
        console.print(
            f"🗑️ Expense with ID {expense_id} ('{expense_to_delete['description']}') has been deleted.", style="red")
        return True
    else:
        console.print(
            f"❌ No expense found with ID {expense_id}.", style="bold red")
        return False


def main():
    """Main program loop."""
    while True:
        console.print("\n--- Welcome to the Expense Tracker! ---",
                      style="bold blue")
        console.print("1. Add Expense")
        console.print("2. View Expenses")
        console.print("3. View Total Expenses")
        console.print("4. Search Expenses")
        console.print("5. Delete Expense")
        console.print("6. Exit")

        choice = input("Please select an option (1-6): ")

        if choice == '1':
            try:
                amount = float(input("Enter the amount: $"))
                category = input("Enter the category: ")
                description = input("Enter the description: ")
                add_expense(amount, category, description)
            except ValueError:
                console.print(
                    "❌ Invalid amount. Please enter a number.", style="bold red")

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            total_expenses()

        elif choice == '4':
            keyword = input("Enter a keyword to search: ")
            search_expenses(keyword)

        elif choice == '5':
            try:
                expense_id = int(input("Enter the expense ID to delete: "))
                delete_expense(expense_id)
            except ValueError:
                console.print(
                    "❌ Invalid ID. Please enter a number.", style="bold red")

        elif choice == '6':
            console.print("Goodbye!", style="bold")
            break

        else:
            console.print("Invalid choice, please try again.",
                          style="bold red")


if __name__ == "__main__":
    main()
