# def calc(x):
#     return x+2
# list1 = [20,23,28]
# list2 = map(calc,list1)
# print(list(list2))


# def calc(x):
#     return x>20
# list1 = [20,23,28]
# list2 = filter(calc,list1)
# print(list(list2))


from functools import reduce
def calc(x,y):
        return x+y
list1 = [2,3,4]
total = reduce(calc,list1)
print(total)

