# subjects = ["Maths","English","Science"]
# counter=0
# for i in subjects:
#     counter=counter+1
#     # print(str(counter)+"."+i)
#     print(f"{counter}.{i}")
    
subjects = ["Maths","English","Science"]
for i,j in enumerate(subjects,start=1):
    print(f"{i}.{j}")