print("***HDFC Bank ATM***")
customer={
    "card":"1234567890",
    "pin":"1234",
    "name":"John",
    "balance":1000
}

def menu():
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance")
    print("4. Exit")
    
def deposit():
    amount=int(input("Enter amount: "))
    customer["balance"] = customer["balance"]+amount
    
def withdraw():
    amount=int(input("Enter amount: "))
    if customer["balance"]<amount:
        print("Insufficient Balance")
    else:
        customer["balance"] = customer["balance"]-amount
    
def balance():
    print(f"Balance is: {customer['balance']}")

def main():
    cardnum = input("Enter Card Number: ")
    pinnumber=input("Enter pin: ")
    if cardnum==customer["card"] and pinnumber==customer["pin"]:
        while True:
            menu()
            ch=input("Enter choice: ")
            if ch=="1":
                deposit()
            elif ch=="2":
                withdraw()
            elif ch=="3":
                balance()
            else:
                break
    else:
        print("Invalid credentials")
        
main()
    
    