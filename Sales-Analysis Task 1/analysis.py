import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_data.csv")

# Show columns (for safety)
print("Columns:", df.columns)

# Clean data
df = df.dropna()
df = df.drop_duplicates()

# Convert Date
df["Sale_Date"] = pd.to_datetime(df["Sale_Date"])

# Total Sales
total_sales = df["Sales_Amount"].sum()
print("Total Sales:", total_sales)

# Top Products (Top 10 only for clean chart)
top_products = (
    df.groupby("Product_ID")["Sales_Amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Products:\n", top_products)

# Monthly Sales
df["Month"] = df["Sale_Date"].dt.month
monthly_sales = df.groupby("Month")["Sales_Amount"].sum()

print("\nMonthly Sales:\n", monthly_sales)

# 📊 Save Product Chart
plt.figure(figsize=(8,5))
top_products.plot(kind="bar", color="skyblue")
plt.title("Top 10 Products by Sales")
plt.xlabel("Product ID")
plt.ylabel("Sales Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_products.png")
plt.close()

# 📈 Save Monthly Chart
plt.figure(figsize=(8,5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales Amount")
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.close()

print("\n✅ Charts saved successfully!")