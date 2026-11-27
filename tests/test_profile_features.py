from src.profile_features import extract_profile_features


def test_complete_profile():
    user = {
        "id": "u1",
        "public_metrics": {
            "followers_count": 100,
            "following_count": 50,
            "tweet_count": 20,
            "listed_count": 2
        }
    }

    result = extract_profile_features(user)

    assert result["tweet_count"] == 20

def test_null_metrics():
    user = {
        "id": "u2",
        "public_metrics": None
    }

    result = extract_profile_features(user)

    assert result["followers_count"] is None
    assert result["following_count"] is None


def test_partial_metrics():
    user = {
        "id": "u3",
        "public_metrics": {
            "followers_count": 30
        }
    }

    result = extract_profile_features(user)

    assert result["followers_count"] == 30
    assert result["following_count"] is None