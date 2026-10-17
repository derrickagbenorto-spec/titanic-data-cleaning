

import pandas as pd

# 1. Load the original dataset
df = pd.read_csv("train.csv")

print("ORIGINAL DATASET SIZE:", df.shape)

# 2. Record initial quality issues
print("\nMISSING VALUES BEFORE CLEANING:")
print(df.isnull().sum())

print("\nDUPLICATE ROWS BEFORE CLEANING:")
print(df.duplicated().sum())

# 3. Remove unnecessary spaces from text fields
for col in df.select_dtypes(include=["object", "str"]).columns:
    df[col] = df[col].str.strip()

# 4. Standardize categorical values
df["Sex"] = df["Sex"].str.lower()
df["Embarked"] = df["Embarked"].str.upper()

# 5. Ensure numeric columns have appropriate types
numeric_columns = [
    "PassengerId", "Survived", "Pclass", "Age",
    "SibSp", "Parch", "Fare"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# 6. Remove exact duplicate rows if present
df = df.drop_duplicates()

# 7. Fill missing Age values using the median
# for passengers in the same class and sex
df["Age"] = df["Age"].fillna(
    df.groupby(["Pclass", "Sex"])["Age"].transform("median")
)
df["Age"] = df["Age"].fillna(df["Age"].median())

# 8. Fill missing Embarked values using the mode
df["Embarked"] = df["Embarked"].fillna(
    df["Embarked"].mode()[0]
)

# 9. Label unavailable cabin information
df["Cabin"] = df["Cabin"].fillna("Unknown")

# 10. Save the cleaned dataset
df.to_csv("cleaned_titanic.csv", index=False)

# 11. Verify the cleaning results
print("\nCLEANED DATASET SIZE:", df.shape)

print("\nMISSING VALUES AFTER CLEANING:")
print(df.isnull().sum())

print("\nDUPLICATE ROWS AFTER CLEANING:")
print(df.duplicated().sum())

print("\nFINAL DATA TYPES:")
print(df.dtypes)

print("\nSUCCESS: cleaned_titanic.csv has been saved.")

