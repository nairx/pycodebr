import matplotlib.pyplot as plt
x = ["Dell","Toshiba","Lenovo","Apple"]
y = [34,55,12,90]
z = [20,35,20,70]
plt.title("Sales Report")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.stackplot(x,y,z)
plt.savefig("SalesReport.jpg")
plt.show()