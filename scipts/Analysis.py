'''
🎯 Goal: Extract Insights
Questions to Answer:
Top-selling products?
Revenue by city?
Monthly sales trend?

👉 Create:
Bar chart → Top products
Line chart → Monthly sales
Pie chart → Category share
'''

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales_cleaned.csv')
'''
plt.figure(figsize=(6,6)): new canvas, size 6x6 inches
plt.bar(top_product.index, top_product.values): bar chart with product names on x-axis and revenue on y-axis
plt.title(): set title of the plot
plt.xlabel(): label for x-axis
plt.ylabel(): label for y-axis
plt.xticks(rotation=45): rotate x-axis labels by 45 degrees for better readability
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.6): add grid lines with dashed style, thin width, and light transparency
plt.gca().set_axisbelow(True): ensure grid lines are behind the bars
plt.tight_layout(): adjust layout to prevent overlap
plt.show(): display the plot
plt.pie(best_city.values, labels = best_city.index, autopct='%1.1f%%'): create a pie chart with city names as labels and revenue values, showing percentage with one decimal place
plt.plot(monthly_trend.index, monthly_trend.values, color='blue', linestyle='--', marker='o'): line plot with month on x-axis and revenue on y-axis, blue dashed line with circle markers
'''

# 1. Top selling products
top_product = df.groupby('Product')['Revenue'].sum().sort_values(ascending = False).head()
print("Top Selling Products:\n",top_product)
plt.figure(figsize=(6,6))
plt.bar(top_product.index, top_product.values)
plt.title("Top Selling Products")
plt.xlabel('Product')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.6)
plt.gca().set_axisbelow(True)
plt.tight_layout()
plt.show()

# 2. Best performing cities
best_city = df.groupby('City')['Revenue'].sum().sort_values(ascending = False).head()
print("\nBest Performing Cities:\n",best_city)
plt.figure(figsize=(6,6))
plt.pie(best_city.values, labels = best_city.index, autopct='%1.1f%%')
plt.title("Best Performing Cities")
plt.tight_layout()
plt.show()


# 3. Monthly sales trends
monthly_trend = df.groupby('Month')['Revenue'].sum().sort_index()
print("\nMonthly Sales Trends:\n",monthly_trend)
plt.figure(figsize=(6,6))
plt.plot(monthly_trend.index, monthly_trend.values, color='blue', linestyle='--', marker='o')
plt.title("Monthly Sales Trends")
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.6)
plt.gca().set_axisbelow(True)
plt.tight_layout()
plt.show()

# 4. Category share
category_share = df.groupby('Category')['Revenue'].sum()
print("\nCategory Share:\n",category_share)
plt.figure(figsize=(6,6))
plt.pie(category_share.values, labels=category_share.index, autopct='%1.1f%%')
plt.title("Category Share")
plt.tight_layout()
plt.show()

'''
5. Additional Questions:
Which city buys most electronics?
Which category sells highest quantity?
Which month generated highest revenue?
'''
electronics_city = df[df['Category'].str.lower() == 'electronics'].groupby('City')['Revenue'].sum().sort_values(ascending = False).head(1)
category_qty = df.groupby('Category')['Quantity'].sum().sort_values(ascending = False).head(1)
month_revenue = df.groupby(['Month','Month_Name'])['Revenue'].sum().sort_values(ascending = False).head(1)

print("\nAdditional Insights:")
print(f"City with highest Electronics revenue: {electronics_city.index[0].capitalize()}")
print(f"Category with highest quantity sold: {category_qty.index[0]}")
print(f"Month with highest revenue: {month_revenue.index[0][1]}")

# 6. Final insights
print("\nFinal Business Insights: ")
print(f"👉 {top_product.index[0]} drives the highest revenue - prioritize inventory and promotions.")
print(f"👉 {best_city.index[0].capitalize()} is the strongest market - expansion opportunities exist here.")
print(f"👉 Peak sales occur in Month {monthly_trend.idxmax()} with revenue of {monthly_trend.max()} - indicates seasonal demand patterns.")
print(f"👉 {category_share.idxmax()} category contributes the most to total revenue.")