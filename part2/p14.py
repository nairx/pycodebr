name = "Hello Ritesh"
print(name[1])
print(name[-1])
print(name[1:5])
print(name[:5])
print(name[5:])
print(name[::-1])
print(name[::2])
print(name[:9:2])

str = "hello"
str1 = str[::-1]
if str==str1:
    print("Pallidrone")
else:
    print("NA")

for i in name:
    print(i)
    
result = 'H' in name
print(result)

result = 'x' not in name
print(result)
