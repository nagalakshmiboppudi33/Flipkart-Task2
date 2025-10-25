# customer_profile_analysis.py
import pandas as pd

# 1️⃣ Load segmented customer data
df = pd.read_csv("customer_features_segmented.csv")
print("Segmented data loaded. First few rows:\n", df.head())

# 2️⃣ Describe each segment
segment_summary = df.groupby('Segment').agg(
    Count=('CustomerID', 'count'),                # Number of customers
    Avg_Total_Spend=('Total_Spend', 'mean'),     # Average spend
    Avg_Purchase_Freq=('Purchase_Frequency', 'mean'), # Avg purchase frequency
    Avg_Average_Spend=('Average_Spend', 'mean'), # Avg spend per purchase
    Top_Category=('Preferred_Category', lambda x: x.value_counts().idxmax())  # Most common category
).reset_index()

print("\nSegment Profile Summary:\n", segment_summary)

# 3️⃣ Save profile summary
segment_summary.to_csv("customer_segment_profiles.csv", index=False)
print("\nSegment profiles saved to 'customer_segment_profiles.csv'")
