class employee:
    def greet(self):
        print("Hello World")
        
class manager(employee):
    def greet(self):
        print("Good Morning")

class staff(employee):
    def welcome(self):
        print("Welcome")

m=manager()
m.greet()

s=staff()
s.greet()
s.welcome()



