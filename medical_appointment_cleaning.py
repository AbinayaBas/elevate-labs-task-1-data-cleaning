import pandas as pd

df = pd.read_csv("data/raw/KaggleV2-May-2016.csv")

print(df.head())
print(df.shape)
print(df.info())
print("\nMissing values:")
print(df.isnull().sum())
print("\nDuplicate rows:")
print(df.duplicated().sum())
print("\nOriginal column names:")
print(df.columns.tolist())
df.columns = [
    "patient_id",
    "appointment_id",
    "gender",
    "scheduled_day",
    "appointment_day",
    "age",
    "neighbourhood",
    "scholarship",
    "hypertension",
    "diabetes",
    "alcoholism",
    "handicap",
    "sms_received",
    "no_show"
]
print("\nCleaned column names:")
print(df.columns.tolist())
df["scheduled_day"] = pd.to_datetime(df["scheduled_day"])
df["appointment_day"] = pd.to_datetime(df["appointment_day"])
print("\nDate column data types:")
print(df[["scheduled_day", "appointment_day"]].dtypes)
print("\nGender values:")
print(df["gender"].unique())
print("\nNo-show values:")
print(df["no_show"].unique())
print("\nAge statistics:")
print(df["age"].describe())
print("\nUnique age values:")
print(df["age"].unique())
print("\nUnique values in binary columns:")
for column in ["scholarship", "hypertension", "diabetes", "alcoholism", "handicap", "sms_received"]:
 print(column, ":", df[column].unique())
invalid_age_count = (df["age"] < 0).sum()
print("\nInvalid age records:")
print(invalid_age_count)
df = df[df["age"] >= 0]
print("\nDataset shape after removing invalid age:")
print(df.shape)
print("\nInvalid age records after cleaning:")
print((df["age"] < 0).sum())
print("\nPatient ID sample:")
print(df["patient_id"].head())
print("\nPatient ID data type:")
print(df["patient_id"].dtype)
print("\nUnique Patient IDs:")
print(df["patient_id"].nunique())
print("\nTotal records:")
print(len(df))
print("\nPatient ID sample with full precision:")
print(df["patient_id"].head(10).to_string())
print("\nPatient ID missing values:")
print(df["patient_id"].isnull().sum())
print("\nNumber of unique neighbourhoods:")
print(df["neighbourhood"].nunique())
print("\nSample neighbourhood values:")
print(df["neighbourhood"].unique()[:20])
print("\nBlank neighbourhood values:")
print((df["neighbourhood"].str.strip() == "").sum())
text_columns = ["gender", "neighbourhood", "no_show"]
for column in text_columns:
    df[column] = df[column].str.strip()
print("\nText columns cleaned:")
print(df[text_columns].head())
print("\n========== FINAL DATA QUALITY CHECK ==========")
print("Dataset shape:", df.shape)
print("\nMissing values:")
print(df.isnull().sum().sum())
print("\nDuplicate rows:")
print(df.duplicated().sum())
print("\nInvalid ages:")
print((df["age"] < 0).sum())
print("\nData types:")
print(df.dtypes)
output_path = "data/cleaned/medical_appointment_cleaned.csv"
df.to_csv(output_path, index=False)
print("\nCleaned dataset saved successfully!")
print("File:", output_path)