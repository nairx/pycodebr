#Create a folder Quiz
#Questions1.txt, Questions2.txt,....,Questions5.txt
#Each Question paper will have 10 random questions
#for example 
# Math Quiz
# Q1. 10 + 5 = 
# Q2. 12 x 3 = 
import random,os
if not os.path.exists("quiz"):
    os.mkdir("quiz")
os.chdir("quiz")
op=['+',"x","-","/"]
for i in range(1,6):
    if not os.path.isfile(f"Question{i}.txt"):
        f=open(f"Question{i}.txt","w")
        f.write("***Math Quiz***\n")
        for j in range(1,11):
            n1=random.randint(10,99)
            n2=random.randint(1,9)
            f.write(f"Q{j}.{n1}{random.choice(op)}{n2}=\n")
        f.close()
        

