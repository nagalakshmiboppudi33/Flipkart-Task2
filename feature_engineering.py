# feature engineering
import pandas as pd
# data loading
df = pd.read_csv("sample_transactions.csv")
#data
print("Rows of the dataset:\n")
print(df.head())
#cust data summary
print("customer summary data:\n")
cust_summary = pd.pivot_table(
    df,
    index='CustomerID',
    values='PurchaseAmount',
    aggfunc=['sum', 'mean', 'count']
)
#repalcing column names 
cust_summary.columns = ['sum', 'mean', 'count']
cust_summary.reset_index()
print(cust_summary.head())

#adding category
pref_category = df.groupby('CustomerID')['Category'].apply(lambda x: x.value_counts().idxmax()).reset_index()
pref_category.rename(columns={'Category': 'Pref_Category'}, inplace=True)
print("preffered category:", pref_category.head())

#combining both
cust_features = cust_summary.merge(pref_category, on='CustomerID')
print("final customer features:\n", cust_features.head())
cust_features.to_csv("customer_features_engineered.csv", index=False)
print("the combined data is in'customer_features_engineered.csv'")
