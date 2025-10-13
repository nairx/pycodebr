from datetime import datetime
dt = datetime.now()
print(dt)
t = dt.timestamp()
print(t)

# d = datetime.fromtimestamp(t)
# print(d)

tstamp = 1660339710
d = datetime.fromtimestamp(tstamp)
print(d)
