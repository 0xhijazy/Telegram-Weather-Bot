# The responses are in Persian; you can change them.



import telebot
import requests

TOKEN = 'TOKEN'  # Put your token here. You can get a token in @botfather

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, text='سلام! من یک ربات برای دیدن وضعیت آب و هوای شهر شما هستم.')

@bot.message_handler(func=lambda m: True)
def get_info(message):
    city = message.text
    bot.reply_to(message, text='شهر شما دریافت شد!')

    try:
        response = requests.get(
            'https://geocoding-api.open-meteo.com/v1/search',
            params={
                'name': city.lower(),
                'count': 1,
                'language': 'en',
                'format': 'json'
            }
        )

        data = response.json()

        
        if 'results' not in data or len(data['results']) == 0:
            bot.reply_to(message, text='شهر شما نا معتبر است!')
            return

        result = data['results'][0]
        latitude = result['latitude']
        longitude = result['longitude']

        response_weather = requests.get(
            'https://api.open-meteo.com/v1/forecast',
            params={
                'latitude': latitude,
                'longitude': longitude,
                'current': 'temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code'
            }
        )

        weather_data = response_weather.json()['current']

        time = weather_data['time']
        time = time[:10]
        temperature = weather_data['temperature_2m']
        humidity = weather_data['relative_humidity_2m']
        wind_speed = weather_data['wind_speed_10m']

        response_to_user = f'''
اطلاعات شهر شما

زمان = {time}

دما = {temperature} سانتی گراد

رطوبت نسبی = {humidity} درصد

سرعت وزش باد = {wind_speed} کیلومتر بر ساعت
'''
        bot.reply_to(message, response_to_user)

    except (KeyError, IndexError, TypeError, UnboundLocalError):
        bot.reply_to(message, text='شهر شما نا معتبر است!')
    except requests.exceptions.RequestException:
        bot.reply_to(message, text='خطا در ارتباط با سرور آب و هوا!')

bot.infinity_polling()