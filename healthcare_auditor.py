import pandas as pd

data = {
    "Patient_ID" : ["P001", "P002", "P003", "P004", "P001", "P005"],
    "Age" : ["25", "unknown", "-5", "130", "25", "40"],
    "Gender" : ["Male" , "Female", "Male", "Female", "Male", "Female"],
    "Blood_Pressure" : [120 , 115, 125, 118, 120, 122],
    "Glucose" : [90 , 95, None, 100, 90 , 105],
    "Weight" : [65.5, 58.0, 70.0, None, 65.5, 62.5],
    "Appointment_Date" : ["2026-10-01","2026-10-02","2026-10-03","2026-10-04","2026-10-01", "invalid-date" ]
}

df = pd.DataFrame(data)
print(df)
print(df.shape)
print(df.dtypes)

missing_counts = df.isna().sum()
print(missing_counts)

duplicate_rows_count = df.duplicated().sum()
print(duplicate_rows_count)

duplicate_patient_count = df["Patient_ID"].duplicated().sum()
print(duplicate_patient_count)

age_numeric = pd.to_numeric(df["Age"], errors="coerce")
print(age_numeric)
print(age_numeric.isna().sum())

invalid_age_mask = (age_numeric < 0) | (age_numeric > 120)
print(invalid_age_mask.sum())
print(df[invalid_age_mask])

appointment_dates = pd.to_datetime(df["Appointment_Date"], errors="coerce")
print(appointment_dates)
invalid_date_mask = appointment_dates.isna()
print(invalid_date_mask.sum())
print(df[invalid_date_mask])

audit_summary = {
    "Rows": df.shape[0],
    "Columns": df.shape[1],
    "Missing_Values": missing_counts.sum(),
    "Duplicate_Rows": duplicate_rows_count,
    "Duplicate_Patient_IDs": duplicate_patient_count,
    "Non_Numeric_Ages": age_numeric.isna().sum(),
    "Out_Of_Range_Ages": invalid_age_mask.sum(),
    "Invalid_Dates": invalid_date_mask.sum()
}
print(audit_summary)

