def add_expense(expenses):
    try:
        amount = float(input("Enter the expense amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a positive number.")
        
        category = input("Enter the expense category (e.g., food, transportation, entertainment, rent, utilities, medical, education, shopping, other, or any other category): ").strip().lower()
        description = input("Enter a short description of the expense: ").strip()

        expense = {'amount': amount, 'category': category, 'description': description}
        expenses.append(expense)
        print("Expense added successfully!")
    
    except ValueError as ve:
        print(f"Error: {ve}")

def display_summary(expenses):
    if not expenses:
        print("\nNo expenses recorded yet.")
        return
    
    summary = {}
    
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        
        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount
    
    print("\nExpense Summary:")
    for category, total in summary.items():
        print(f"{category.capitalize()}: Rs.{total:.2f}")

def main():
    expenses = []
    
    while True:
        print("\n1. Add an expense")
        print("2. View expense summary")
        print("3. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            display_summary(expenses)
        elif choice == '3':
            print("Exiting the expense tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()