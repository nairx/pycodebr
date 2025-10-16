import os
os.chdir("quiz")
file = open("Question1.txt","r")
for line in file:
    print(line)
file.close()
