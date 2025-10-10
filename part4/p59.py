subjects = ["Maths","English","Science"]
marks=[40,70,20]

# result = []
# for i in range(len(subjects)):
#     t = (subjects[i],marks[i])
#     result.append(t)
# print(result)

result = zip(subjects,marks)
print(list(result))

for i,j in zip(subjects,marks):
    if i!="English":
        print(i,j)