# 🌤️ Persian Weather Telegram Bot

A simple Persian Telegram bot built with Python that receives a city name and provides current weather information for that city.

The bot uses Open-Meteo for city geocoding and weather data and presents the results in Persian.

---

## ✨ Features

- 🌍 Search for cities by name
- 🌡️ Current temperature
- 💧 Current humidity
- 💨 Wind speed
- 🌤️ Current weather condition
- 📅 Local date
- 🕐 Local time
- 🗓️ Day of the week
- 😊 Persian weather descriptions
- 💡 Weather recommendations
- 🌦️ Weather emojis based on weather conditions
- ⚠️ Basic error handling
- 🔐 Secure token loading through environment variables

---

## 🏗️ Project Architecture

The bot follows this general workflow:

```text
Telegram User
      ↓
   City Name
      ↓
Open-Meteo Geocoding API
      ↓
 Latitude + Longitude
      ↓
Open-Meteo Forecast API
      ↓
 Current Weather Data
      ↓
Time API
      ↓
Local Date & Time
      ↓
Weather Code Dictionary
      ↓
Persian Weather Response
      ↓
   Telegram User
```

---

## 🛠️ Technologies

- Python
- pyTelegramBotAPI
- Requests
- Open-Meteo API
- TimeAPI
- Git
- GitHub

---

## 📁 Project Structure

```text
Telegram-Weather-Bot/
│
├── main.py
├── Weather_codes.py
├── README.md
├── LICENSE
└── .gitignore
```

### `main.py`

Contains the main Telegram bot logic, API requests, data processing, error handling, and response generation.

### `Weather_codes.py`

Contains the weather code dictionary based on Open-Meteo weather codes.

Each weather code contains:

```python
{
    "description": "...",
    "emoji": "...",
    "advice": "..."
}
```

For example:

```python
weather_codes = {
    0: {
        "description": "آسمان صاف",
        "emoji": "☀️",
        "advice": "هوا برای فعالیت‌های فضای باز مناسب است."
    },

    63: {
        "description": "باران متوسط",
        "emoji": "🌧️",
        "advice": "بهتر است چتر همراه داشته باشید."
    }
}
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/0xhijazy/Telegram-Weather-Bot.git
```

### 2. Go to the project directory

```bash
cd Telegram-Weather-Bot
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

On Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install pyTelegramBotAPI requests
```

---

## 🔐 Telegram Bot Token

Create a Telegram bot using `@BotFather` and get your bot token.

The bot loads the token from an environment variable:

```python
TOKEN = os.environ.get(
    'TELEGRAM_BOT_TOKEN',
    'PUT_YOUR_NEW_TOKEN_HERE'
)
```

### Windows PowerShell

Set the environment variable:

```powershell
$env:TELEGRAM_BOT_TOKEN="YOUR_BOT_TOKEN"
```

Then run the bot:

```bash
python main.py
```

> ⚠️ Never publish your real Telegram bot token on GitHub.

If a token is accidentally exposed, revoke it immediately through `@BotFather` and generate a new one.

---

## 🌦️ Weather Codes

The bot uses the `weather_code` returned by Open-Meteo.

These codes are converted into Persian descriptions, emojis, and recommendations using `Weather_codes.py`.

Example:

```python
weather_code = 63

weather = weather_codes.get(weather_code)
```

The result contains:

```python
weather["description"]
weather["emoji"]
weather["advice"]
```

Which can produce a user-friendly response such as:

```text
🌧️ وضعیت: باران متوسط

💡 توصیه:
بهتر است چتر همراه داشته باشید.
```

---

## 💬 Example Response

```text
🌤️ وضعیت آب‌وهوا

شهر : Zanjan

تاریخ : 2026-09-15 (Tuesday)

ساعت محلی : 16:30:00

دما : 18°C

رطوبت : 45%

سرعت وزش باد : 12 km/h

وضعیت : آسمان صاف ☀️

توصیه : هوا برای فعالیت‌های فضای باز مناسب است.
```

---

## 🌐 APIs

### Open-Meteo

Used for:

- City geocoding
- Latitude and longitude
- Current weather
- Temperature
- Humidity
- Wind speed
- Weather codes

### TimeAPI

Used for:

- Local time
- Local date
- Day of the week

---

## 🧪 Current Project Status

The core functionality of the bot has been implemented and tested.

Current workflow:

```text
Receive city
      ↓
Find city coordinates
      ↓
Get current weather
      ↓
Get local time
      ↓
Interpret weather code
      ↓
Generate Persian response
      ↓
Send response to user
```

---

## 🔮 Future Improvements

Possible future features:

- 🏙️ More detailed city information
- 🏃 Running suitability
- 🚴 Cycling suitability
- 🚶 Walking suitability
- 👕 Clothing recommendations
- ☔ Better rain analysis
- 🌡️ Temperature-based recommendations
- 🗺️ More location information
- 🔘 Telegram buttons
- 🧹 Improved project structure
- ⚙️ More advanced error handling
- 🔐 `.env` configuration
- 🗄️ Database integration

---

## 🎯 Project Goal

The main goal of this project is to build a practical Python application while learning how to work with:

- APIs
- HTTP requests
- JSON data
- Data processing
- Python functions
- Error handling
- Environment variables
- Telegram bots
- Git & GitHub

The project is being developed step by step, starting with the core functionality and gradually improving its structure, usability, and features.

---

## 📜 License

This project is licensed under the MIT License.


---

## 🦁☀️ Persian Weather Bot

Built with Python and Open-Meteo.