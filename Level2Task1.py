import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "C:/Users/ganes/Downloads/rayuduintern/Dataset .csv"
df = pd.read_csv(file_path)

df['Has Table booking'] = df['Has Table booking'].map({'Yes': 'Table Booking', 'No': 'No Table Booking'})
df['Has Online delivery'] = df['Has Online delivery'].map({'Yes': 'Online Delivery', 'No': 'No Online Delivery'})

table_booking_counts = df['Has Table booking'].value_counts(normalize=True) * 100
online_delivery_counts = df['Has Online delivery'].value_counts(normalize=True) * 100

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.barplot(x=table_booking_counts.index, y=table_booking_counts.values, ax=axes[0], palette=['lightcoral', 'lightblue'])
axes[0].set_title("Percentage of Restaurants Offering Table Booking")
axes[0].set_ylabel("Percentage")

sns.barplot(x=online_delivery_counts.index, y=online_delivery_counts.values, ax=axes[1], palette=['lightgreen', 'orange'])
axes[1].set_title("Percentage of Restaurants Offering Online Delivery")
axes[1].set_ylabel("Percentage")

plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(x=df['Has Table booking'], y=df['Aggregate rating'], palette="coolwarm")
plt.title("Comparison of Ratings for Restaurants with and without Table Booking")
plt.xlabel("Table Booking")
plt.ylabel("Aggregate Rating")
plt.show()

plt.figure(figsize=(8, 5))
sns.countplot(x='Price range', hue='Has Online delivery', data=df, palette="magma")
plt.title("Online Delivery Availability Across Different Price Ranges")
plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")
plt.legend(title="Online Delivery")
plt.show()

plt.figure(figsize=(8, 5))
sns.violinplot(x='Price range', y='Aggregate rating', hue='Has Online delivery', data=df, split=True, palette="coolwarm")
plt.title("Ratings Distribution by Price Range and Online Delivery Availability")
plt.xlabel("Price Range")
plt.ylabel("Aggregate Rating")
plt.legend(title="Online Delivery")
plt.show()
