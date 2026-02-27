import sqlite3
from datetime import date
import argparse

def add_expense(name, category, amount):
    
    connection = sqlite3.connect("Budget.db")
    cursor = connection.cursor()
    
    today = date.today().isoformat()
    
    sql_query = """INSERT INTO expenses (name, category, amount, date) VALUES(?, ?, ?, ?);"""

    values = (name, category, amount, today)
    
    cursor.execute(sql_query, values)
    
    connection.commit()
    connection.close()
    
    print(f"Expense '{name}' added successfully with amount Rs.{amount} in category '{category}' on {today}.")
    
def view_expenses():
    connection = sqlite3.connect("Budget.db")
    cursor = connection.cursor()
    
    sql_query = """SELECT * FROM expenses;"""
    cursor.execute(sql_query)
    
    rows = cursor.fetchall()
    connection.close()
    
    # Print the expenses in a readable format
    print("Expenses: ")
    
    if len(rows) == 0:
        print("No expenses found")
    else:
        print(f"{'ID':<5} {'Name':<20} {'Category':<15} {'Amount Rs.':<10} {'Date':<12}")
        
        print("-" * 65) 
        
        for row in rows:
            print(f"{row[0]:<5} {row[1]:<20} {row[3]:<15} {row[2]:<10.2f} {row[4]:<12}")
            
            
def delete_expense(expense_id):
    connection = sqlite3.connect("Budget.db")
    cursor = connection.cursor()
    
    sql_query = """DELETE FROM expenses WHERE id = ?;"""
    
    cursor.execute(sql_query, (expense_id,))
    
    connection.commit()
    connection.close()
    
    print(f"Expense with ID {expense_id} has been deleted successfully.")
    
    # --- ARGUMENT PARSER (The Interface) ---
def clear_data():
    connection = sqlite3.connect("Budget.db")
    cursor = connection.cursor()
    
    cursor.execute("DELETE FROM expenses;")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='expenses';")
    
    connection.commit()
    connection.close()
    
    print("All expenses have been cleared successfully.")
    
def main():
    # 1. Create the Parser
    # This object handles the reading of the command line inputs.
    parser = argparse.ArgumentParser(description="BudgetBuddy CLI - Track your finances.")
    
    # 2. Create Sub-Commands
    # We want different modes: 'add' mode and 'view' mode.
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # --- COMMAND: ADD ---
    # This setup listens for: python budget.py add --name "X" --price Y --category Z
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--name", type=str, required=True, help="What did you buy?")
    add_parser.add_argument("--price", type=float, required=True, help="How much was it?")
    add_parser.add_argument("--category", type=str, default="Misc", help="Category (Food, Travel, etc)")
    
    # --- COMMAND: VIEW ---
    # This setup listens for: python budget.py view
    subparsers.add_parser("view", help="View all expenses")
    
    del_parser = subparsers.add_parser("delete", help="Delete expense by ID")
    del_parser.add_argument("--id", type= int, required=True, help="ID of the expense to delete")
    
    subparsers.add_parser("clear", help="Clear all expenses")
    
    # 3. Parse the Arguments
    # This line actually reads what you typed in the terminal.
    args = parser.parse_args()
    
    # 4. Logic Switch
    # Decide which function to run based on the command.
    if args.command == "add":
        add_expense(args.name, args.category, args.price)
    elif args.command == "view":
        view_expenses()
    elif args.command =="delete":
        delete_expense(args.id)
    elif args.command == "clear":
        confirm = input("Are you sure you want to clear all expenses? This action cannot be undone.(yes/no): ")
        if confirm.lower() == "yes":
            clear_data()
        else :
            print("Operation Cancelled!")
        # If they run the script without a command, show help.
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
