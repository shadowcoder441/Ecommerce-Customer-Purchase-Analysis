import pandas as pd
import matplotlib.pyplot as plt

#Loading the dataset here:
df = pd.read_csv("Project_Dataset.csv")

#Creating a Total_Purchase Column:
df["total_purchase"] = df["quantity"] * df["price"]

#------------------------------------
# 1. Top Customers
# -----------------------------------
top_customers = df.groupby("customer_name")["total_purchase"]. sum().sort_values(ascending = False)

print('\nTop Customers: \n')
print(top_customers)

#-------------------------------------
# 2. Product Popularity
#-------------------------------------
prodcut_sales = df.groupby("product")["quantity"].sum().sort_values(ascending = False)
print('\nProduct Popularity: \n')
print(prodcut_sales)

#-------------------------------------
# 3. City Revenue
#-------------------------------------
city_sales = df.groupby("city")["total_purchase"].sum().sort_values(ascending=False)

print("\nCity Revenue:\n")
print(city_sales)

# -------------------------------
# 4. Bar Chart → Product Sales
# -------------------------------
plt.figure()
prodcut_sales.plot(kind='bar')
plt.title("Product Sales (Quantity-wise)")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.tight_layout()
plt.show()

# -------------------------------
# 5. Pie Chart → City Revenue
# -------------------------------
plt.figure()
city_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("City Revenue Distribution")
plt.ylabel("")
plt.tight_layout()
plt.show()