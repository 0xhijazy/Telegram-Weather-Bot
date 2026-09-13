# 🌤️ Telegram Weather Bot

A simple Telegram bot built with Python that receives a city name and provides
current weather information using the Open-Meteo API.

> 🚧 This project is currently under development and new features will be added.

## ✨ Features

- 📍 Get the coordinates of a city using its name
- 🌡️ Get current temperature
- 💧 Get relative humidity
- 💨 Get wind speed
- 🕐 Display the current weather data time
- ❌ Handle invalid city names
- 🌐 Uses Open-Meteo APIs
-  Persian responses

## 🛠️ Technologies

- Python
- pyTelegramBotAPI (Telebot)
- Requests
- Open-Meteo API
- Telegram Bot API

## 🔄 How It Works

The bot follows this process:

```text
User
  ↓
Enter city name
  ↓
Geocoding API
  ↓
Latitude & Longitude
  ↓
Weather API
  ↓
Weather Data
  ↓
Persian Response
