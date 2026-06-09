from flask import Flask, render_template

from services.resident_evil.pre_ar import get_pre_ar_news
from ai.package_generator import generate_package

app = Flask(__name__)

@app.route("/")
def home():

    news = get_pre_ar_news()

    return render_template(
        "index.html",
        resident_evil_news=news
    )

@app.route("/generate")
def generate():

    result = generate_package(
        "كشف الستار عن خفايا عرض Resident Evil Requiem!"
    )

    return f"""
    <h1>📦 Gemini Package</h1>

    <pre style="
    white-space:pre-wrap;
    font-size:18px;
    padding:20px;
    ">
    {result}
    </pre>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
