# def gen():
#     for i in range(100):
#         yield i
# result = gen()
# for i in result:
#     print(i)
  
# t = (4,6,7,8,4)  
# print(type(t)) #will print tuple

# g1 = (x for x in range(100))
# print(type(g1)) #will print generator

# g2 = (x for x in range(2))
# print(next(g2))
# print(next(g2))
# print(next(g2)) #will throw an error

# list1 = [4,6,7,8,9,1,2,3]
# g1 = iter(list1)
# print(type(list1))
# print(type(g1))

import sys
list1 = [x for x in range(100000)]
g1 = (x for x in range(100000))
print(sys.getsizeof(list1,"Bytes"))
print(sys.getsizeof(g1,"Bytes"))
