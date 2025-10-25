# customer_visualization.py
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1️⃣ Load segmented customer features
df = pd.read_csv("customer_features_segmented.csv")
print("Segmented customer data loaded.\n")
sns.countplot(x='Segment', data=df, palette='Set2', hue=None)
 
# 2️⃣ Segment size
plt.figure(figsize=(6,4))
sns.countplot(x='Segment', data=df, palette='Set2')
plt.title("Customer Count per Segment")
plt.xlabel("Segment")
plt.ylabel("Number of Customers")
plt.show()

# 3️⃣ Total Spend by Segment
plt.figure(figsize=(6,4))
sns.boxplot(x='Segment', y='Total_Spend', data=df, palette='Set3')
plt.title("Total Spend Distribution per Segment")
plt.xlabel("Segment")
plt.ylabel("Total Spend")
plt.show()

# 4️⃣ Purchase Frequency by Segment
plt.figure(figsize=(6,4))
sns.boxplot(x='Segment', y='Purchase_Frequency', data=df, palette='Set1')
plt.title("Purchase Frequency per Segment")
plt.xlabel("Segment")
plt.ylabel("Purchase Frequency")
plt.show()

# 5️⃣ Preferred Category per Segment
category_segment = df.groupby(['Segment', 'Preferred_Category']).size().unstack(fill_value=0)
category_segment.plot(kind='bar', stacked=True, figsize=(8,5), colormap='Pastel1')
plt.title("Preferred Category per Segment")
plt.xlabel("Segment")
plt.ylabel("Number of Customers")
plt.legend(title='Category')
plt.show()
