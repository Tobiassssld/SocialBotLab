from src.user_stat import count_active_bots


test_records = [
    {"user_id": "u1", "posts": 5, "label": 1},
    {"user_id": "u2", "posts": 3, "label": 0},
    {"user_id": "u1", "posts": 2, "label": 1},
    {"user_id": "u3", "posts": 0, "label": 1},
    {"user_id": "u4", "posts": 8, "label": 1}
]


no_active_bots = [
    {"user_id": "u1", "posts": 0, "label": 1},
    {"user_id": "u2", "posts": 5, "label": 0},
    {"user_id": "u1", "posts": 0, "label": 1},
    {"user_id": "u3", "posts": 0, "label": 1},
    {"user_id": "u4", "posts": 0, "label": 1}
]

assert count_active_bots(no_active_bots) == 0

assert count_active_bots([]) == 0

assert count_active_bots(test_records) == 2
