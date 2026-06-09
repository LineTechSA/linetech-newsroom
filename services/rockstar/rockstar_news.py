import requests
from bs4 import BeautifulSoup

def get_rockstar_news():

    try:

        url = "https://www.rockstargames.com/newswire"

        response = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=10
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        latest_articles = []

        for link in soup.find_all("a"):

            title = link.get_text(strip=True)
            href = link.get("href")

            if title and len(title) > 20:

                if href and href.startswith("/"):
                    href = "https://www.rockstargames.com" + href

                latest_articles.append({
                    "title": title,
                    "url": href
                })

        return latest_articles[:5]

    except Exception as e:

        return [{
            "title": f"Rockstar Error: {e}",
            "url": "#"
        }]
