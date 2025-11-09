#customer visualizations
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#loading from customer segment visualizations
df = pd.read_csv("customer_features_segmented.csv")
sns.countplot(x='Segment', data=df, palette='Set2', hue=None)
 #segment size
plt.figure(figsize=(6,4))
sns.countplot(x='Segment',data=df,palette='Set2')
plt.title("customer Count as per Segment")
plt.xlabel("Segment")
plt.ylabel("No of Customers")
plt.show()
#total Spent by Segment
plt.figure(figsize=(6,4))
sns.boxplot(x='Segment', y='sum', data=df, palette='Set3')
plt.title("Total Spend Distribution per Segment")
plt.xlabel("Segment")
plt.ylabel("Total money spent")
plt.show()
#purchase Frequency as per Segment
plt.figure(figsize=(6,4))
sns.boxplot(x='Segment', y='count', data=df, palette='Set1')
plt.title("purchase Frequency as per Segment")
plt.xlabel("Segment")
plt.ylabel("count")
plt.show()
#preferred Category as per Segment
category_segment = df.groupby(['Segment', 'Pref_Category'])
plt.bar(stacked=True, figsize=(8,5), colormap='Pastel1')
plt.title("Preferred Category as per Segment")
plt.xlabel("Segment")
plt.ylabel("No of Customers")
plt.legend(title='Category')
plt.show()
