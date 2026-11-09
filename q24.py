import pandas as pd

# 1. Load the dataset
df = pd.read_csv("titanic.csv")

print("Original Dataset:")
print(df.head())

# 2. Display basic information
print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# 3. Remove duplicate rows
df.drop_duplicates(inplace=True)

# 4. Handle missing values

# Fill missing Age with median
df["Age"].fillna(df["Age"].median(), inplace=True)

# Fill missing Fare with median
df["Fare"].fillna(df["Fare"].median(), inplace=True)

# Fill missing Embarked with mode
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)

# Fill missing Name and Ticket with "Unknown"
df["Name"].fillna("Unknown", inplace=True)
df["Ticket"].fillna("Unknown", inplace=True)

# Cabin has many missing values, so replace them with "Unknown"
df["Cabin"].fillna("Unknown", inplace=True)

# 5. Convert categorical columns into numerical form

# Convert Sex into numerical values
df["Sex"] = df["Sex"].map({
    "male": 0,
    "female": 1
})

# One-hot encode Embarked
df = pd.get_dummies(df, columns=["Embarked"], dtype=int)

# 6. Create a new feature: FamilySize
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

# 7. Remove unnecessary columns
df.drop(["Name", "Ticket", "Cabin"], axis=1, inplace=True)

# 8. Check the cleaned dataset
print("\nCleaned Dataset:")
print(df.head())

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# 9. Save the cleaned dataset
df.to_csv("cleaned_titanic.csv", index=False)

print("\nCleaned dataset saved as 'cleaned_titanic.csv'")
