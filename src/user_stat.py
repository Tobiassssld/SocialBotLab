def count_active_bots(records):
    active_users = set()

    for record in records:
        if record["posts"] > 0 and record["label"] == 1:
            active_users.add(record["user_id"])

    return len(active_users)

def count_unique_active_humans(records):
    active_humans = set()
    for record in records:
        if record["posts"] > 0 and record["label"] == 0:
            active_humans.add(record["user_id"])

    return len(active_humans)

def count_labels(records):
    label_counts = {}

    for record in records:
        label = record["label"]

        current_count = label_counts.get(label, 0)
        new_count = current_count + 1
        label_counts[label] = new_count

    return label_counts