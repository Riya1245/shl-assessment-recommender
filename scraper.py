import json
import requests
from bs4 import BeautifulSoup


BASE_URL = "https://www.shl.com"


def scrape_catalog():

    url = "https://www.shl.com/solutions/products/product-catalog/"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    assessments = []

    links = soup.find_all("a", href=True)

    for link in links:

        href = link["href"]
        name = link.get_text(strip=True)

        if "/products/" in href and name:

            if not href.startswith("http"):
                href = BASE_URL + href

            assessments.append({
                "name": name,
                "url": href
            })

    unique = []

    seen = set()

    for item in assessments:

        if item["url"] not in seen:

            unique.append(item)

            seen.add(item["url"])

    with open("data/catalog.json", "w", encoding="utf-8") as f:

        json.dump(unique, f, indent=4)

    print(f"Saved {len(unique)} assessments")


if __name__ == "__main__":
    scrape_catalog()