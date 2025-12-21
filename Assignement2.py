import numpy as np
import pandas as pd

# Part 1
# 1
products_id = np.array([1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010])
print("Products ID:", products_id)

inventory_data = np.array([
    [50, 15.5, 10.99],
    [120, 3.2, 50.50],
    [30, 25.0, 5.00],
    [85, 12.8, 22.75],
    [200, 8.5, 15.99],
    [15, 18.3, 8.50],
    [75, 6.7, 35.00],
    [45, 20.1, 12.25],
    [160, 4.5, 28.99],
    [95, 14.2, 18.75]
])
print("Inventory Data:\n", inventory_data)

# 2
print("Shape of Inventory Data:", inventory_data.shape)
print("Data Type of Inventory Data:", inventory_data.dtype)

total_value = inventory_data[:,0] * inventory_data[:,2]
print("Total Value per product:", total_value)

# 3 
subset_products = inventory_data[2:7, :]
print("Subset of products (3rd to 7th):\n", subset_products)

average_weekly_sales = np.mean(inventory_data[:,1])
print("Average Weekly Sales:", average_weekly_sales)

print("Unit Cost of first product:", inventory_data[0,2])

# Part 2
# 1
weeks_of_stock = inventory_data[:,0] / inventory_data[:,1]
low_stock_mask = weeks_of_stock < 4
low_stock_products = inventory_data[low_stock_mask]
print("Low stock products:\n", low_stock_products)

#2
reorder_quantity = (4 * inventory_data[:,1]) - inventory_data[:,0]
reorder_quantity = np.where(reorder_quantity < 0, 0, reorder_quantity)
reorder_quantity = reorder_quantity.reshape(-1,1)
updated_inventory = np.concatenate((inventory_data, reorder_quantity), axis=1)
print("Updated Inventory with Reorder Quantity:\n", updated_inventory)

# Part 3
# 1
column_names = ['Stock', 'Sales', 'Cost', 'Reorder Qty']
inventory_df = pd.DataFrame(updated_inventory, columns=column_names, index=products_id)
print("Full Inventory DataFrame:")
print(inventory_df)

#2
stock_reorder = inventory_df[['Stock', 'Reorder Qty']]
print("\nStock and Reorder Quantity:")
print(stock_reorder)

first_five_rows = inventory_df.head(5)
print("\nFirst 5 rows of Inventory DataFrame:")
print(first_five_rows)
