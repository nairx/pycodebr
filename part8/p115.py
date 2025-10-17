from collections import Counter
EmpLocation = ["Hyderabad","Bengaluru","Hyderabad","Delhi","Bengaluru","Hyderabad"]
mycounter = Counter(EmpLocation)
print(mycounter.most_common(2))