# d1 = {
#     12:20,
#     10:30,
#     15:10
# }
# print(max(d1))
# print(sum(d1))

d1 = {
    "Sohan":20,
    "Lahari":30,
    "Aishwarya":10
}
print(max(d1,key=d1.get))
print(min(d1,key=d1.get))

print(sum(d1.values()))
print(min(d1.values()))