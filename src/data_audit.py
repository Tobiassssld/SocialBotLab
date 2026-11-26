import pandas as pd
from pathlib import Path


project_root = Path(__file__).resolve().parents[1]


label_path = project_root / "data" / "twibot22" / "label.csv"
split_path = project_root / "data" / "twibot22" / "split.csv"


label_df = pd.read_csv(label_path)
split_df = pd.read_csv(split_path)


def audit_dataframe(df):
    print("Shape:", df.shape)
    print("Columns:", df.columns.tolist())
    print("Missing values:", df.isna().sum())
    print("Duplicate IDs:", df["id"].duplicated().sum())

def label_distribution(df):
    print(df["label"].value_counts(dropna=False))

def split_distribution(df):
    print(df["split"].value_counts(dropna=False))

def id_consistency(df1, df2):
    label_ids = set(df1["id"])
    split_ids = set(df2["id"])

    print("check label and split ids consistency:", label_ids == split_ids)


print("=== LABEL DATA AUDIT ===")
audit_dataframe(label_df)

print("=== SPLIT DATA AUDIT ===")
audit_dataframe(split_df)

print("=== LABEL Distribution ===")
label_distribution(label_df)

print("=== Split Distribution ===")
split_distribution(split_df)

print("=== ID CONSISTENCY ===")
id_consistency(label_df, split_df)

