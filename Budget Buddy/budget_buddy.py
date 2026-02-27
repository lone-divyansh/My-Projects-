# --- CLASS DEFINITION (The Blueprint) ---
class Expense:
    """
    This class acts as a 'Blueprint' for every expense.
    Instead of just a list of numbers, we create an Object that knows
    its own name, price, and quantity.
    """
    def __init__(self, name, amount, qty):
        """
        The Constructor. This runs automatically when you create a new Expense().
        It sets up the initial data for the object.
        """
        self.name = name       # Variable to store the item name (e.g., "Coffee")
        self.amount = amount   # Variable to store the price per item (e.g., 5.0)
        self.qty = qty         # Variable to store how many items (e.g., 2)

    def get_total(self):
        """
        A Method (function inside a class) that calculates the total cost.
        Formula: Price * Quantity
        """
        return self.amount * self.qty


# --- FUNCTION 1: DISPLAY TO SCREEN ---
def print_receipt(receipt_data):
    """
    Loops through the list of Expense objects and prints them to the console.
    
    Args:
        receipt_data (list): A list containing Expense objects.
    """
    print("\n - - - Your Receipt - - - ")

    total_spent = 0 # Accumulator variable to keep running total

    for item in receipt_data:
        # 'item' is one Expense object from the list
        
        # 1. Ask the object to calculate its own total cost
        unit_total = item.get_total()

        # 2. Print the details using f-string
        # We access data using DOT notation (item.name, item.amount)
        print(f"You Spent ${item.amount} on {item.qty} {item.name}") 
        
        # 3. Add this item's cost to the grand total
        total_spent = total_spent + unit_total

    print(f"Your Grand total : {total_spent}")


# --- FUNCTION 2: SAVE TO FILE ---
def save_receipt(receipt_data):
    """
    Loops through the list of Expense objects and writes them to a text file.
    """
    # 'with open' safely opens the file and closes it automatically when done.
    # "w" mode means WRITE (it will overwrite existing files).
    with open("budget_receipt.txt", "w") as file:
        
        file.write("- - - Your Receipt - - - \n") # \n means New Line
        total_spent = 0
    
        for item in receipt_data:
            # Same logic as print_receipt, but writing to file
            unit_total = item.get_total()

            # Create the string variable first
            line = f"You Spent ${item.amount} on {item.qty} {item.name}\n"

            file.write(line) # Write the string to the text file
            total_spent = total_spent + unit_total

        file.write(f"Your Grand total : {total_spent}\n")

    print("Receipt saved to budget_receipt.txt")


# --- MAIN PROGRAM EXECUTION STARTS HERE ---

expenses = [] # An empty list to store all our Expense objects
print("Welcome to BudgetBuddy")

# Start the Infinite Loop (The "Game Loop")
while True:
    # 1. Get the Name
    Expense_name = input("Enter Your Expense: " )

    # Validation: Ensure they didn't type numbers as a name
    if Expense_name.isdigit():
        print("please enter a valid item.")
        continue # Skip the rest of the loop and start over

    # 2. Get Quantity and Amount (Protected by Error Handling)
    while True:
        try:
            quantity = int(input("Enter How many you got : "))
            Expense_amount = float(input("Enter the Price per unit You Spent: " ))
            break # If lines above work, break this inner loop
        except ValueError:
            # If user types "abc" instead of numbers, this runs
            print("Please enter valid numeric values for quantity and amount.")
            continue 

    # 3. Create the Object 
    # We call the Class to build a real object with the user's data
    current_expense = Expense(Expense_name, Expense_amount, quantity)
    
    # 4. Ask to continue
    user_input = input("Anything Else ? (Yes/no): " )
    
    # 5. Save the object into our list
    expenses.append(current_expense)
    
    # Check if we should stop the main loop
    if user_input == "no":
        break

# Call the helper functions to show results
print_receipt(expenses)
save_receipt(expenses)