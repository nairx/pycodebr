names = {"Lahari","Ritesh","Ritesh","Gopinath"}
print(names)
# print(names[0])
names.add("Gautham")
names.remove("Ritesh")
for i in names:
    print(i)
    
numbers = [5,3,2,5,3]
# new = set(numbers)
new = frozenset(numbers)
print(new)
new.add(9)
print(new)