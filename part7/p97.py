import os
os.chdir("part7")
f=open("temp.txt","a")
while True:
    n = input("Enter name: ")
    f.write(n+"\n")
    ch= input("Continue?(y/n)")
    if ch != "y":
        break
f.close()

