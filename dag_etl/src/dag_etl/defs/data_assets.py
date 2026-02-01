import pandas as pd
import numpy as np
from dagster import asset


@asset
def create_dirty_data():
    data = {
        "Name": [" John Doe ", "Jane Smith", "Bob Johnson ", "  Alice Brown"],
        "Age": [30, np.nan, 40, 35],
        "City": ["New York", "los angeles", "CHICAGO", "Houston"],
        "Salary": ["50,000", "60000", "75,000", "invalid"],
    }

    df = pd.DataFrame(data)

    dirty_file_path = "dirty_data.csv"
    df.to_csv(dirty_file_path, index=False)

    return dirty_file_path


@asset
def clean_data(create_dirty_data: str):
    df = pd.read_csv(create_dirty_data)

    df["Name"] = df["Name"].str.strip()
    df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
    df["Age"] = df["Age"].fillna(df["Age"].mean())
    df["City"] = df["City"].str.upper()
    df["Salary"] = df["Salary"].replace(r"[\$,]", "", regex=True)
    df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce").fillna(0)

    avg_salary = df["Salary"].mean()

    cleaned_file_path = "cleaned_data.csv"
    df.to_csv(cleaned_file_path, index=False)

    return {
        "cleaned_file_path": cleaned_file_path,
        "avg_salary": avg_salary,
    }


@asset
def load_cleaned_data(clean_data: dict):
    cleaned_file_path = clean_data["cleaned_file_path"]
    avg_salary = clean_data["avg_salary"]

    df = pd.read_csv(cleaned_file_path)

    return {
        "num_rows": len(df),
        "num_columns": len(df.columns),
        "avg_salary": avg_salary,
    }
