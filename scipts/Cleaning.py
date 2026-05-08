import pandas as pd

df = pd.read_csv("sales_raw.csv")

print(df.head())
print()
print(df.tail())
print()
print(df.info()) #before
'''
drop_duplicates(subset, keep) = drop duplicates based on a specific col and keep the first occurrence
coerce = set it to NaN if failed instead of crashing
to_datetime() = convert to datetime format
.dt.year = extract year from datetime
.dt.month = extract month from datetime
.dt.month_name() = extract month name from datetime
to_numeric() = convert to numeric format
asastype(str) = convert to string format
abc.str.lower() = convert to lowercase
fillna() = fill missing values with specified value
df = df[df['Price']>0] : keeping only values that are greater than 0
replace() = replace values in a column with specified values
fillna(df['Quantity'].median()) = fill missing values with the median 
ffill() = forward fill, fill missing values with the last valid observation
median() → gives summary per group
transform('median'): gives value for each row in that group
'''

#======= Removing duplicates (if any) =======
df = df.drop_duplicates(subset='Order_ID', keep='first') 

'''
df['Order_ID'] = df['Order_ID'].drop_duplicates()
rather not use it because it only changes one column not whole df
'''

#======= Fixing City =======
df['City'] = df['City'].fillna('unknown').str.lower()

#======= Fixing Date =======
df['Date'] = pd.to_datetime(df['Date'], errors = 'coerce')
df = df.dropna(subset=['Date']) # drop rows where Date is NaT

# ======= Adding Year and Month columns =======
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Month_Name'] = df['Date'].dt.month_name()

'''
1) df['Date'] = df['Date'].dropna()
--> dropna() removes rows from the Series only, not from the DataFrame

2) df['Date'] = df['Date'].fillna(df['Date'].ffill())
--> If first row is NaN → still NaN, Can create incorrect timeline data
'''

#====== Fixing Price =======
df['Price'] = pd.to_numeric(df['Price'], errors = 'coerce')
'''
df['Price'] = df['Price'].fillna(df.groupby('Product')['Price'].median())
we should not use median() directly because it indexes by Product not aligned with org rows, 
transform() returns a column same size as original df
'''
df['Price'] = df['Price'].fillna(df.groupby('Product')['Price'].transform('median'))
df = df[df['Price']>0]

#======= Fixing QTY =======
df['Quantity'] = df['Quantity'].astype(str).str.lower()
df['Quantity'] = df['Quantity'].replace({
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5
})
df['Quantity'] = pd.to_numeric(df['Quantity'], errors = 'coerce')
# Different products may have different buying patterns
# so we fill missing Quantity with median of that specific product
df['Quantity'] = df['Quantity'].fillna(df.groupby('Product')['Quantity'].transform('median'))
df = df[df['Quantity']> 0]
df['Quantity'] = df['Quantity'].astype(int)

# ======= Adding Revenue column =======
df['Revenue'] = df['Price'] * df['Quantity']

# ======= Sorting & Resetting index =======
df = df.sort_values(by = 'Date')
df = df.reset_index(drop=True)

# ======= Final check =======
print(df.info())
print()
print(df.head())
print()
print(df.tail())
print()
print(df.describe())

# ======= Saving cleaned data =======
df.to_csv("sales_cleaned.csv", index=False)
