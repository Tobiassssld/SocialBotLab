def count_active_bots(records):
    active_users = set()

    for record in records:
        if record["posts"] > 0 and record["label"] == 1:
            active_users.add(record["user_id"])

    return len(active_users)

