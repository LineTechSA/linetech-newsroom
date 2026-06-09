from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🎮 LineTech Newsroom</h1>

    <h2>🚨 GTA 6 Tracker</h2>
    <p>قريباً سيتم جلب أخبار Rockstar تلقائياً.</p>

    <h2>🧟 Resident Evil News</h2>
    <p>قريباً سيتم جلب أخبار Capcom تلقائياً.</p>

    <h2>🎖️ Battlefield</h2>
    <p>قريباً...</p>

    <h2>🎮 Call of Duty</h2>
    <p>قريباً...</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
