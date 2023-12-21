# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 18:28:39 2023

@author: olimovdev
"""
import telebot

bot = telebot.TeleBot("6752512084:AAGlK6S3ywO3a-f3P7K_V1dR8lkhIPlo7Jw", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

from t import to_cyrillic, to_latin

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Sizga qanday yordam bera olaman?")
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    myText = message.text
    if myText.isascii():
        myText = to_cyrillic(message.text)
    else:
        myText = to_latin(message.text)
    bot.reply_to(message, myText)
    
bot.infinity_polling()