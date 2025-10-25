import pandas as pd

# 1️⃣ Load dataset
df = pd.read_csv("sample_transactions.csv")

# 2️⃣ Preview dataset
print("First 5 rows of the dataset:")
print(df.head())

print("\nDataset shape:", df.shape)
print("\nMissing values per column:\n", df.isnull().sum())

# 3️⃣ Clean the data
# Fill numeric columns with median
numeric_cols = df.select_dtypes(include='number').columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

# Fill categorical columns with mode
categorical_cols = df.select_dtypes(include='object').columns
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# Remove duplicate rows
df = df.drop_duplicates()

# Convert PurchaseDate to datetime
df['PurchaseDate'] = pd.to_datetime(df['PurchaseDate'], errors='coerce')

# Drop rows with invalid data
df = df.dropna().reset_index(drop=True)

# 4️⃣ Create customer-level features
customer_features = df.groupby('CustomerID').agg(
    Total_Spend=('PurchaseAmount', 'sum'),
    Purchase_Frequency=('ProductID', 'count'),
    Preferred_Category=('Category', lambda x: x.mode()[0])
).reset_index()

# 5️⃣ Preview prepared features
print("\nCustomer Features:")
print(customer_features.head())

# 6️⃣ Save prepared features for next steps
customer_features.to_csv("customer_features_prepared.csv", index=False)
print("\n Prepared features saved to 'customer_features_prepared.csv'")
