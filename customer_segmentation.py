# customer_segmentation.py
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# 1️⃣ Load prepared customer features
df = pd.read_csv("customer_features_engineered.csv")
print("Customer features loaded:\n", df.head())

# 2️⃣ Select numeric features for clustering
numeric_features = ['Total_Spend', 'Purchase_Frequency', 'Average_Spend']  # Add 'Recency_Days' if available
X = df[numeric_features]

# 3️⃣ Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4️⃣ Determine optimal number of clusters (Elbow Method)
inertia = []
for k in range(1, 6):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

# Plot elbow curve
plt.figure(figsize=(6,4))
plt.plot(range(1,6), inertia, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method to Determine Optimal K')
plt.show()

# 5️⃣ Fit KMeans with chosen number of clusters (e.g., k=3)
k = 3
kmeans = KMeans(n_clusters=k, random_state=42)
df['Segment'] = kmeans.fit_predict(X_scaled)

# 6️⃣ Examine segment sizes
print("\nSegment counts:\n", df['Segment'].value_counts())

# 7️⃣ Visualize segments (Total_Spend vs Purchase_Frequency)
plt.figure(figsize=(7,5))
sns.scatterplot(
    data=df, 
    x='Total_Spend', 
    y='Purchase_Frequency', 
    hue='Segment', 
    palette='Set2', 
    s=100
)
plt.title('Customer Segments')
plt.show()

# 8️⃣ Save segmented data
df.to_csv("customer_features_segmented.csv", index=False)
print("\nCustomer features with segments saved to 'customer_features_segmented.csv'")
