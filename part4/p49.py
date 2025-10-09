#Accept two numbers and print sum and product using functions

def add(a,b):
    return a+b

def product(a,b):
    return a*b

def main():
    x = int(input("Enter a value: "))
    y = int(input("Enter a value: "))
    c=add(x,y)
    print(c)
    d=product(x,y)
    print(d)

main()
    

