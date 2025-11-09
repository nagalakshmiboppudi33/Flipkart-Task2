#step 1 data cleaning and preparation
import pandas as pd
# dataset load
df = pd.read_csv("sample_transactions.csv")
# data 
print("Rows of the dataset:")
print(df.head())
df.info()
#duplicates
df = df.drop_duplicates()
print("duplicates removed\n")
#removing null values
df = df.dropna()
print("null values removed\n")
#final data
customer_features = df.groupby('CustomerID').agg(
    Totalspent=('PurchaseAmount', 'sum'),
    Purchasefreq=('ProductID', 'count'),
    prefcategory=('Category', lambda x: x.mode()[0])
).reset_index()
print("customer features:")
print(customer_features.head())
customer_features.to_csv("customer_features_prepared.csv", index=False)
print("the prepared data in'customer_features_prepared.csv'")



