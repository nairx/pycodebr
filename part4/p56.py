# list1 = [1,1,2,3,4,5]
# list2 = []
# for i in list1:
#     list2.append(i+2)
# print(list2)

# list2 = [i+2 for i in list1]
# print(list2)

# list2 = [i+2 for i in list1 if i<4]
# print(list2)

# set2 = {i+2 for i in list1 if i<4}
# print(set2)

# employees={}
# for i in range(1,6):
#     employees[f"emp{i}"]=1000+i
# print(employees)


employees={f"emp{i}":1000+i for i in range(1,5)}
print(employees)




