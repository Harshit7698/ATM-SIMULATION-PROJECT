balance = 10000
pin = 1234

print("WELCOME TO ATM")

user_pin = int(input("Enter your PIN: "))

if user_pin == pin:
    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Your balance is:", balance)

        elif choice == 2:
            amount = int(input("Enter amount to deposit: "))
            balance += amount
            print("Amount deposited successfully")

        elif choice == 3:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print("Please collect your cash")
            else:
                print("Insufficient balance")

        elif choice == 4:
            print("Thank you for using ATM")
            break

        else:
            print("Invalid choice")

else:
    print("Incorrect PIN")