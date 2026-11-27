from pathlib import Path
from profile_features import extract_profile_features
import pandas as pd
import ijson

# Extract the first 1,000 records in file order (non-random sample).

project_root = Path(__file__).resolve().parents[1]

feature_path = project_root / "data" / "twibot22" / "user.json"
label_path = project_root / "data" / "twibot22" / "label.csv"
split_path = project_root / "data" / "twibot22" / "split.csv"


output_dir = project_root / "data" / "processed"
output_dir.mkdir(parents=True, exist_ok=True)
output_path = output_dir / "profile_features_4500.csv"

sample_size = 4500
batch_size = 2000

batch = []
first_batch = True

with open(feature_path, "r", encoding="utf-8") as f:
    users = ijson.items(f, "item")
    for i in range(sample_size):
        user = next(users)
        result = extract_profile_features(user)
        batch.append(result)
        if len(batch) == batch_size:
            batch_df = pd.DataFrame(batch)

            if first_batch:
                batch_df.to_csv(
                    output_path,
                    mode="w",
                    index=False,
                    header=True
                )
                first_batch = False
            else:
                batch_df.to_csv(
                    output_path,
                    mode="a",
                    index=False,
                    header=False
                )

            batch = []

# Save remaining records
if batch:
    batch_df = pd.DataFrame(batch)

    if first_batch:
        batch_df.to_csv(
            output_path,
            mode="w",
            index=False,
            header=True
        )
    else:
        batch_df.to_csv(
            output_path,
            mode="a",
            index=False,
            header=False
        )


saved_df = pd.read_csv(output_path)

print("Saved shape:", saved_df.shape)

print("Duplicate IDs:", saved_df["id"].duplicated().sum())



# features_df = pd.DataFrame(user_features)
# label_df = pd.read_csv(label_path)
# split_df = pd.read_csv(split_path)
#
# merged_df = pd.merge(features_df, label_df, on="id", how="left")
# dataset_df = pd.merge(merged_df, split_df, on="id", how="left")

# print(dataset_df.shape)
# print(dataset_df.head())
# print(dataset_df.isna().sum())
# print(dataset_df["label"].value_counts(dropna=False))
# print(dataset_df["id"].duplicated().sum())
# print(dataset_df["split"].value_counts(dropna=False))


#
# dataset_df.to_csv(output_path, index=False)
#
# saved_df = pd.read_csv(output_path)
#
# print("Saved shape:", saved_df.shape)
