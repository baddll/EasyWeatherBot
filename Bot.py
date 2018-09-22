# -*- coding: utf-8 with BOM -*-
import telebot
import requests
import time

appid = "token_OWMAPI" #Коды городов можно найти на сайте https://openweathermap.org/
token = 'telegram_bot_token' 
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def handle_start_help(message):
    bot.send_message(message.chat.id, 'Привет! Я бот погоды!\nЧтобы узнать текущую погоду, '
                                            'введите команду /now')

@bot.message_handler(commands=['now'])
def Choose_user_city(message):

    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                       params={'id': 498817, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()

    A = ("Погода в Санкт-Петербурге:\n"
        + "\n\nЗа окном: " + str(data['weather'][0]['description'])
        + "\nТемпература: " + str(data['main']['temp'])
        + " °C"+ "\nMin: " + str(data['main']['temp'])
        + " °C"+ "\nMax: " + str(data['main']['temp']) + " °C\n"
        + "\nДавление: " + str(data['main']['pressure']) + " hPa"
        + "\nВлажность: " + str(data['main']['humidity']) + "%"
        + "\nВетер: " + str(data['wind']['speed']) + " М/c"
        + "\nНаправление ветра: " + str(data['wind']['deg']) + "°"
        + "\nОблачность: " + str(data['clouds']['all']) + "%\n"
        + 'Время восхода: '
        + time.strftime("%H:%M:%S", time.localtime(float(data['sys']['sunrise'])))
        + '\nВремя заката: '
        + time.strftime("%H:%M:%S", time.localtime(float(data['sys']['sunset'])))
        + '\n')
    bot.send_message(message.chat.id, A)

while True:
    try:
        bot.polling(none_stop=True, timeout=3.5)
    except:
        print('restart')
        time.sleep(10)
