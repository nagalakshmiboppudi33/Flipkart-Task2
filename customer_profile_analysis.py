#profile analysis
import pandas as pd
#data loading
df = pd.read_csv("customer_features_segmented.csv")
print("Segmented data loaded")
#segment summary
segment_summary = df.groupby('Segment').agg(
    Count=('CustomerID', 'count'),         
    Avg_Total_Spend=('sum', 'mean'),     # Average spend
    Avg_Purchase_Freq=('count', 'mean'), # Avg purchase frequency
    Avg_Average_Spend=('mean', 'mean'), # Avg spend per purchase
    Top_Category=('Pref_Category', lambda x: x.value_counts().idxmax()) 
).reset_index()
print("\nSegment Profile Summary:\n", segment_summary)
segment_summary.to_csv("customer_segment_profiles.csv", index=False)
print("\nSegment profiles saved to 'customer_segment_profiles.csv'")
