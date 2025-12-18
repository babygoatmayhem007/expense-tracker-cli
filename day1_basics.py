name = input("What's your name? ")

expenses = []

while True:
    print("\nMenu:")
    print("1. Add an expense")
    print("2. View total expenses")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        while True:
            try:
                amount = float(input("Enter expense amount: "))
                expenses.append(amount)
                print(f"Added {amount} to your expenses.")
                break
            except ValueError:
                print("Please enter a valid number.")
    elif choice == "2":
        total = sum(expenses)
        print(f"Total expenses so far: {total}")
    elif choice == "3":
        print("Exiting program...")
        print(f"Summary for {name}: Total expenses = {sum(expenses)}")
        break
    else:
        print("Invalid choice, please select 1, 2, or 3.")
