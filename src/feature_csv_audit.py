from pathlib import Path
import csv

project_root = Path(__file__).resolve().parents[1]
output_path = project_root / "data" / "processed" / "profile_features_full.csv"


with open(output_path, "r", encoding="utf-8", newline="") as f:
    saved_count = sum(1 for row in csv.DictReader(f))

print("Saved records:", saved_count)

unique_ids = set()

with open(output_path, "r", encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        unique_ids.add(row["id"])


print("Unique IDs:", len(unique_ids))
print("Duplicate IDs:", saved_count - len(unique_ids))

missing_counts = {
    "followers_count": 0,
    "following_count": 0,
    "tweet_count": 0,
    "listed_count": 0
}

with open(output_path, "r", encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        for feature in missing_counts:
            if row[feature] == "":
                missing_counts[feature] += 1

print("Missing values:", missing_counts)