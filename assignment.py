import pandas as pd

# 1. Create a DataFrame manually
data = {
    "name": ["Ram", "Sham", "Rani", "Pari", "Gita"],
    "age": [20, 23, None, 27, 25],
    "marks": [80, 75, 90, None, 85]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


# 2. Handle missing values using fillna()
df["age"] = df["age"].fillna(df["age"].mean())
df["marks"] = df["marks"].fillna(df["marks"].mean())

print("\nAfter filling missing values:")
print(df)


# 3. Sort DataFrame by a column
df = df.sort_values("age")

print("\nDataFrame sorted by age:")
print(df)


# 4. Find mean, median, and mode of numeric columns

print("\nMean:")
print(df[["age", "marks"]].mean())

print("\nMedian:")
print(df[["age", "marks"]].median())

print("\nMode:")
print(df[["age", "marks"]].mode())