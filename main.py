from flask import Flask
import pyautogui

app = Flask(__name__)

@app.route("/next")
def next_slide():
    pyautogui.press("right")
    return "Next Slide"

@app.route("/prev")
def prev_slide():
    pyautogui.press("left")
    return "Previous Slide"

app.run(host="0.0.0.0", port=5000)