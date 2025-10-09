list1 = []
list2 = []
for i in range(5):
    value = int(input("Enter a number"))
    list1.append(value)
    if value not in list2:
        list2.append(value)
print(list1)
print(list2)