from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>LineTech Newsroom</title>

        <style>
            *{
                margin:0;
                padding:0;
                box-sizing:border-box;
                font-family:Tahoma,sans-serif;
            }

            body{
                background:#0b0b0b;
                color:white;
            }

            .navbar{
                background:#111;
                border-bottom:2px solid #ff0000;
                padding:20px;
                position:sticky;
                top:0;
            }

            .logo{
                font-size:30px;
                font-weight:bold;
                color:#ff0000;
            }

            .categories{
                display:flex;
                gap:10px;
                flex-wrap:wrap;
                margin-top:15px;
            }

            .tag{
                background:#1c1c1c;
                padding:10px 15px;
                border-radius:10px;
                border:1px solid #333;
            }

            .hero{
                text-align:center;
                padding:60px 20px;
            }

            .hero h1{
                font-size:48px;
                margin-bottom:15px;
            }

            .hero p{
                color:#bbb;
            }

            .container{
                max-width:1300px;
                margin:auto;
                padding:20px;
            }

            .grid{
                display:grid;
                grid-template-columns:repeat(auto-fit,minmax(320px,1fr));
                gap:20px;
            }

            .card{
                background:#151515;
                border:1px solid #252525;
                border-radius:15px;
                overflow:hidden;
                transition:.3s;
            }

            .card:hover{
                transform:translateY(-5px);
                border-color:#ff0000;
            }

            .card-header{
                background:#ff0000;
                color:white;
                padding:12px;
                font-weight:bold;
            }

            .card-body{
                padding:20px;
            }

            .title{
                font-size:20px;
                margin-bottom:10px;
            }

            .source{
                color:#999;
                margin-bottom:15px;
            }

            .btn{
                display:inline-block;
                background:#ff0000;
                color:white;
                padding:10px 15px;
                text-decoration:none;
                border-radius:8px;
            }

            .stats{
                display:grid;
                grid-template-columns:repeat(4,1fr);
                gap:15px;
                margin:30px 0;
            }

            .stat{
                background:#151515;
                text-align:center;
                padding:20px;
                border-radius:15px;
            }

            @media(max-width:768px){
                .hero h1{
                    font-size:32px;
                }

                .stats{
                    grid-template-columns:repeat(2,1fr);
                }
            }
        </style>
    </head>

    <body>

        <div class="navbar">
            <div class="logo">🎮 LineTech Newsroom</div>

            <div class="categories">
                <div class="tag">GTA 6</div>
                <div class="tag">Resident Evil</div>
                <div class="tag">Battlefield</div>
                <div class="tag">Call of Duty</div>
                <div class="tag">PlayStation</div>
                <div class="tag">Xbox</div>
            </div>
        </div>

        <div class="hero">
            <h1>غرفة أخبار لاين تك</h1>
            <p>نسخة تجريبية لبناء موظف لاين تك الرقمي</p>
        </div>

        <div class="container">

            <div class="stats">
                <div class="stat">
                    <h2>6</h2>
                    <p>أقسام</p>
                </div>

                <div class="stat">
                    <h2>24/7</h2>
                    <p>مراقبة</p>
                </div>

                <div class="stat">
                    <h2>AI</h2>
                    <p>بكجات</p>
                </div>

                <div class="stat">
                    <h2>∞</h2>
                    <p>أخبار</p>
                </div>
            </div>

            <div class="grid">

                <div class="card">
                    <div class="card-header">🚨 GTA 6</div>

                    <div class="card-body">
                        <div class="title">
                            لم يتم ربط الأخبار بعد
                        </div>

                        <div class="source">
                            Rockstar Games
                        </div>

                        <a class="btn">Generate Package</a>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header">🧟 Resident Evil</div>

                    <div class="card-body">
                        <div class="title">
                            بانتظار ربط أخبار كابكوم
                        </div>

                        <div class="source">
                            Capcom
                        </div>

                        <a class="btn">Generate Package</a>
                    </div>
                </div>

                <div class="card">
                    <div class="card-header">🎖 Battlefield</div>

                    <div class="card-body">
                        <div class="title">
                            بانتظار الأخبار
                        </div>

                        <div class="source">
                            EA
                        </div>

                        <a class="btn">Generate Package</a>
                    </div>
                </div>

            </div>

        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
<hr style="margin:40px 0;border:1px solid #222;">

<h2 style="margin-bottom:20px;">🌍 مصادر الأخبار المرتبطة</h2>

<div class="grid">

    <div class="card">
        <div class="card-header">Rockstar</div>
        <div class="card-body">
            <a href="https://www.rockstargames.com/newswire" target="_blank">
                فتح المصدر
            </a>
        </div>
    </div>

    <div class="card">
        <div class="card-header">Capcom</div>
        <div class="card-body">
            <a href="https://www.capcom-games.com/en-us/" target="_blank">
                فتح المصدر
            </a>
        </div>
    </div>

    <div class="card">
        <div class="card-header">PlayStation Blog</div>
        <div class="card-body">
            <a href="https://blog.playstation.com/" target="_blank">
                فتح المصدر
            </a>
        </div>
    </div>

    <div class="card">
        <div class="card-header">Xbox Wire</div>
        <div class="card-body">
            <a href="https://news.xbox.com/" target="_blank">
                فتح المصدر
            </a>
        </div>
    </div>

    <div class="card">
        <div class="card-header">Battlefield</div>
        <div class="card-body">
            <a href="https://www.ea.com/games/battlefield/news" target="_blank">
                فتح المصدر
            </a>
        </div>
    </div>

    <div class="card">
        <div class="card-header">Call of Duty Blog</div>
        <div class="card-body">
            <a href="https://www.callofduty.com/blog" target="_blank">
                فتح المصدر
            </a>
        </div>
    </div>

</div>

<hr style="margin:40px 0;border:1px solid #222;">

<h2>📦 توليد البكج الكامل</h2>

<textarea
style="
width:100%;
height:200px;
background:#151515;
color:white;
border:1px solid #333;
padding:15px;
margin-top:10px;
border-radius:10px;
"
placeholder="سيظهر البكج هنا لاحقاً...">
</textarea>

<br><br>

<button
style="
background:#ff0000;
color:white;
padding:12px 20px;
border:none;
border-radius:10px;
cursor:pointer;
">
Generate Package
</button>

<hr style="margin:40px 0;border:1px solid #222;">

<h2>🖼️ برومبت الثمنيل</h2>

<textarea
style="
width:100%;
height:150px;
background:#151515;
color:white;
border:1px solid #333;
padding:15px;
margin-top:10px;
border-radius:10px;
"
placeholder="سيظهر برومبت الثمنيل هنا لاحقاً...">
</textarea>

<br><br>

<button
style="
background:#222;
color:white;
padding:12px 20px;
border:none;
border-radius:10px;
cursor:pointer;
">
Generate Thumbnail Prompt
</button>
