from flask import Flask, render_template
from services.resident_evil.pre_ar import get_pre_ar_news

app = Flask(__name__)

@app.route("/")
def home():

    news = get_pre_ar_news()

    return render_template(
        "index.html",
        resident_evil_news=news
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
