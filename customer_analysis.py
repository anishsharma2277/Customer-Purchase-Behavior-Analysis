# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv('supermarket_sales.csv')  # Make sure this file name matches your dataset file

# Data Cleaning
data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%Y')
data.drop_duplicates(inplace=True)

# Example Analysis: Top Products Sold
top_products = data['Product line'].value_counts()
top_products.plot(kind='bar', color='skyblue', title='Top Selling Product Lines')
plt.xlabel('Product Line')
plt.ylabel('Number of Sales')
plt.show()

# Example Analysis: Revenue by Product Line
category_revenue = data.groupby('Product line')['Total'].sum().sort_values(ascending=False)
category_revenue.plot(kind='bar', color='salmon', title='Revenue by Product Line')
plt.xlabel('Product Line')
plt.ylabel('Total Revenue')
plt.show()

# Example Analysis: Monthly Sales Trends
data['Month'] = data['Date'].dt.month
monthly_sales = data.groupby('Month')['Total'].sum()
monthly_sales.plot(kind='line', marker='o', color='green', title='Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.show()
