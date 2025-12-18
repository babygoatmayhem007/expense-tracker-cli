def add_expense(expenses):
     while True:
          try:
               amount = float(input("Enter expense amount:"))
               expenses.append(amount)
               with open("expenses.txt","a")as file:
                    file.write(f"{amount}\n")
                    print(f"Added {amount} to yor expenses")
                    break 
          except ValueError:
               print("Invalid input.Please enter a valid number")



def view_total(expenses):
     total= sum(expenses)
     print(f"Total expenses so far is {total}")

                        




def load_expenses():
    expenses=[]
    cleaned_lines = []

    try: 
        with open("expenses.text","r")as file:
            for line in file:
                try:
                  value=float(line.strip())
                  expenses.append(value)
                  cleaned_lines.append(f"{value}\n")

                except ValueError:  
                    pass
     
    except FileNotFoundError:
        pass
    with open("expenses.txt","w")as file:
        file.writelines(cleaned_lines)
    return expenses



while True:
 name = input("Enter Your Name:").strip()
 if name:
    break
 print("Name cannot be empty")


expenses=load_expenses()

while True:
         
         print("\nmenu")
         print("1.Add expenses")
         print("2.View expenses")
         print("3.Exit") 
         
         choice  = input("Enter your option (1-3):")

         if choice == "1":
             add_expense(expenses)
        
         elif choice == "2":
             view_total(expenses)

         elif choice =="3":
             print("Exiting program....")
             print(f"Summary for {name}: Total expenses = {sum(expenses)}")
             break
         else:
             print("Invalid choice. Please select a valid option")
            




