from datetime import datetime,date,timedelta
d = date.today()
print(d)
d1 = d + timedelta(days=1)
print(d1)
d2 = d - timedelta(days=1)
print(d2)
d3 = d + timedelta(minutes=1)
print(d3)
t1 = datetime.now()
t2 = datetime(2025,10,13,10,10,10)
t = t1 - t2
print(t.days)
print(t.seconds)
