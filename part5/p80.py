# try:
#     print(a)
# except:
#     print("Something went wrong")
# else:
#     print("Program completed successfully")

try:
    a = "Hello"
    print(a/2)
except NameError:
    print("Name Error")
except TypeError:
    print("The type of the variable is incorrect")
except:
    print("Something went wrong")
else:
    print("Program completed successfully")