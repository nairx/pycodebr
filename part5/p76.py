from datetime import datetime,timezone,timedelta
dt = datetime.utcnow()
print(dt)
ist = timezone(timedelta(hours=5,minutes=30))
ist_time = dt.now(ist)
print(ist_time)
frankfurt_time = timezone(timedelta(hours=2))
print(dt.now(frankfurt_time))