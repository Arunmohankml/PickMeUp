# PickMeUp — Auto Booking Web App

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-5.0-green)
![WebSocket](https://img.shields.io/badge/Realtime-WebSocket-orange)
![Mobile-Optimized](https://img.shields.io/badge/Mobile-First-blueviolet)
![Made-in-Browser](https://img.shields.io/badge/Built%20in-Browser-black)
![License](https://img.shields.io/badge/License-MIT-yellow)

# (NOT COMPLETELY FINISHED)
**PickMeUp** is a fully functional auto-rickshaw booking platform built using Django, Channels (for WebSocket real-time features), Leaflet.js (for maps), and a clean mobile-first UI.

This project was developed entirely within a browser-based environment (Glitch + GitHub Codespaces), without using a physical PC or external IDE. It is optimized for mobile screens and designed to provide a seamless experience for both users and drivers.

---

## 🚀 Features

- **Real-Time Ride Tracking**  
  Drivers' live location is sent via WebSocket and displayed to the user on a Leaflet map.

- **User & Driver Authentication**  
  Clean registration and login flow for both users and drivers, with role-based dashboard redirection.

- **Auto Discovery & Booking**  
  Users can see available drivers, check fares, and request rides based on live coordinates.

- **Live Driver Info**  
  Driver name, bio, vehicle info, and profile image are shown during active rides.

- **Secure Ride Cancellation**  
  Built-in OTP and cancellation logic with CSRF protection for POST operations.

- **Driver Side Interface**  
  Drivers can accept rides, send location updates, and view passenger details.

- **Modern UI**  
  Professional, responsive, and clean interface inspired by platforms like Tukxi — designed for usability and clarity.

---

## ⚙️ Tech Stack

- **Backend:** Django 5, Channels 4  
- **Frontend:** HTML, CSS, JavaScript, Leaflet.js  
- **WebSocket Server:** Uvicorn (ASGI)  
- **Static Files & Media:** Served via Django’s default setup  
- **Image Handling:** Pillow

---

## 📂 Folder Structure

```bash
autoapp/
├── autoapp/        # Django project settings
├── home/           # App for user-facing pages
├── driver/         # App for driver dashboard and WebSocket handling
├── templates/      # HTML templates
├── static/         # Static files (CSS, JS)
├── asgi.py         # WebSocket routing via Channels
└── routing.py      # URL router for Channels
```


---

✅ Installation (for development)

# Install dependencies
```pip install -r requirements.txt```

# Run migrations
```
python3 manage.py makemigrations
python3 manage.py migrate
```

# Start ASGI server (WebSocket + HTTP)
```uvicorn autoapp.asgi:application --host 0.0.0.0 --port 8000```

> 📝 Ensure you are using Python 3.11+ and have uvicorn, channels, and Django installed properly.




---

📱 Best Viewed On

This app is mobile-first and is best experienced on a smartphone browser. While it works on desktops, the layout, fonts, and interactions are tailored for mobile screens.


---

👤 Author

Arun Mohan
Made entirely inside a browser using Glitch,GitHub Codespace and Acode — without a PC in mobile phone.

From Kerala, India 🇮🇳


---

📜 License

This project is open-source and free to use for learning or personal experimentation. Attribution is appreciated.


---


Feel free contribute to this project.
