from pathlib import Path
import pandas as pd
import ijson

# Extract the first 1,000 records in file order (non-random sample).

project_root = Path(__file__).resolve().parents[1]

feature_path = project_root / "data" / "twibot22" / "user.json"
label_path = project_root / "data" / "twibot22" / "label.csv"
split_path = project_root / "data" / "twibot22" / "split.csv"

sample_size = 1000

def extract_profile_features(user):
    user_feature = {}

    user_feature["id"] = user["id"]
    user_feature["followers_count"] = user["public_metrics"]["followers_count"]
    user_feature["following_count"] = user["public_metrics"]["following_count"]
    user_feature["tweet_count"] = user["public_metrics"]["tweet_count"]
    user_feature["listed_count"] = user["public_metrics"]["listed_count"]

    return user_feature

user_features = []

with open(feature_path, "r", encoding="utf-8") as f:
    users = ijson.items(f, "item")
    for i in range(sample_size):
        user = next(users)
        result = extract_profile_features(user)
        user_features.append(result)


features_df = pd.DataFrame(user_features)
label_df = pd.read_csv(label_path)
split_df = pd.read_csv(split_path)

merged_df = pd.merge(features_df, label_df, on="id", how="left")
dataset_df = pd.merge(merged_df, split_df, on="id", how="left")


print(dataset_df.shape)
print(dataset_df.head())
print(dataset_df.isna().sum())
print(dataset_df["label"].value_counts(dropna=False))
print(dataset_df["id"].duplicated().sum())
print(dataset_df["split"].value_counts(dropna=False))


