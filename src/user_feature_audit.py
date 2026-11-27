from pathlib import Path
from profile_features import extract_profile_features
from batch_writer import save_batch
import pandas as pd
import ijson


project_root = Path(__file__).resolve().parents[1]

feature_path = project_root / "data" / "twibot22" / "user.json"
label_path = project_root / "data" / "twibot22" / "label.csv"
split_path = project_root / "data" / "twibot22" / "split.csv"


output_dir = project_root / "data" / "processed"
output_dir.mkdir(parents=True, exist_ok=True)
output_path = output_dir / "profile_features_full.csv"

batch_size = 2000

batch = []
first_batch = True

with open(feature_path, "r", encoding="utf-8") as f:
    users = ijson.items(f, "item")
    processed_count = 0
    for user in users:
        result = extract_profile_features(user)
        batch.append(result)
        processed_count += 1

        if len(batch) == batch_size:
            first_batch = save_batch(batch, output_path, first_batch)
            batch = []


# Save remaining records
if batch:
    save_batch(batch, output_path, first_batch)

print("Processed users:", processed_count)


# saved_df = pd.read_csv(output_path)
#
# print("Saved shape:", saved_df.shape)
#
# print("Duplicate IDs:", saved_df["id"].duplicated().sum())

