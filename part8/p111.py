import matplotlib.pyplot as plt
x = ["Dell","Toshiba","Lenovo","Apple"]
y = [34,55,12,90]
z = [20,35,20,70]
plt.plot(x,y,color="blue",marker="o",linestyle="--",label="Year 2025")
plt.plot(x,z,color="green",marker="o",linestyle="--",label="Year 2024")
plt.title("Sales Report")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.legend()
plt.savefig("SalesReport.jpg")
plt.show()