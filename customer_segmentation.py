# customer segmentation
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
#load data from feature engineering
df = pd.read_csv("customer_features_engineered.csv")
print("Customer features loaded:\n", df.head())
#Select numeric features for clustering
numeric_features = ['sum', 'count', 'mean'] 
x = df[numeric_features]
#standardize features
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)
#clustering kmeans
kmeans = KMeans(n_clusters=3, random_state=42)
df['segment'] = kmeans.fit_predict(x_scaled)

df.to_csv("customer_features_segmented.csv", index=False)
print("customer features as per segments is in 'customer_features_segmented.csv'")
