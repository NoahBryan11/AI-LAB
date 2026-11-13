import pandas as pd

df = pd.read_csv("/usercode/data/sales_data.csv")

#Convert data to time 
df["date"] = pd.to_datetime(df["date"])

# ACCURACY - Check for impossible values
print("=== ACCURACY CHECKS ===")

negative_prices = (df["price"] < 0).sum()
current_date = pd.Timestamp.now()
future_date_count = (df["date"] > current_date).sum()

print(f"Negative Prices: {negative_prices}")
print(f"Number of Future Dates: {future_date_count}")

# CONSISTENCY - Check standardization
print("=== CONSISTENCY CHECKS ===")

unique_products = df["product"].unique()
unique_count = df["product"].nunique()

print("Unique products:", unique_products)
print("Count of unique products:", unique_count)

# COMPLETENESS - Missing values
print("=== COMPLETENESS CHECKS ===")

missing_values = df.isnull().sum()
completeness_rate = df.notnull().mean().mean() * 100

print("Missing Values:", missing_values)
print(f"Overall completeness rate: {completeness_rate:.1f}%")

assert (df["price"] >= 0).all(), "Negative prices found!"