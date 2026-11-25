from src.user_stat import count_active_bots
from src.user_stat import count_unique_active_humans
from src.user_stat import count_labels

records = [
    {"user_id": "u1", "posts": 3, "label": 0},
    {"user_id": "u2", "posts": 5, "label": 1},
    {"user_id": "u1", "posts": 2, "label": 0},
    {"user_id": "u3", "posts": 0, "label": 0},
    {"user_id": "u4", "posts": 8, "label": 0}
]


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

assert count_unique_active_humans(records) == 2

assert count_unique_active_humans([]) == 0

assert count_labels(records) == {0: 4, 1: 1}

assert count_labels([]) == {}
