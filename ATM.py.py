# ATM Management System

balance = 10000

pin = "1234"

def check_balance():

    print("Current Balance:", balance)

def deposit():

    global balance

    amount = float(input("Enter deposit amount: "))

    if amount > 0:

        balance += amount

        print("Amount deposited successfully.")

        print("New Balance:", balance)

    else:

        print("Invalid amount.")

def withdraw():

    global balance

    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:

        print("Invalid amount.")

    elif amount > balance:

        print("Insufficient balance.")

    else:

        balance -= amount

        print("Please collect your cash.")

        print("Remaining Balance:", balance)

def change_pin():

    global pin

    old_pin = input("Enter current PIN: ")

    if old_pin == pin:

        new_pin = input("Enter new PIN: ")

        if len(new_pin) == 4 and new_pin.isdigit():

            pin = new_pin

            print("PIN changed successfully.")

        else:

            print("PIN must contain exactly 4 digits.")

    else:

        print("Incorrect PIN.")

# PIN Verification

entered_pin = input("Enter your PIN: ")

if entered_pin == pin:

    while True:

        print("\n===== ATM MENU =====")

        print("1. Balance Enquiry")

        print("2. Deposit")

        print("3. Withdrawal")

        print("4. Change PIN")

        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            check_balance()

        elif choice == "2":

            deposit()

        elif choice == "3":

            withdraw()

        elif choice == "4":

            change_pin()

        elif choice == "5":

            print("Thank you for using the ATM.")

            break

        else:

            print("Invalid choice.")

else:

    print("Incorrect PIN. Access Denied.")