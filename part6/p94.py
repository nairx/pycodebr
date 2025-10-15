import os
os.chdir("part6")
file_info = os.stat("temp.txt")
print(file_info)
print(file_info.st_size)

from datetime import datetime
st_ctime=1760429250
print(datetime.fromtimestamp(st_ctime))