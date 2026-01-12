import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("activity_log.csv")

# Map category to score
score_map = {
    "productive": 1,
    "neutral": 0,
    "distracting": -1
}

df["score"] = df["category"].map(score_map)
df["weighted_score"] = df["minutes"] * df["score"]

# Aggregate per hour
hourly_score = df.groupby("hour")["weighted_score"].sum()

# Create full 24-hour index
hours = pd.Series(index=range(24), dtype=float)
hours.update(hourly_score)

# Convert to DataFrame for heatmap
heatmap_data = pd.DataFrame(hours).T
heatmap_data.index = ["Productivity"]

# Plot heatmap
plt.figure(figsize=(14, 3))
sns.heatmap(
    heatmap_data,
    cmap="RdYlGn",
    center=0,
    linewidths=0.5,
    cbar=True
)

plt.title("Daily Productivity Heatmap")
plt.xlabel("Hour of Day")
plt.ylabel("")
plt.show()
