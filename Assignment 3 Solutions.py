import pandas as pd

#Part1: Reading and Inspecting Data
# Read csv file
data = pd.read_csv('global_sales.csv')

# Display first 5 rows of the dataframe
print(data.head())

# Display data types of each column
print(data.dtypes)


# Part 2: Data Cleaning and Indexing
# 1. Handling missing values and casting
# Fill missing values in Units_Sold with column mean
data["Units_Sold"] = data["Units_Sold"].fillna(data["Units_Sold"].mean())
print(data)

# Convert Sales column to numeric (coerce errors to NaN, then fill with 0)
data["Sales"] = pd.to_numeric(data["Sales"], errors="coerce").fillna(0)
print(data)

# Convert Date column to datetime
data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
print(data)

# 2. Indexing and Setting
# Set OrderID as index
data.set_index("OrderID", inplace=True)

# Reset index
data.reset_index(inplace=True)

# Set Date as index for time series analysis
data.set_index("Date", inplace=True)


# Part 3: Filtering, Modifying, and Sorting
# 1. Filtering Data
# High value European sales
high_value_sales = data[(data["Sales"] > 500) & (data["Region"] == "Europe")]
print(high_value_sales.head())

# 2. Updating and Adding Columns
# Update Units_Sold for the 5th row (position-based)
data.iloc[4, data.columns.get_loc("Units_Sold")] = 99

# Add Profit column
data["Profit"] = data["Sales"] * 0.20
print(data)

# 3. Sorting Data
# Sort by Region (ascending) and Sales (descending)
sorted_data = data.sort_values(
    by=["Region", "Sales"],
    ascending=[True, False]
)
print(sorted_data.head())


# Part 4: Grouping and Aggregation
# Regional Performance
regional_performance = data.groupby("Region").agg(
    Total_Sales=("Sales", "sum"),
    Avg_Units_Sold=("Units_Sold", "mean")
)
print(regional_performance)

# Product Deep Dive
product_profit = data.groupby("Product").agg(
    Max_Profit=("Profit", "max")
)

print(product_profit)

# Time Series Analysis
monthly_sales = data.resample("M")["Sales"].sum()
print(monthly_sales)

