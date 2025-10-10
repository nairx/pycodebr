def f2(f):
    def wrapper(role):
        f(role)
        if role=="VP":
            print("Bonus is 20%")
        else:
            print("Bonus is 10%")
    return wrapper
               
@f2
def f1(role):
    print(f"Hello {role}")
    
f1("AVP")
