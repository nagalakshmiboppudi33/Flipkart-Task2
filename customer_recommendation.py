#customer recommondation
import pandas as pd
#loading transactions and customers data
transactions=pd.read_csv("sample_transactions.csv")
customers=pd.read_csv("customer_features_segmented.csv")
print("data loaded\n")
#data per segment
data = transactions.merge(customers[['CustomerID', 'Segment']],on='CustomerID')
print("data with segments:\n", data.head())
print("")
# top products as per segment
topproducts = data.groupby(['Segment', 'ProductID'])['PurchaseAmount'] \
                             .sum().reset_index()
#ranking the products as per segment
topproducts['Rank'] = topproducts.groupby('Segment')['PurchaseAmount'] \
                                  .rank(method='first', ascending=False)
#Keep top products  as per segment
top_products_per_segment = topproducts[topproducts['Rank'] <= 3] \
    .sort_values(['Segment', 'Rank'])
print("recommended products per segment:\n", top_products_per_segment)
