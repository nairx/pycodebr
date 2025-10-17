from collections import ChainMap
d1 = {'a':4,'b':6}
d2 = {'c':7,'d':9}
d3 = {'e':7,'f':9}
d4 = {'g':7,'h':9}

d = ChainMap(d1,d2,d3,d4)
# print(d['f'])
for key,value in d.items():
    print(key,value)




