#basic level ATM simulator program
print("Welcome to ATM-Simulator")
pin = 1234 #defining default pin
balance = 1000 # defining default balance
attempts = 0 # setting a counter for attempts
choice = 0 # initializing the choice to be 0 

# creating a function to check balance
def check_balance():
    print(balance)

# a function to deposit money
def deposit(a):
    global balance
    balance = balance + a
    print("Deposit Successful")
    return balance

# function to withdraw money 
def withdraw(a):
    global balance
    if(a<balance):
        balance = balance - a
        print("Withdraw Successful\nNew Balance is",balance)
    else:
        print("Insufficient Funds")

# function to change pin 
def change_pin(a):
    global pin
    pin = a
    print("Pin Successfully changed")

while(attempts < 3): # specifying the number of attempts a user can make
    entered_pin = int(input("Enter your pin: ")) # taking pin from the user as input 
    if(entered_pin == pin): # validating the pin 
        while (choice != 5): 
            # displaying the menu
            print("Choose the operation to perform")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Change PIN")
            print("5. Exit")
            choice = int(input("Enter your choice: ")) # taking user's choice
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

    else:
        attempts = attempts + 1
        if(attempts == 3):
            print("Account locked due to too many login attempts")
            break;
        print("Wrong pin, enter your pin again")  
        
