def count_active_bots(records):
    active_users = set()

    for record in records:
        if record["posts"] > 0 and record["label"] == 1:
            active_users.add(record["user_id"])

    return len(active_users)

no_active_bots = [
    {"user_id": "u1", "posts": 0, "label": 1},
    {"user_id": "u2", "posts": 5, "label": 0},
    {"user_id": "u1", "posts": 0, "label": 1},
    {"user_id": "u3", "posts": 0, "label": 1},
    {"user_id": "u4", "posts": 0, "label": 1}
]




assert count_active_bots(no_active_bots) == 0