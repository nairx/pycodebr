import threading
from time import sleep
def cube(a):
    for i in range(3):
        sleep(2)
        print(f"Cube of {a} is {a*a*a}")

def square(a):
    for i in range(3):
        sleep(3)
        print(f"Square of {a} is {a*a}")
t1=threading.Thread(target=cube,args=(2,))
t2=threading.Thread(target=square,args=(3,))
t1.start()
t2.start()
t1.join()
t2.join()
print("Program Completed")