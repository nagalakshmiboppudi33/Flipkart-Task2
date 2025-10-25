# feature_engineering_alternative.py
import pandas as pd

# 1️⃣ Load dataset
df = pd.read_csv("sample_transactions.csv")

print("Dataset loaded. First few rows:\n", df.head())

# 2️⃣ Create a summary table using pivot_table
customer_summary = pd.pivot_table(
    df,
    index='CustomerID',
    values='PurchaseAmount',
    aggfunc=['sum', 'mean', 'count']
)

# Flatten MultiIndex columns
customer_summary.columns = ['Total_Spend', 'Average_Spend', 'Purchase_Frequency']
customer_summary.reset_index(inplace=True)

print("\nCustomer summary using pivot_table:\n", customer_summary.head())

# 3️⃣ Determine most purchased category per customer
preferred_category = df.groupby('CustomerID')['Category'].apply(lambda x: x.value_counts().idxmax()).reset_index()
preferred_category.rename(columns={'Category': 'Preferred_Category'}, inplace=True)

print("\nPreferred category per customer:\n", preferred_category.head())

# 4️⃣ Merge features
customer_features = customer_summary.merge(preferred_category, on='CustomerID')
print("\nFinal customer features:\n", customer_features.head())

# 5️⃣ Save to CSV
customer_features.to_csv("customer_features_engineered.csv", index=False)
print("\nCustomer features saved to 'customer_features_engineered.csv'")
