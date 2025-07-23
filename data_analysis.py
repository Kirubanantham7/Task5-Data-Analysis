import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('sales_data.csv')

# Preview data
print(df.head())

# Summary stats
print(df.info())
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Total Revenue by Region
region_sales = df.groupby('Region')['Revenue'].sum().reset_index()
print(region_sales)

# Plot
plt.figure(figsize=(8, 5))
sns.barplot(data=region_sales, x='Region', y='Revenue', hue='Region', palette='viridis', legend=False)
plt.title('Total Revenue by Region')
plt.xlabel('Region')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Total Quantity Sold by Product
product_quantity = df.groupby('Product')['Quantity'].sum().reset_index()

# Plot
plt.figure(figsize=(8, 5))
sns.barplot(data=product_quantity, x='Product', y='Quantity', hue='Product', palette='magma', legend=False)
plt.title('Total Quantity Sold by Product')
plt.xlabel('Product')
plt.ylabel('Quantity Sold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Monthly Sales Trend
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M').astype(str)

monthly_sales = df.groupby('Month')['Revenue'].sum().reset_index()
monthly_sales['Revenue'] = pd.to_numeric(monthly_sales['Revenue'], errors='coerce')

# Plot
plt.figure(figsize=(10, 6))
sns.lineplot(data=monthly_sales, x='Month', y='Revenue', marker='o')
plt.title('Monthly Sales Revenue Trend')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
