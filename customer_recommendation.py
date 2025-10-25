# customer_recommendation.py
import pandas as pd

# 1️⃣ Load cleaned transactions and segmented customers
transactions = pd.read_csv("sample_transactions.csv")

customers = pd.read_csv("customer_features_segmented.csv")

print("Transactions and customer segments loaded.")

# 2️⃣ Merge transactions with segments
data = transactions.merge(customers[['CustomerID', 'Segment']], on='CustomerID')
print("\nData with segments:\n", data.head())

# 3️⃣ Compute top products per segment
top_products = data.groupby(['Segment', 'ProductID'])['PurchaseAmount'] \
                   .sum().reset_index()

# Rank products within each segment
top_products['Rank'] = top_products.groupby('Segment')['PurchaseAmount'] \
                                  .rank(method='first', ascending=False)

# Keep top 3 products per segment
top_products_per_segment = top_products[top_products['Rank'] <= 3] \
    .sort_values(['Segment', 'Rank'])

print("\nTop recommended products per segment:\n", top_products_per_segment)

# 4️⃣ Save recommendations
# 3️⃣ Print top recommended products per segment
print("\nTop recommended products per segment:\n", top_products_per_segment)
