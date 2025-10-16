from time import sleep
import threading
def f1():
    for i in range(3):
        sleep(2)
        print("This is function f1")

def f2():
    for i in range(3):
        sleep(3)
        print("This is function f2")
t1 = threading.Thread(target=f1)
t2 = threading.Thread(target=f2)
t1.start()
t2.start()
t1.join()
t2.join()
print("Main program")