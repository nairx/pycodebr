#Accept name and increment point
names={}
while True:
    name = input("Enter name: ")
    names[name]=names.get(name,0)+1
    flag = input("Do you want to continue(y/n)?")
    if flag.lower()!="y":
        break
print(names)
    
    