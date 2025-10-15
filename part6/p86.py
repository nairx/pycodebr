class employee:
    def greet(self,name=None,age=None):
        if name and age:
            print(f"Name:{name},Age:{age}")
        elif name:
            print(f"Name:{name}")
        else:
            print("Hello")
        
e = employee()
e.greet()
e.greet("Amy")
e.greet("Amy",23)
