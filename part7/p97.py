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
# with open("temp.txt") as file:
#     for line in file:
#         print(line)

# file = open("temp.txt","r")
# data = file.read()
# print(data)
# file.close()

file = open("temp.txt","r")
for line in file:
    print(line)
file.close()


