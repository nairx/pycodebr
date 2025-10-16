import matplotlib.pyplot as plt
x = ["Dell","Toshiba","Lenovo","Apple"]
y = [34,55,12,90]
plt.pie(y,labels=x)
plt.title("Sales Report")
plt.savefig("SalesReport.jpg")
plt.show()