import pandas as pd
from src.batch_writer import save_batch


def test_first_batch_creates_file(tmp_path):
    output_path = tmp_path / "profiles.csv"

    batch = [
        {"id": "u1", "followers_count": 10},
        {"id": "u2", "followers_count": 20}
    ]

    next_first_batch = save_batch(batch, output_path, True)

    saved_df = pd.read_csv(output_path)

    assert saved_df.shape == (2, 2)
    assert next_first_batch is False

def test_second_batch_appends(tmp_path):
    output_path = tmp_path / "profiles.csv"

    batch1 = [
        {"id": "u1", "followers_count": 10},
        {"id": "u2", "followers_count": 20}
    ]

    batch2 = [
        {"id": "u3", "followers_count": 30}
    ]

    first_batch = save_batch(batch1, output_path, True)

    first_batch = save_batch(batch2, output_path, first_batch)

    saved_df = pd.read_csv(output_path)

    assert saved_df.shape == (3, 2)
    assert saved_df["id"].tolist() == ["u1", "u2", "u3"]