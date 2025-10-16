import matplotlib.pyplot as plt
x = ["Dell","Toshiba","Lenovo","Apple"]
y = [34,55,12,90]
plt.plot(x,y)
plt.title("Sales Report")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.savefig("SalesReport.jpg")
plt.show()