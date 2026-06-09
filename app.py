from flask import Flask, render_template

from services.resident_evil.pre_ar import get_pre_ar_news
from services.rockstar.rockstar_news import get_rockstar_news

app = Flask(__name__)

@app.route("/")
def home():

    resident_news = get_pre_ar_news()
    rockstar_news = get_rockstar_news()

    return render_template(
        "index.html",
        resident_evil_news=resident_news,
        rockstar_news=rockstar_news
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
