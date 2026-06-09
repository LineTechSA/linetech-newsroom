from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def home():
    try:
        url = "https://www.rockstargames.com/newswire"
        response = requests.get(url, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        title = "تعذر جلب الخبر"

        h2 = soup.find("h2")
        if h2:
            title = h2.get_text(strip=True)

        return f"""
        <h1>🎮 LineTech Newsroom</h1>

        <h2>🚨 آخر خبر من Rockstar</h2>
        <p>{title}</p>

        <hr>

        <h2>🧟 Resident Evil</h2>
        <p>قريباً...</p>
        """

    except Exception as e:
        return f"<h1>خطأ</h1><p>{e}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
