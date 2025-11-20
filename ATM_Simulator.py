print("Welcome to ATM-Simulator")
pin = 1234
balance = 1000
attempts = 0
while(attempts < 3):
    entered_pin = int(input("Enter your pin: "))
    if(entered_pin == pin):
        print("Choose the operation to perform")
        break;
    else:
        print("Wrong pin, enter your pin again")
        attempts = attempts + 1