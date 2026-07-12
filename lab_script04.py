# Lab Setup: create sample CSV, Excel, and JSON files
import pandas as pd
 
# customers.csv
customers = pd.DataFrame([
    {"customer_id": 1, "name": "Asha Kapoor", "city": "Pune", "loyalty_points": 120},
    {"customer_id": 2, "name": "Rahul Mehta", "city": "Mumbai", "loyalty_points": 80},
    {"customer_id": 3, "name": "Sita Rao", "city": "Bengaluru", "loyalty_points": None},
    {"customer_id": 4, "name": "John Doe", "city": "Pune", "loyalty_points": 200},
    {"customer_id": 5, "name": "Priya Singh", "city": None, "loyalty_points": 50},
])
customers.to_csv("customers.csv", index=False)
 
# orders.csv
orders = pd.DataFrame([
    {"order_id": 101, "customer_id": 1, "product": "Keyboard", "amount": 1200.0, "order_date": "2024-05-01"},
    {"order_id": 102, "customer_id": 2, "product": "Mouse", "amount": 350.5, "order_date": "2024-05-02"},
    {"order_id": 103, "customer_id": 1, "product": "Monitor", "amount": 8000.0, "order_date": "2024-05-02"},
    {"order_id": 104, "customer_id": 3, "product": "Laptop", "amount": 55000.0, "order_date": "2024-05-03"},
    {"order_id": 105, "customer_id": 2, "product": "Webcam", "amount": 1500.0, "order_date": "2024-05-04"},
    {"order_id": 106, "customer_id": 5, "product": "Headset", "amount": 900.0, "order_date": "2024-05-05"},
])
orders.to_csv("orders.csv", index=False)
 
# products.json
products = [
    {"product_id": "P01", "product_name": "Keyboard", "category": "Accessories"},
    {"product_id": "P02", "product_name": "Mouse", "category": "Accessories"},
    {"product_id": "P03", "product_name": "Monitor", "category": "Displays"},
]
import json
with open("products.json", "w") as f:
    json.dump(products, f, indent=2)
 
# Save an Excel file (orders with additional sheet)
with pd.ExcelWriter("orders.xlsx") as writer:
    orders.to_excel(writer, sheet_name="orders", index=False)
    customers.to_excel(writer, sheet_name="customers", index=False)


    print("Setup complete.")
print("customers.csv created")
print("orders.csv created")
print("products.json created")
print("orders.xlsx created")


# 1. Series vs DataFrame

# Read the customers CSV file into a DataFrame.
df_customers = pd.read_csv("customers.csv")

# Select one column.
# One selected column becomes a pandas Series.
loyalty_points = df_customers["loyalty_points"]

print("Series:")
print(loyalty_points)

print()

# shape shows:
# number of rows, number of columns.
print("DataFrame shape:", df_customers.shape)

# 2. Create DataFrame from Dictionary

# Create a small products table from a Python dictionary.
products_df = pd.DataFrame({
    "product_id": ["P10", "P11", "P12"],
    "product_name": ["USB Cable", "Charger", "Power Bank"],
    "price": [250.0, 799.0, 1299.5]
})

print("\nLab 2 - Products DataFrame:")
print(products_df)

# 3. Read CSV File

# Read the orders CSV file into a DataFrame.
df_orders = pd.read_csv("orders.csv")

# head() shows the first five rows.
print("\nLab 3 - First 5 rows of orders:")
print(df_orders.head())

# 4. Read Excel File

# Read the "orders" sheet from the Excel file.
df_excel_orders = pd.read_excel(
    "orders.xlsx",
    sheet_name="orders"
)

# Show the number of rows and columns.
print("\nLab 4 - Excel shape:")
print(df_excel_orders.shape)

# iloc[0] selects the first row by position.
print("\nFirst row:")
print(df_excel_orders.iloc[0])

# 5. Read JSON File

# Read the products JSON file into a DataFrame.
df_products = pd.read_json("products.json")

# Select and print only the product_name column.
print("\nLab 5 - Product names:")
print(df_products["product_name"])

# 6. Inspect Data

# Read the customers CSV file.
df_customers = pd.read_csv("customers.csv")

# Show the first five rows.
print("\nLab 6 - First rows:")
print(df_customers.head())

# Show the last five rows.
print("\nLast rows:")
print(df_customers.tail())

# Show number of rows and columns.
print("\nShape:")
print(df_customers.shape)

# Show column names, data types, and non-null counts.
print("\nInfo:")
df_customers.info()

# Show numeric summary statistics.
print("\nDescription:")
print(df_customers.describe())

# 7. Select Columns

# Read the orders CSV file.
df_orders = pd.read_csv("orders.csv")

# Double brackets select multiple columns
# and return a new DataFrame.
selected_columns = df_orders[
    ["order_id", "amount"]
]

print("\nLab 7 - Selected columns:")
print(selected_columns)

# 8. Filter Rows

# Read the orders CSV file.
df_orders = pd.read_csv("orders.csv")

# Keep only rows where the amount is greater than 1000.
filtered_orders = df_orders[
    df_orders["amount"] > 1000
]

# Show only the required columns.
filtered_orders = filtered_orders[
    ["order_id", "customer_id", "amount"]
]

print("\nLab 8 - Orders above 1000:")
print(filtered_orders)


# 9. Handle Missing Values

# Read the customers CSV file.
df_customers = pd.read_csv("customers.csv")

# Find rows where the city value is missing.
missing_city_rows = df_customers[
    df_customers["city"].isnull()
]

print("\nLab 9 - Rows with missing city:")
print(missing_city_rows)

# Calculate the average loyalty points.
# mean() ignores missing values automatically.
mean_loyalty_points = df_customers["loyalty_points"].mean()

print("\nMean loyalty points:")
print(mean_loyalty_points)

# Replace the missing loyalty_points value with the average.
df_customers["loyalty_points"] = (
    df_customers["loyalty_points"]
    .fillna(mean_loyalty_points)
)

print("\nAfter filling missing loyalty points:")
print(df_customers)

# Remove rows where the name is missing.
# In this dataset, no names are missing.
final_customers = df_customers.dropna(
    subset=["name"]
)

print("\nAfter dropping rows with missing names:")
print(final_customers)

# 10. Rename Columns

# Read the orders CSV file.
df_orders = pd.read_csv("orders.csv")

# Rename the requested columns.
df_renamed = df_orders.rename(columns={
    "order_id": "id",
    "customer_id": "cust_id",
    "order_date": "date"
})

print("\nLab 10 - First row with renamed columns:")
print(df_renamed.iloc[0])

# 11. Create a Derived Column

# Read the orders CSV file.
df_orders = pd.read_csv("orders.csv")

# Create a new column with 18% tax added.
# Multiplying by 1.18 means:
# original amount + 18% tax.
df_orders["amount_with_tax"] = (
    df_orders["amount"] * 1.18
).round(2)

print("\nLab 11 - Amount with tax:")
print(
    df_orders[
        ["order_id", "amount", "amount_with_tax"]
    ]
)

# 12. Sort Data

# Read the orders CSV file.
df_orders = pd.read_csv("orders.csv")

# Sort the rows from the highest amount to the lowest amount.
sorted_orders = df_orders.sort_values(
    by="amount",
    ascending=False
)

# Select only order_id and amount.
# head(3) shows the first 3 rows after sorting.
top_three_orders = sorted_orders[
    ["order_id", "amount"]
].head(3)

print("\nLab 12 - Top 3 orders by amount:")
print(top_three_orders)

# 13. Group and Aggregate Data

# Read the orders CSV file.
df_orders = pd.read_csv("orders.csv")

# Group all rows that have the same customer_id.
# Then calculate:
# - total amount
# - average amount
# - number of orders
customer_summary = (
    df_orders
    .groupby("customer_id")
    .agg(
        total_amount=("amount", "sum"),
        avg_amount=("amount", "mean"),
        order_count=("amount", "count")
    )
    .reset_index()
)

# Sort customers from the highest total amount to the lowest.
customer_summary = customer_summary.sort_values(
    by="total_amount",
    ascending=False
)

print("\nLab 13 - Customer summary:")
print(customer_summary)

# 14. Merge DataFrames

# Read the orders and customers CSV files.
df_orders = pd.read_csv("orders.csv")
df_customers = pd.read_csv("customers.csv")

# Merge both DataFrames using customer_id.
# how="left" keeps all rows from df_orders.
merged_sales = pd.merge(
    df_orders,
    df_customers,
    on="customer_id",
    how="left"
)

# Select only the columns required by the lab.
merged_result = merged_sales[
    ["order_id", "name", "city", "product", "amount"]
]

print("\nLab 14 - Merged sales data:")
print(merged_result.head())

# 15. Export Output

# Read the orders and customers CSV files.
df_orders = pd.read_csv("orders.csv")
df_customers = pd.read_csv("customers.csv")

# Merge both DataFrames using customer_id.
merged_sales = pd.merge(
    df_orders,
    df_customers,
    on="customer_id",
    how="left"
)

# Keep the 6 columns required for the sales report.
sales_report = merged_sales[
    [
        "order_id",
        "customer_id",
        "name",
        "city",
        "product",
        "amount"
    ]
]

# Export the report to CSV.
# index=False prevents an extra index column.
sales_report.to_csv(
    "sales_report.csv",
    index=False
)

# Export the same report to JSON.
# orient="records" saves each row as a JSON object.
sales_report.to_json(
    "sales_report.json",
    orient="records"
)

print("\nLab 15 - Export complete")
print("Created: sales_report.csv and sales_report.json")

# Read the CSV again to verify the export.
reloaded_report = pd.read_csv("sales_report.csv")

print("Reloaded CSV shape:", reloaded_report.shape)

# 16. Integrated Lab - Mini ETL Sales Report

# Read the source files.
customers_df = pd.read_csv("customers.csv")
orders_df = pd.read_csv("orders.csv")
products_df = pd.read_json("products.json")

# Merge orders with customers using customer_id.
merged_df = pd.merge(
    orders_df,
    customers_df,
    on="customer_id",
    how="left"
)

# Merge product category information.
# The orders table uses "product".
# The products table uses "product_name".
merged_df = pd.merge(
    merged_df,
    products_df[["product_name", "category"]],
    left_on="product",
    right_on="product_name",
    how="left"
)

# Replace missing city values with "Unknown".
merged_df["city"] = merged_df["city"].fillna("Unknown")

# Replace missing categories with "Unknown".
# This keeps products that are not listed in products.json.
merged_df["category"] = merged_df["category"].fillna("Unknown")

# Create a new column with 18% tax added.
merged_df["amount_with_tax"] = (
    merged_df["amount"] * 1.18
).round(2)

# Group the data by city and category.
city_category_report = (
    merged_df
    .groupby(["city", "category"])
    .agg(
        total_sales=("amount_with_tax", "sum"),
        avg_order_value=("amount_with_tax", "mean"),
        order_count=("order_id", "count")
    )
    .reset_index()
)

# Sort the report from highest total sales to lowest.
city_category_report = city_category_report.sort_values(
    by="total_sales",
    ascending=False
)

# Export the final report to CSV.
city_category_report.to_csv(
    "city_category_report.csv",
    index=False
)

print("\nLab 16 - Final city and category report:")
print(city_category_report.head(5))

print("\nCreated: city_category_report.csv")