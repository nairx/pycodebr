"""
1. create a folder part7 under pycodebr if does not exist
2. change to part7
3. create a file file1.txt inside part7 if does not exist
4. list the directory of part7
5. rename file1.txt to file2.txt
6. list the directory of part7
7. remove file2.txt
8. change directory to pycodebr
9. remove directory part7
10. list directory of pycodebr
"""
import os
if not os.path.exists("part7"):
    os.mkdir("part7")
print(os.listdir())
os.chdir("part7")
print(os.listdir())
if not os.path.isfile("file1.txt"):
    open("file1.txt","w")
print(os.listdir())
os.rename("file1.txt","file2.txt")
print(os.listdir())
os.remove("file2.txt")
print(os.listdir())
os.chdir("..")
print(os.listdir())
os.rmdir("part7")
print(os.listdir())




from datetime import datetime
import os
d = datetime.now()
dd = d.strftime("%Y%m%d%H%M%S")
os.chdir("backup")
os.mkdir(dd)