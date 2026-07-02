from app.catalog import load_catalog


def recommend(user_query: str):

    catalog = load_catalog()
    user_query = user_query.lower().strip()

    scored_results = []

    query_words = set(user_query.split())

    for item in catalog:

        score = 0

        name = item.get("name", "").lower()
        description = item.get("description", "").lower()
        keys = [k.lower() for k in item.get("keys", [])]
        job_levels = [j.lower() for j in item.get("job_levels", [])]

        # Exact match gets highest priority
        if user_query in name:
            score += 20

        # Match individual words
        for word in query_words:

            if len(word) < 3:
                continue

            if word in name:
                score += 10

            if word in description:
                score += 5

            for key in keys:
                if word in key:
                    score += 4

            for level in job_levels:
                if word in level:
                    score += 2

        if score > 0:
            scored_results.append((score, item))

    scored_results.sort(key=lambda x: x[0], reverse=True)

    recommendations = []

    for score, item in scored_results[:10]:
        recommendations.append(
            {
                "name": item["name"],
                "url": item["link"],
                "test_type": ", ".join(item.get("keys", []))
            }
        )

    # Fallback if nothing matched
    if not recommendations:
        for item in catalog[:5]:
            recommendations.append(
                {
                    "name": item["name"],
                    "url": item["link"],
                    "test_type": ", ".join(item.get("keys", []))
                }
            )

    return recommendations