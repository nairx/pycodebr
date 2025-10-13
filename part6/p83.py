class calc:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("This is a constructor")
    def add(self):
        print(f"Sum is {self.a+self.b}")
    def multiply(self):
        print(f"Product is {self.a*self.b}")

c = calc(4,5)
c.add()
c.multiply()