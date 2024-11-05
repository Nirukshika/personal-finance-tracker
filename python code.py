import json

# Global dictionary to store transactions
transactions = {}

# File handling functions
def load_transactions():
    global transactions
    try:
        with open('transactions.json', 'r') as file:
            transactions = json.load(file)
    except FileNotFoundError:
        print("Transactions file not found.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")


def save_transactions():
    global transactions
    with open('transactions.json', 'w') as file:
        json.dump(transactions, file, indent=2)

def read_bulk_transactions_from_file(filename):
    global transactions
    try:
        with open(filename, 'r') as file:
            transactions = json.load(file)
    except FileNotFoundError:
     print("File not found.")

# Feature implementations
def add_transaction():
    global transactions
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    date = input("Enter date (YYYY-MM-DD): ")
    if category in transactions:
        transactions[category].append({"amount": amount, "date": date})
    else:
        transactions[category] = [{"amount": amount, "date": date}]
    print("Transaction added successfully.")

def view_transactions():
    global transactions
    print(json.dumps(transactions, indent=2))

def update_transaction():
    global transactions
    category = input("Enter category to update: ")
    if category in transactions:
        print(f"Current transactions under {category}:")
        for index, expense in enumerate(transactions[category], start=1):
            print(f"{index}. Amount: {expense['amount']}, Date: {expense['date']}")
        choice = input("Enter transaction number to update: ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(transactions[category]):
                new_amount = float(input("Enter new amount: "))
                new_date = input("Enter new date (YYYY-MM-DD): ")
                transactions[category][choice-1] = {"amount": new_amount, "date": new_date}
                print("Transaction updated successfully.")
            else:
                print("Invalid transaction number.")
        else:
            print("Invalid input. Please enter a valid number.")
    else:
        print("Category not found.")

def delete_transaction():
    global transactions
    category = input("Enter category to delete: ")
    if category in transactions:
        print(f"Current transactions under {category}:")
        for index, expense in enumerate(transactions[category], start=1):
            print(f"{index}. Amount: {expense['amount']}, Date: {expense['date']}")
        choice = input("Enter transaction number to delete: ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(transactions[category]):
                del transactions[category][choice-1]
                print("Transaction deleted successfully.")
            else:
                print("Invalid transaction number.")
        else:
            print("Invalid input. Please enter a valid number.")
    else:
        print("Category not found.")

def display_summary():
    global transactions
    for category, expenses in transactions.items():
        total_amount = sum(expense['amount'] for expense in expenses)
        print(f"{category}: Total Amount - {total_amount}, Count - {len(expenses)}")

def main_menu():
    load_transactions()
    while True:
        print("\n===== Personal Finance Tracker =====")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Display Summary")
        print("6. Read Bulk Transactions from File")
        print("7. Save Transactions to File")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            update_transaction()
        elif choice == '4':
            delete_transaction()
        elif choice == '5':
            display_summary()
        elif choice == '6':
            filename = input("Enter filename to read transactions from: ")
            read_bulk_transactions_from_file(filename)
        elif choice == '7':
            save_transactions()
        elif choice == '8':
            save_transactions()
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main_menu()
