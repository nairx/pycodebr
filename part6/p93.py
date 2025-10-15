import os
from datetime import datetime
if not os.path.exists("backup"):
    os.mkdir("backup")
os.chdir("backup")
dt = datetime.now()
folder = dt.strftime("%Y%m%d%H%M%S")
os.mkdir(folder)
os.chdir(folder)
open("file1.txt","w")
os.chdir("..")
