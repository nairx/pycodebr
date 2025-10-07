username = input("Enter username")
# if username.isalnum() and len(username) >= 5 and len(username) <= 15 :
if username.isalnum() and  5 <=  len(username) <= 15 :
    print(f"Welcome {username}")
else:
    print("Invalid username")