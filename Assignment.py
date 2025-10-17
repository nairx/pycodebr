# Analyze and visualize a company’s monthly sales data using NumPy, 
# Pandas, and Matplotlib.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Sales': [25000, 27000, 30000, 28000, 35000, 37000, 
              40000, 42000, 41000, 45000, 47000, 50000]
}

# Convert to DataFrame
df = pd.DataFrame(data)
print(df)

# Basic statistics
mean_sales = np.mean(df['Sales'])
max_sales = np.max(df['Sales'])
min_sales = np.min(df['Sales'])
std_dev = np.std(df['Sales'])

print(f"Average Monthly Sales: ₹{mean_sales:,.0f}")
print(f"Highest Sales: ₹{max_sales:,.0f}")
print(f"Lowest Sales: ₹{min_sales:,.0f}")
print(f"Standard Deviation: ₹{std_dev:,.0f}")

# Identify best and worst months
best_month = df.loc[df['Sales'].idxmax(), 'Month']
worst_month = df.loc[df['Sales'].idxmin(), 'Month']

print(f"Best Month: {best_month}")
print(f"Worst Month: {worst_month}")

plt.figure(figsize=(10, 5))
plt.plot(df['Month'], df['Sales'], marker='o', linestyle='-', linewidth=2)
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales (₹)')
plt.grid(True)
plt.show()


