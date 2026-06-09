import requests
from bs4 import BeautifulSoup

def get_resident_evil_news():

    try:
        url = "https://www.residentevil.com/"

        response = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=10
        )

        soup = BeautifulSoup(response.text, "html.parser")

        title = "لا يوجد خبر حالياً"

        h1 = soup.find("h1")

        if h1:
            title = h1.get_text(strip=True)

        return {
            "title": title
        }

    except Exception as e:

        return {
            "title": f"خطأ: {str(e)}"
        }
