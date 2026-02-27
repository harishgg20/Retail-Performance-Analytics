import pandas as pd
import numpy as np

# =========================
# 1. Load Raw Dataset
# =========================

file_path = "SuperStore.csv"
df = pd.read_csv(file_path, encoding='latin1')

# Remove BOM issue if exists
df.columns = df.columns.str.replace('ï»¿', '', regex=False)

# =========================
# 2. Date Cleaning
# =========================

df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True, errors='coerce')
df['ship_date'] = pd.to_datetime(df['ship_date'], dayfirst=True, errors='coerce')

# Extract Year & Month
df['year'] = df['order_date'].dt.year
df['month'] = df['order_date'].dt.month
df['month_name'] = df['order_date'].dt.month_name()

# =========================
# 3. Delivery Days
# =========================

df['delivery_days'] = (df['ship_date'] - df['order_date']).dt.days

# =========================
# 4. Sales Cleaning
# =========================

df['sales'] = (
    df['sales']
    .astype(str)
    .str.replace(',', '', regex=False)
    .str.replace('$', '', regex=False)
)

df['sales'] = pd.to_numeric(df['sales'], errors='coerce')

# =========================
# 5. Profit Margin
# =========================

df['profit_margin'] = np.where(
    df['sales'] != 0,
    df['profit'] / df['sales'],
    0
)

# =========================
# 6. Remove Nulls
# =========================

df = df.dropna()

# =========================
# 7. Export Cleaned File
# =========================

output_path = r"C:\superstore_db\SuperStore_Cleaned.csv"
df.to_csv(output_path, index=False)

print("Data cleaning completed successfully!")
