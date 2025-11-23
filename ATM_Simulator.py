print("Welcome to ATM-Simulator")
pin = 1234
balance = 1000
attempts = 0
while(attempts < 3):
    entered_pin = int(input("Enter your pin: "))
    if(entered_pin == pin):
        print("Choose the operation to perform")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("Your balance is",balance)
        break;
        if choice == 2:
            deposit_amount = int(input("Enter the amount to deposit: "))  
            deposit(deposit_amount) 
    else:
        attempts = attempts + 1
        if(attempts == 3):
            print("Account locked due to too many login attempts")
            break;
        print("Wrong pin, enter your pin again")  


def deposit(a):
    balance = balance + a