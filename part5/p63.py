def f2(f):
    def wrapper():
        print("f1 function begins")
        f()
        print("f1 function ends")
    return wrapper

@f2
def f1():
    print("I am f1 function")

f1()




