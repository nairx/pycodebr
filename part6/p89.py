class employee:
    def __init__(self,name):
        self.__name = name
    def setname(self,name):
        self.__name = name
    def getname(self):
        return self.__name
    
e=employee("John")
# print(e.__name)
print(e.getname())
e.setname("Cathy")
print(e.getname())