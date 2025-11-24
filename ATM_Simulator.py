print("Welcome to ATM-Simulator")
pin = 1234
balance = 1000
attempts = 0
choice = 0
def check_balance():
    print(balance)

def deposit(a):
    global balance
    balance = balance + a
    return balance

def withdraw(a):
    global balance
    if(a<balance):
        balance = balance - a
        print("Withdraw Successful\nNew Balance is",balance)
    else:
        print("Insufficient Funds")

def change_pin(a):
    global pin
    pin = a
    print("Pin Successfully changed")

while(attempts < 3):
    entered_pin = int(input("Enter your pin: "))
    if(entered_pin == pin):
        while (choice != 5):
            print("Choose the operation to perform")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Change PIN")
            print("5. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                check_balance()
            elif choice == 2:
                deposit_amount = int(input("Enter the amount to deposit: "))  
                deposit(deposit_amount)
            elif choice == 3:
                withdraw_amount = int(input("Enter the amount to withdraw: "))
                withdraw(withdraw_amount)
            elif choice == 4:
                current_pin = int(input("Enter your current pin: "))
                if(current_pin==pin):
                    new_pin = int(input("Enter the new pin: "))
                    change_pin(new_pin)
                else:
                    print("Incorrect Pin Entered")
            elif choice == 5:
                break
            break
        break

    else:
        attempts = attempts + 1
        if(attempts == 3):
            print("Account locked due to too many login attempts")
            break;
        print("Wrong pin, enter your pin again")  
