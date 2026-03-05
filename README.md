# 📱 Python Phone Remote for PowerPoint

Turn your smartphone into a simple remote controller for PowerPoint presentations using Python and Flask.

This project allows you to control presentation slides (Next, Previous, and Exit) directly from your phone through a web interface connected to your laptop on the same network.

---

## ✨ Features

* ▶ **Next Slide**
* ◀ **Previous Slide**
* ⛔ **Exit Slide Show**
* 📱 Mobile-friendly web interface
* ⚡ Very low latency (local network)
* 🧠 Simple Python implementation

---

## 🖥️ How It Works

The phone accesses a small web server running on your laptop.
When a button is pressed on the phone, the server sends a keyboard command to PowerPoint using `pyautogui`.

```
Phone Browser
      ↓
Flask Web Server (Laptop)
      ↓
pyautogui
      ↓
PowerPoint Slide Control
```

---

## 📦 Requirements

Install the required Python libraries:

```bash
pip install flask pyautogui
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/python-phone-slide-remote.git
cd python-phone-slide-remote
```

### 2. Run the Python server

```bash
python main.py
```

You will see something like:

```
Running on http://127.0.0.1:5000
Running on http://192.168.x.x:5000
```

### 3. Open the remote on your phone

Make sure your **phone and laptop are on the same WiFi network**.

Open your phone browser and visit:

```
http://YOUR_LAPTOP_IP:5000
```

Example:

```
http://192.168.1.5:5000
```

---

## 🎮 Controls

| Button | Function               |
| ------ | ---------------------- |
| ▶ NEXT | Move to next slide     |
| ◀ PREV | Move to previous slide |
| ⛔ EXIT | Exit slide show        |

---

## ⚠️ Important Notes

* PowerPoint must be **open and active** on your laptop.
* The laptop and phone must be on the **same network**.
* This project works best when PowerPoint is in **Slide Show mode**.

---

## 💡 Possible Improvements

Future ideas for this project:

* Swipe gesture control
* Presentation timer on phone
* Vibrate feedback on button press
* Laser pointer simulation
* Voice command (e.g. "Next Slide")

---

## 🧑‍💻 Built With

* Python
* Flask
* PyAutoGUI
* HTML & CSS

---

## 📜 License

This project is open-source and available under the MIT License.

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!
