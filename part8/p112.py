import matplotlib.pyplot as plt
x = ["Dell","Toshiba","Lenovo","Apple"]
y = [34,55,12,90]
# plt.bar(x,y)
plt.scatter(x,y,marker="x")
# plt.barh(x,y,color="green")
plt.title("Sales Report")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.savefig("SalesReport.jpg")
plt.show()