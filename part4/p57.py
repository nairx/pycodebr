# result = [True,False,True,True]
# for i in result:
#     if i!=True:
#         print("Fail")
#         break
# else:
#     print("Pass")

# result = [False,False,False,False]
# for i in result:
#     if i==True:
#         print("Pass")
#         break
# else:
#     print("Fail")
    
# result = [True,True,True,True]
# if all(result):
#     print("Pass")
# else:
#     print("Fail")
    
# result = [True,False,True,True]
# if any(result):
#     print("Pass")
# else:
#     print("Fail")
    

marks = [45,20,60,80]
result = [i>30 for i in marks]
if all(result):
    print("Pass")
else:
    print("Fail")

marks = [45,20,60,80]
result = {i:i>30 for i in marks}
print(result)
if all(result.values()):
    print("Pass")
else:
    print("Fail")
