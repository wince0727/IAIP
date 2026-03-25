import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

print("Columns:", df.columns)

df = df.dropna()
df = df.drop_duplicates()

df["Sale_Date"] = pd.to_datetime(df["Sale_Date"])

total_sales = df["Sales_Amount"].sum()
print("Total Sales:", total_sales)

top_products = (
    df.groupby("Product_ID")["Sales_Amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Products:\n", top_products)

df["Month"] = df["Sale_Date"].dt.month
monthly_sales = df.groupby("Month")["Sales_Amount"].sum()

print("\nMonthly Sales:\n", monthly_sales)

plt.figure(figsize=(8,5))
top_products.plot(kind="bar", color="skyblue")
plt.title("Top 10 Products by Sales")
plt.xlabel("Product ID")
plt.ylabel("Sales Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_products.png")
plt.close()

plt.figure(figsize=(8,5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales Amount")
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.close()

print("\n Charts saved successfully!")