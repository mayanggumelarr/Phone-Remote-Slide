from flask import Flask
import pyautogui

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
    <title>Slide Remote</title>
    <style>
        body{
            background:#111;
            display:flex;
            flex-direction:column;
            justify-content:center;
            align-items:center;
            height:100vh;
            margin:0;
            font-family:Arial;
        }

        button{
            width:80%;
            height:120px;
            font-size:40px;
            margin:20px;
            border:none;
            border-radius:20px;
            color:white;
        }

        .next{
            background:#28a745;
        }

        .prev{
            background:#dc3545;
        }

        .exit{
            background:#8a7650;
        }
    </style>
    </head>

    <body>
        <button class="next" onclick="fetch('/next')">NEXT ▶</button>
        <button class="prev" onclick="fetch('/prev')">◀ PREV</button>
        <button class="exit" onclick="fetch('/exit')">EXIT</button>
    </body>
    </html>
    """

@app.route("/next")
def next_slide():
    pyautogui.press("right")
    return "OK"

@app.route("/prev")
def prev_slide():
    pyautogui.press("left")
    return "OK"

@app.route("/exit")
def exit_slide():
    pyautogui.press("esc")
    return "EXIT"

app.run(host="0.0.0.0", port=5000)