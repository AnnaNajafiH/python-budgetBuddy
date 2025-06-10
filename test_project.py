import pytest

from project import (
    add_expense,
    view_expenses,
    total_expenses,
    search_expenses,
    delete_expense,
    expenses
)


@pytest.fixture(autouse=True)
def clean_slate():
    """
    A pytest fixture that runs automatically before each test function.
    It ensures the global 'expenses' list is empty, so that each test
    starts fresh and is not affected by previous tests.
    """
    expenses.clear()


def test_add_expense():
    """Tests the add_expense function."""
    add_expense(50.00, "Groceries", "Weekly shopping")
    assert len(expenses) == 1
    assert expenses[0]["id"] == 1
    assert expenses[0]["amount"] == 50.00
    assert expenses[0]["category"] == "Groceries"

    add_expense(15.50, "Transport", "Bus ticket")
    assert len(expenses) == 2
    assert expenses[1]["id"] == 2


def test_view_expenses(capsys):
    """
    Tests the view_expenses function by capturing its printed output.
    'capsys' is a special pytest fixture that captures terminal output.
    """
    add_expense(99.99, "Tech", "New mouse")
    view_expenses()
    captured = capsys.readouterr()
    assert "Expense Report" in captured.out
    assert "99.99" in captured.out
    assert "Tech" in captured.out

    expenses.clear()
    view_expenses()
    captured = capsys.readouterr()
    assert "Expense Report" in captured.out
    assert "$" not in captured.out


def test_total_expenses():
    """Tests the total_expenses function."""
    assert total_expenses() == 0

    add_expense(100.00, "Rent", "Monthly rent")
    add_expense(25.50, "Food", "Dinner")
    assert total_expenses() == 125.50


def test_search_expenses():
    """Tests the search_expenses function."""
    add_expense(10.00, "Food", "Cheese and crackers")
    add_expense(20.00, "Transport", "Train ticket")
    add_expense(30.00, "Food", "Lunch with a client")

    results_food = search_expenses("Food")
    assert len(results_food) == 2

    results_ticket = search_expenses("TICKET")
    assert len(results_ticket) == 1
    assert results_ticket[0]["category"] == "Transport"

    results_none = search_expenses("nonexistent_keyword")
    assert len(results_none) == 0


def test_delete_expense():
    """Tests the delete_expense function."""
    add_expense(20.00, "Entertainment", "Movie ticket")
    add_expense(30.00, "Bills", "Internet bill")

    assert len(expenses) == 2

    result_success = delete_expense(1)
    assert result_success is True
    assert len(expenses) == 1
    assert expenses[0]["id"] == 2

    result_fail = delete_expense(99)
    assert result_fail is False
    assert len(expenses) == 1
