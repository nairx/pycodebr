customer = {"name":"Suman","city":"Hyderabad"}
# print(customer["age"])
# print(customer.get("age"))
# print(customer.get("age",0))
print(customer)
customer["name"] = "Pramod"
print(customer)
customer["state"] = "Telangana"
print(customer)
customer["score"] = customer.get("score",0) + 1
print(customer)
del customer["city"]
print(customer)
