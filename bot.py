# import telebot

# bot = telebot.TeleBot("5194006532:AAHfEHyU_Kqlnu7LZwfGQNbgcl1UgM_UeLA", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")

# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)



# bot.infinity_polling()
import telebot
import requests
import json
import datetime


token='5194006532:AAHfEHyU_Kqlnu7LZwfGQNbgcl1UgM_UeLA'
bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.chat.id, "Hello, I am WeatherBot, Text me City name")

@bot.message_handler(content_types='text')
def send_data(message):
    API_key = '0960bae1e05a229c452ab6eae80debcb'
    city = message.text.title()
    API = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_key}'
    data = requests.get(API).json()
    coord = data['main']['temp']
    flike = data['main']['feels_like']
    min_temp = data['main']['temp_min']
    max_temp = data['main']['temp_max']
    bot.send_message(message.chat.id, f"Temperature:{coord} \n Feels like:{flike}")
        
        
bot.infinity_polling()
# @Martankg_bot this bot name on telegram