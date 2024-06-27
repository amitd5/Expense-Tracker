import csv
from collections import defaultdict

# Define the categories
categories = ['Food', 'Transportation', 'Entertainment', 'Other']

# Function to get user input
def get_user_input():
    try:
        amount = float(input("Enter the amount spent: "))
        description = input("Enter a brief description: ")
        date = input("Enter the date (YYYY-MM-DD): ")
        return amount, description, date
    except ValueError:
        print("Invalid input. Please enter numeric values for amount and correct format for date.")
        return None

# Function to get user input with category
def get_user_input_with_category():
    expense = get_user_input()
    if expense:
        amount, description, date = expense
        print("Categories: ", ", ".join(categories))
        category = input("Enter the category: ")
        if category not in categories:
            print("Invalid category. Please choose from the given categories.")
            return None
        return amount, description, date, category
    return None

# Function to save expense to CSV
def save_expense_to_csv(expense, filename='expenses.csv'):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(expense)

# Function to read expenses from CSV
def read_expenses_from_csv(filename='expenses.csv'):
    expenses = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        expenses = list(reader)
    return expenses

# Function to generate monthly summary
def generate_monthly_summary(filename='expenses.csv'):
    monthly_expenses = defaultdict(float)
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                date = row[2]
                amount = float(row[0])
                month = date[:7]
                monthly_expenses[month] += amount
    except FileNotFoundError:
        print("No expenses found. Please add some expenses first.")
    return dict(monthly_expenses)

# Function to generate category summary
def generate_category_summary(filename='expenses.csv'):
    category_expenses = defaultdict(float)
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                amount = float(row[0])
                category = row[3]
                category_expenses[category] += amount
    except FileNotFoundError:
        print("No expenses found. Please add some expenses first.")
    return dict(category_expenses)

# Function to display the menu
def display_menu():
    print("\nExpense Tracker Menu")
    print("1. Add an expense")
    print("2. View monthly summary")
    print("3. View category summary")
    print("4. Exit")

# Main function to run the expense tracker
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            expense = get_user_input_with_category()
            if expense:
                save_expense_to_csv(expense)
                print("Expense added successfully!")
        elif choice == '2':
            summary = generate_monthly_summary()
            print("Monthly Summary:", summary)
        elif choice == '3':
            summary = generate_category_summary()
            print("Category Summary:", summary)
        elif choice == '4':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
