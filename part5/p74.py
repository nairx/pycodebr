from datetime import datetime
# d = datetime.now()
# print(d)
# # print(d.strftime("%B %d %y"))
# # print(d.strftime("%B %d %Y"))
# # print(d.strftime("%B %d %Y %H:%M:%S"))
# print(d.strftime("%B, %d %Y %I%p"))

date_str = "2025-10-10 14:30:00"
dt_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(dt_obj)
