# The responses are in Persian; you can change them.

import os
import telebot
import requests
from Weather_codes import weather_codes

# 🔐 Load token from environment variable (recommended).
# Set it with:  export TELEGRAM_BOT_TOKEN='your_new_token'
# Or for quick testing, replace the line below with your token string directly.
TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', 'PUT_YOUR_NEW_TOKEN_HERE')

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, text='سلام! من یک ربات برای دیدن وضعیت آب و هوای شهر شما هستم.')


def extract_weather_info(data_weather):
    """
    Normalize weather_codes entry into (description, emoji, advice).
    Supports both formats:
      - tuple/list:  (description, emoji, advice)
      - dict:        {'description': ..., 'emoji': ..., 'advice': ...}
    Returns a fallback tuple if data_weather is None or unrecognized.
    """
    fallback = ('نامشخص', '❓', 'توصیه‌ای موجود نیست')

    if data_weather is None:
        return fallback

    if isinstance(data_weather, dict):
        return (
            data_weather.get('description', fallback[0]),
            data_weather.get('emoji', fallback[1]),
            data_weather.get('advice', fallback[2]),
        )

    if isinstance(data_weather, (tuple, list)) and len(data_weather) >= 3:
        return data_weather[0], data_weather[1], data_weather[2]

    return fallback


@bot.message_handler(func=lambda m: True)
def get_info(message):
    city = (message.text or '').strip()
    if not city:
        bot.reply_to(message, text='لطفاً نام شهر را وارد کنید.')
        return

    bot.reply_to(message, text='شهر شما دریافت شد!')

    try:
        # --- 1) Geocoding ---
        response = requests.get(
            'https://geocoding-api.open-meteo.com/v1/search',
            params={
                'name': city.lower(),
                'count': 1,
                'language': 'en',
                'format': 'json'
            },
            timeout=10
        )
        response.raise_for_status()
        data = response.json()

        if 'results' not in data or len(data['results']) == 0:
            bot.reply_to(message, text='شهر شما نا معتبر است!')
            return

        result = data['results'][0]
        latitude = result['latitude']
        longitude = result['longitude']

        # --- 2) Weather ---
        response_weather = requests.get(
            'https://api.open-meteo.com/v1/forecast',
            params={
                'latitude': latitude,
                'longitude': longitude,
                'current': 'temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code'
            },
            timeout=10
        )
        response_weather.raise_for_status()

        # --- 3) Local time ---
        response_time = requests.get(
            'https://timeapi.io/api/v1/time/current/coordinate',
            params={
                'latitude': latitude,
                'longitude': longitude
            },
            timeout=10
        )
        response_time.raise_for_status()
        time_data = response_time.json()

        # --- 4) Parse weather ---
        weather_data = response_weather.json()['current']

        temperature  = weather_data['temperature_2m']
        humidity     = weather_data['relative_humidity_2m']
        wind_speed   = weather_data['wind_speed_10m']
        weather_code = weather_data['weather_code']

        # --- 5) Parse time (handle both snake_case and camelCase keys) ---
        time_value  = time_data.get('time') or time_data.get('dateTime') or ''
        # Take just HH:MM:SS from an ISO string
        time_value  = time_value.split('T')[-1][:8] if 'T' in time_value else time_value[:8]

        date_value  = time_data.get('date') or (
            time_data.get('dateTime', '').split('T')[0] if 'dateTime' in time_data else ''
        )
        day_of_week = (
            time_data.get('day_of_week')
            or time_data.get('dayOfWeek')
            or ''
        )

        # --- 6) Weather description/emoji/advice ---
        data_weather = weather_codes.get(weather_code)
        description, emoji, advice = extract_weather_info(data_weather)

        # --- 7) Build reply ---
        response_to_user = f'''


🌤️ وضعیت آب‌وهوا

شهر : {city.capitalize()}


تاریخ : {date_value} ({day_of_week})


ساعت محلی : {time_value}


دما : {temperature}°C


رطوبت : {humidity}%


سرعت وزش باد : {wind_speed} km/h


وضعیت : {description} {emoji}


توصیه : {advice}


'''
        bot.reply_to(message, response_to_user)

    except requests.exceptions.RequestException:
        bot.reply_to(message, text='خطا در ارتباط با سرور آب و هوا!')

    except (KeyError, IndexError, TypeError) as e:
        # Log to console to help debugging; user sees a friendly message.
        print(f'[parse error] {type(e).__name__}: {e}')
        bot.reply_to(message, text='خطا در پردازش اطلاعات آب و هوا!')


if __name__ == '__main__':
    bot.polling(none_stop=True)