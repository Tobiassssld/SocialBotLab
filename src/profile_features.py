def extract_profile_features(user):
    user_feature = {}

    user_feature["id"] = user["id"]

    metrics = user.get("public_metrics")

    if metrics is None:
        metrics = {}

    user_feature["followers_count"] = metrics.get("followers_count")
    user_feature["following_count"] = metrics.get("following_count")
    user_feature["tweet_count"] = metrics.get("tweet_count")
    user_feature["listed_count"] = metrics.get("listed_count")

    return user_feature