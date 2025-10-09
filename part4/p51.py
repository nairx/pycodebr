print("***HDFC Bank ATM***")
customer={
    "card":"1234567890",
    "pin":"1234",
    "name":"John",
    "balance":1000
}
cardnum = input("Enter Card Number: ")
pinnumber=input("Enter pin: ")
if cardnum==customer["card"] and pinnumber==customer["pin"]:
    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance")
        print("4. Exit")
        ch=input("Enter choice: ")
        if ch=="1":
            amount=int(input("Enter amount: "))
            customer["balance"] = customer["balance"]+amount
        elif ch=="2":
            amount=int(input("Enter amount: "))
            if customer["balance"]<amount:
                print("Insufficient Balance")
            else:
                customer["balance"] = customer["balance"]-amount
        elif ch=="3":
            print(f"Balance is: {customer["balance"]}")
        else:
            break
else:
    print("Invalid credentials")
        
    
    