from ddgs import DDGS


def search_web(query):

    results = []

    try:

        search_results = DDGS().text(
            query,
            max_results=5
        )

        for result in search_results:

            results.append({
                "title": result.get("title", ""),
                "url": result.get("href", ""),
                "snippet": result.get("body", "")
            })

    except Exception as e:

        print("Web search error:", e)

    return results
