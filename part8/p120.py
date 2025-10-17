from collections import UserList

class MyList(UserList):
    def pop(self,s=None):
        raise Exception("Pop method is not allowed")
        return
    
users = MyList(["Gowtham","Sainath"])
print(users)
users.pop()
print(users)


# users = ["Gowtham","Sainath"]
# users.pop()
# print(users)

