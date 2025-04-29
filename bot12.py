# 1 - install library supported
import telebot
from telebot import types  # 2 - import module

import os
from dotenv import load_dotenv, find_dotenv  # 2 - import modules
import math
import os
import random
import requests
import datetime
import wikipedia, re


load_dotenv(find_dotenv())
                                 # 2 - writting TOKEN for telebot using lib getenv
bot = telebot.TeleBot(os.getenv("TOKEN"))

                                 # 3 -writting handler start
@bot.message_handler(commands=["start"])
def start(message): # 3 -writting def start with params
    markup = types.ReplyKeyboardMarkup(   # 4 -create class Keyboard
        resize_keyboard=True, input_field_placeholder="Выбери пункт меню 🤖"
    )
    # 4 -writting btn - Keyboard 
    btn1 = types.KeyboardButton("Привет пользователь 👋")
    btn13 = types.KeyboardButton(" Wikipedia  📚📰📖")
    btn2 = types.KeyboardButton("Задайте вопрос боту ❓")
    btn3 = types.KeyboardButton("📺📽 Просмотр видео")
    btn4 = types.KeyboardButton("🌎 Прогноз погоды")
    btn5 = types.KeyboardButton("🌟 Астропрогноз")
    btn6 = types.KeyboardButton("💵📈 Курс валют")
    btn7 = types.KeyboardButton("🎙🎚 Прослушивание музыки")
    btn8 = types.KeyboardButton(
        text=" 🏙 Местоположение пользователя", request_location=True
    )
    btn9 = types.KeyboardButton(text="Запрос номера телефона ☎️", request_contact=True)
    btn14 = types.KeyboardButton(text="Опрос по оценки бота ⁉️❤️❤️❤️")
    btn10 = types.KeyboardButton(text="Новостной сайт🖥⌨️💻 ")
    btn11 = types.KeyboardButton(text="Калькулятор 💻⌨️ ")
    btn12 = types.KeyboardButton(text="👩‍⚕️💂‍♂️👩‍✈️👨‍❤️‍👨Сайты для общения")
    btn15 = types.KeyboardButton(text="Курсы биткоинов ₿")
    markup.add(btn1).row(btn2, btn13).row(btn3, btn7).row(btn4, btn5).row(
        btn6, btn11, btn15
    ).row(btn8, btn9).row(btn10, btn12).row(btn14)   # 4 -location btn kbds
    nowdate = datetime.datetime.now().strftime("%d./%m./%Y, %H:%M:%S") # 5 -get variable nowdate using class datetime
    bot.send_message(   # 6 - using method send_message
        message.chat.id,
        text="Привет,  {0.first_name} {0.last_name} с ником {0.username}   {0.language_code}!!! Я информационно-поисквой  бот для поиска последних новостей,прогноза погоды, курс биржи, астропроноз".format(
            message.from_user
        ),  # 7 -write hello message using  method format
        reply_markup=markup,# 8 -passing params (reply_markup) = assign  variable
    )

    bot.send_dice(message.chat.id, "🎯") # 9 - send dice
    bot.send_photo(
        message.chat.id,
        "https://sun9-72.userapi.com/DUf3yKfMEjJiC4CNl6ex_8gnWeSUr6t62xW4mA/H4-lHOfTjEg.jpg",
    ) # 9 - send photo

                           # 10 -writting handler text
@bot.message_handler(content_types=["text"])
def func(message):  # 10 -writting def
    if message.text == "Привет пользователь 👋":  # 11 -writting cycle if elif
        bot.send_dice(message.chat.id, "🎯")
        bot.send_message(
            message.chat.id,
            text="Привет.. Спасибо что общаешься со мной, чем я могу помочь тебе!)",
        )
    elif message.text == "Задайте вопрос боту ❓":
        markup = types.ReplyKeyboardMarkup(
            resize_keyboard=True,
            input_field_placeholder="Выбери свой вопрос",
            row_width=2,
        )                  # 12 -writting btn question
        btn1 = types.KeyboardButton("Как тебя зовут?")
        btn2 = types.KeyboardButton("Что ты можешь?")
        btn10 = types.KeyboardButton("А сколько тебе лет?")
        btn3 = types.KeyboardButton("Чем ты занимаешься?")
        btn4 = types.KeyboardButton("Как твои дела?")
        btn5 = types.KeyboardButton("Что ты можешь мне найти?")
        btn6 = types.KeyboardButton("Ты можешь мне сказать сколько сейчас времени?")
        btn7 = types.KeyboardButton("Хотелось бы узнать, какие твои любимые блюда?")
        btn8 = types.KeyboardButton(
            "А ты можешь мне рассказать о путешествиях  и показать их?"
        )
        btn9 = types.KeyboardButton("А в каком городе ты живешь?")
        btn11 = types.KeyboardButton("А какая музыка тебе нравится?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2).row(btn3, btn4).add(btn5, btn9).row(btn7).row(btn8).row(
            btn6
        ).row(btn10, btn11).row(back)
        bot.send_message(
            message.chat.id, text="Задай мне свой вопрос", reply_markup=markup
        )
    elif message.text == "А какая музыка тебе нравится?":
        markup = types.ReplyKeyboardMarkup(
            resize_keyboard=True,
            input_field_placeholder="Выбери песню 𝄞⨾𓍢ִ໋",
            row_width=2,
        )                                  # 13 -writting btn music
        btn1 = types.KeyboardButton("Русские певцы 𝄞⨾𓍢ִ໋")
        btn2 = types.KeyboardButton("Американские певцы 𝄞⨾𓍢ִ໋")
        btn3 = types.KeyboardButton("Европейские певцы 𝄞⨾𓍢ִ໋")
        btn4 = types.KeyboardButton("Любимые певцы𝄞⨾𓍢ִ໋ ")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, back)
        bot.send_message(
            message.chat.id,
            text="🎙😀 Посмотри некоторых любимых певцов 𝄞⨾𓍢ִ໋",
            reply_markup=markup,
        )
    elif message.text == "🌟 Астропрогноз":
        markup = types.ReplyKeyboardMarkup(
            resize_keyboard=True, input_field_placeholder=" Знаки зодиака ♈️♉️♊️♎️"
        )                                 # 14 -writting btn zodiac
        btn0 = types.KeyboardButton("Знак зодиака ♈️♉️♊️♎️ по 🥳 дате рождения  ❓❓❓")
        btn1 = types.KeyboardButton("♑ Козерог ♑")
        btn2 = types.KeyboardButton("♓ Рыбы ♓")
        btn3 = types.KeyboardButton("♒ Водолей ♒")
        btn4 = types.KeyboardButton("♈ Овен ♈")
        btn5 = types.KeyboardButton("♋ Рак ♋")
        btn6 = types.KeyboardButton("♌ Лев ♌")
        btn7 = types.KeyboardButton("♍ Дева ♍")
        btn8 = types.KeyboardButton("♎ Весы ♎")
        btn9 = types.KeyboardButton("♐ Стрелец ♐")
        btn10 = types.KeyboardButton("♊ Близнецы ♊")
        btn11 = types.KeyboardButton("♉ Телец ♉")
        btn12 = types.KeyboardButton("♏ Скорпион ♏")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn0).row(btn1, btn2).row(btn3, btn4).row(btn5, btn6).row(
            btn7, btn8
        ).row(btn9, btn10).row(btn11, btn12).add(back)
        bot.send_message(
            message.chat.id,
            text="Привет, 😎  {0.first_name} {0.last_name} с ником {0.username} \ Пожалуйста нажми на свой знак зодиака ♊️♉️♈️♋️♌️♍️♎️♏️♐️♑️♒️♓️ и узнаешь гороскоп на сегодня. Если ты не знаешь свой зодиака? Мы тебе поможем. Нажми на кнопку = Знак зодиака по дате рождения ❓❓❓ и введи день и месяц твоего рождения".format(
                message.from_user
            ),
            reply_markup=markup,
        )
    elif message.text == "Опрос по оценки бота ⁉️❤️❤️❤️":
        markup = types.ReplyKeyboardMarkup(
            resize_keyboard=True,
            input_field_placeholder="Оцените моего бота",
            row_width=3,
        )                                   # 14 -writting btn survey
        btn1 = types.KeyboardButton("5️⃣❤️❤️❤️")
        btn2 = types.KeyboardButton("4️⃣💝💘💖")
        btn3 = types.KeyboardButton("3️⃣💞💗❓")
        btn4 = types.KeyboardButton("2️⃣🛑⭕️❌")
        btn6 = types.KeyboardButton("1️⃣💔💔🖤")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2).row(btn3, btn4, btn6).row(back)
        bot.send_message(
            message.chat.id,
            text="Привет!!! Оцени моего бота по 5️⃣ балльной шкале, где 5️⃣ это отлично, а - 1️⃣ ужасно )",
            reply_markup=markup,
        )
    elif message.text == "3️⃣💞💗❓":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="Спасибо😎")
        bot.send_dice(message.chat.id, "🎯")
    elif message.text == "1️⃣💔💔🖤":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="Очень Жаль 👎😲")
        bot.send_dice(message.chat.id, "🏀")
    elif message.text == "4️⃣💝💘💖":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="Я очень рад этому.🤚😀")
        bot.send_dice(message.chat.id, "⚽")
    elif message.text == "2️⃣🛑⭕️❌":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="Хорошо.Буду стараться делать лучше!!😞")
        bot.send_dice(message.chat.id, "🎳")
    elif message.text == "5️⃣❤️❤️❤️":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="Ок. ❤️🤟👌")
        bot.send_dice(message.chat.id, "🎰")
    elif message.text == "♑ Козерог ♑":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(
            message.chat.id,
            text="Нажми на ссылку https://horo.mail.ru/prediction/capricorn/today/ )",
        )
    elif message.text == "♓ Рыбы ♓":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(
            message.chat.id,
            text="Нажми на ссылку https://horo.mail.ru/prediction/pisces/today/ )",
        )
    elif message.text == "♒ Водолей ♒":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(
            message.chat.id,
            text="Нажми на ссылку https://horo.mail.ru/prediction/aquarius/today/ )",
        )
    elif message.text == "♈ Овен ♈":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(
            message.chat.id,
            text="Нажми на ссылку https://horo.mail.ru/prediction/aries/today/ )",
        )
    elif message.text == "♋ Рак ♋":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(
            message.chat.id,
            text="Нажми на ссылку https://horo.mail.ru/prediction/cancer/today/ )",
        )
    elif message.text == "♌ Лев ♌":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(
            message.chat.id,
            text="Нажми на ссылку https://horo.mail.ru/prediction/leo/today/ )",
        )
    elif message.text == "♍ Дева ♍":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(
            message.chat.id,
            text="Нажми на ссылку https://horo.mail.ru/prediction/virgo/today/ )",
        )
    elif message.text == "♎ Весы ♎":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(
            message.chat.id,
            text="Нажми на ссылку https://horo.mail.ru/prediction/libra/today/ )",
        )
    elif message.text == "♐ Стрелец ♐":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(
            message.chat.id,
            text="Нажми на ссылку https://horo.mail.ru/prediction/sagittarius/today/ )",
        )
    elif message.text == "♊ Близнецы ♊":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(
            message.chat.id,
            text="Нажми на ссылку https://horo.mail.ru/prediction/gemini/today/ )",
        )
    elif message.text == "♉ Телец ♉":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(
            message.chat.id,
            text="Нажми на ссылку https://horo.mail.ru/prediction/taurus/today/ )",
        )
    elif message.text == "♏ Скорпион ♏":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(
            message.chat.id,
            text="Нажми на ссылку https://horo.mail.ru/prediction/scorpio/today/ )",
        )
    elif message.text == "Знак зодиака ♈️♉️♊️♎️ по 🥳 дате рождения  ❓❓❓":
        markup = types.ReplyKeyboardMarkup(
            resize_keyboard=True,
            input_field_placeholder="Знак зодиака ♈️♉️♊️♎️",
            row_width=3,
        )                                                           # 14 -create btn zodiac
        btn15 = types.KeyboardButton("⌛️23 ноября-22 декабря🌙")
        btn16 = types.KeyboardButton("⌛️23 декабря–20 января🌙")
        btn17 = types.KeyboardButton("⌛️20 февраля–20 марта🌙")
        btn18 = types.KeyboardButton("⌛️24 сентября–23 октября🌙")
        btn19 = types.KeyboardButton("⌛️24 октября–22 ноября🌙")
        btn20 = types.KeyboardButton("⌛️22 августа–23 сентября🌙")
        btn21 = types.KeyboardButton("⌛️23 июля–21 августа🌙")
        btn22 = types.KeyboardButton("⌛️22 июня–22 июля🌙")
        btn23 = types.KeyboardButton("⌛️22 мая–21 июня🌙")
        btn24 = types.KeyboardButton("⌛️21 апреля–21 мая🌙")
        btn25 = types.KeyboardButton("⌛️21 марта–20 апреля🌙")
        btn26 = types.KeyboardButton("⌛️21 января–19 февраля🌙")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.row(btn16, btn26).row(btn15, btn17).row(btn25, btn24).row(
            btn23, btn22
        ).row(btn21, btn20).row(btn18, btn19).row(back)
        bot.send_message(
            message.from_user.id,
            "Привет, {0.first_name} {0.last_name}! \Выбери месяц🌙 и 🥳 день своего рождения в заданном интервале и я подскажу тебе твой знак зодиака♈️♉️♊️ и твою стихию🔥🌊⛰️💨".format(
                message.from_user
            ),
            reply_markup=markup,
        )
    elif message.text == "⌛️23 ноября-22 декабря🌙":
        bot.send_message(
            message.chat.id,
            text="Стрелец ♐️. Стихия  🔥🔥🔥  https://leonardo.osnova.io/8d220e63-5a3d-5905-a8df-a1aade82cbb1/",
        )
    elif message.text == "⌛️23 декабря–20 января🌙":
        bot.send_message(
            message.chat.id,
            text="Козерог ♑️. Стихия  ⛰🏞🌲☘️ https://leonardo.osnova.io/5556d999-6d72-51cd-848e-9e7052d5ade5/-/preview/500/-/format/webp/ ",
        )
    elif message.text == "⌛️20 февраля–20 марта🌙":
        bot.send_message(
            message.chat.id,
            text="Рыбы ♓️. Стихия  🌊💧💦 https://leonardo.osnova.io/3dca6d2a-84fc-5306-858e-fc1a995760c5/",
        )
    elif message.text == "⌛️24 сентября–23 октября🌙":
        bot.send_message(
            message.chat.id,
            text="Весы ♎️. Стихия  🌪🌬💨 https://leonardo.osnova.io/d4cf1be7-3840-5362-8ef0-98e679dc199c/",
        )
    elif message.text == "⌛️24 октября–22 ноября🌙":
        bot.send_message(
            message.chat.id,
            text="Скорпион ♏️. Стихия  🌊💧💦 https://leonardo.osnova.io/3dca6d2a-84fc-5306-858e-fc1a995760c5/",
        )
    elif message.text == "⌛️22 августа–23 сентября🌙":
        bot.send_message(
            message.chat.id,
            text="Дева ♍️. Стихия  ⛰🏞🌲☘️ https://leonardo.osnova.io/5556d999-6d72-51cd-848e-9e7052d5ade5/-/preview/500/-/format/webp/",
        )
    elif message.text == "⌛️23 июля–21 августа🌙":
        bot.send_message(
            message.chat.id,
            text="Лев ♌️. Стихия  🔥🔥🔥 https://leonardo.osnova.io/8d220e63-5a3d-5905-a8df-a1aade82cbb1/",
        )
    elif message.text == "⌛️22 июня–22 июля🌙":
        bot.send_message(
            message.chat.id,
            text="Рак ♋️. Стихия  🌊💧💦 https://leonardo.osnova.io/3dca6d2a-84fc-5306-858e-fc1a995760c5/",
        )
    elif message.text == "⌛️22 мая–21 июня🌙":
        bot.send_message(
            message.chat.id,
            text="Близнецы♊️ . Стихия  🌪🌬💨 https://leonardo.osnova.io/d4cf1be7-3840-5362-8ef0-98e679dc199c/",
        )
    elif message.text == "⌛️21 апреля–21 мая🌙":
        bot.send_message(
            message.chat.id,
            text="Телец ♉️ . Стихия  ⛰🏞🌲☘️ https://leonardo.osnova.io/5556d999-6d72-51cd-848e-9e7052d5ade5/-/preview/500/-/format/webp/ ",
        )
    elif message.text == "⌛️21 марта–20 апреля🌙":
        bot.send_message(
            message.chat.id,
            text="Овен♈️ . Стихия  🔥🔥🔥 https://leonardo.osnova.io/8d220e63-5a3d-5905-a8df-a1aade82cbb1/",
        )
    elif message.text == "⌛️21 января–19 февраля🌙":
        bot.send_message(
            message.chat.id,
            text="Водолей♒️ . Стихия  🌪🌬💨  https://leonardo.osnova.io/d4cf1be7-3840-5362-8ef0-98e679dc199c/",
        )
        
                                     # 15 -contacting wikipedia using def start_2
        
    elif message.text == "Wikipedia  📚📰📖":
        start_2(message)
        markup = types.ReplyKeyboardMarkup(
            resize_keyboard=True, input_field_placeholder="📗📘📚📰"
        )                          
        
                                        # 16 -contacting music using audion convert files
        
    elif message.text == "Русские певцы 𝄞⨾𓍢ִ໋":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        audio = open(r"F:\16 Звезды нас ждут.mp3", "rb")
        bot.send_chat_action(message.from_user.id, "upload_audio")
        bot.send_audio(message.chat.id, audio)
    elif message.text == "Американские певцы 𝄞⨾𓍢ִ໋":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        audio = open(r"F:\Freddie Mercury - We Will Rock You.mp3", "rb")
        bot.send_chat_action(message.from_user.id, "upload_audio")
        bot.send_audio(message.chat.id, audio)
    elif message.text == "Европейские певцы 𝄞⨾𓍢ִ໋":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        audio = open(r"F:\ABBA - Mamma Mia.mp3", "rb")
        bot.send_chat_action(message.from_user.id, "upload_audio")
        bot.send_audio(message.chat.id, audio)
    elif message.text == "Любимые певцы 𝄞⨾𓍢ִ໋":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        audio = open(r"F:\11.Так хочется жить.mp3", "rb")
        bot.send_chat_action(message.from_user.id, "upload_audio")
        bot.send_audio(message.chat.id, audio)
        
        
    elif message.text == "📺📽 Просмотр видео":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(
            message.chat.id,
            text="Для просмотра видео зайди по следующей ссылке https://www.youtube.com )",
        )
    elif message.text == "💵📈 Курс валют":
        markup = types.ReplyKeyboardMarkup(
            resize_keyboard=True, input_field_placeholder="Выбери курсы валют💲💲💱"
        )                                              
                              # 16  -create btn course valutes
        
        btn30 = types.KeyboardButton("💲KRW/RUB💲")
        btn31 = types.KeyboardButton("💲GBP/RUB💲")
        btn32 = types.KeyboardButton("💵EUR/RUB💵")
        btn33 = types.KeyboardButton("💲USD/RUB💲")
        btn35 = types.KeyboardButton("💰CNY/RUB💰")
        btn36 = types.KeyboardButton("💰UZS/RUB💰")
        btn37 = types.KeyboardButton("💰KZT/RUB💰")
        btn38 = types.KeyboardButton("💵INR/RUB💵")
        btn39 = types.KeyboardButton("💸BYN/RUB💸")
        btn40 = types.KeyboardButton("💵THB/RUB💵")
        btn41 = types.KeyboardButton("💰JPY/RUB💰")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.row(btn30, btn31, btn40).row(btn33, btn32, btn35, btn41).row(
            btn39, btn36, btn37, btn38
        ).row(back)
        bot.send_message(
            message.chat.id, "💲Выберите курс валют💲", reply_markup=markup
        )
        
                         # 16  -using json method for convert valute
        
    elif message.text == "💲KRW/RUB💲":
        url = "https://www.cbr-xml-daily.ru/daily_json.js"  # 16 /1 - contacting cbrf bank and parsing files
        response = requests.get(url) # 16/2  - getting requsets through url 
        data = response.json() # 16/3  - we getting responce using json  
        krw_1 = data["Date"] # 16/4  - we getting changes which we needing  
        krw_2 = data["Valute"]["KRW"]["Value"]
        krw_3 = data["Valute"]["KRW"]["Name"]
        krw_5 = data["Valute"]["KRW"]["Nominal"]
        krw_4 = f" Актуальный курс 💲валюты c номиналом {krw_5} {krw_3} по данным ЦБ РФ составляет {krw_2}  рублей - на {krw_1} 🕐"
        bot.send_message(message.from_user.id, krw_4)
    elif message.text == "💲GBP/RUB💲":
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url)
        data = response.json()
        gbp_1 = data["Date"]
        gbp_2 = data["Valute"]["GBP"]["Value"]
        gbp_3 = data["Valute"]["GBP"]["Name"]
        gbp_5 = data["Valute"]["GBP"]["Nominal"]
        gbp_4 = f" Актуальный курс 💲валюты c номиналом {gbp_5} {gbp_3} по данным ЦБ РФ составляет {gbp_2}  рублей - на {gbp_1} 🕐"
        bot.send_message(message.from_user.id, gbp_4)
    elif message.text == "💵EUR/RUB💵":
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url)
        data = response.json()
        eur_1 = data["Date"]
        eur_2 = data["Valute"]["EUR"]["Value"]
        eur_3 = data["Valute"]["EUR"]["Name"]
        eur_5 = data["Valute"]["EUR"]["Nominal"]
        one = 1
        eur_4 = f"  Актуальный курс 💲валюты c номиналом {eur_5} {eur_3} по данным ЦБ РФ составляет {eur_2}  рублей - на {eur_1} 🕐"
        bot.send_message(message.from_user.id, eur_4)
    elif message.text == "💲USD/RUB💲":
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url)
        data = response.json()
        usd_1 = data["Date"]
        usd_2 = data["Valute"]["USD"]["Value"]
        usd_3 = data["Valute"]["USD"]["Name"]
        usd_5 = data["Valute"]["USD"]["Nominal"]
        usd_4 = f" Актуальный курс 💲валюты c номиналом {usd_5} {usd_3} по данным ЦБ РФ составляет {usd_2}  рублей - на {usd_1} 🕐"
        bot.send_message(message.from_user.id, usd_4)
    elif message.text == "💰CNY/RUB💰":
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url)
        data = response.json()
        cny_1 = data["Date"]
        cny_2 = data["Valute"]["CNY"]["Value"]
        cny_3 = data["Valute"]["CNY"]["Name"]
        cny_5 = data["Valute"]["CNY"]["Nominal"]
        cny_4 = f"  Актуальный курс 💲валюты c номиналом {cny_5} {cny_3} по данным ЦБ РФ составляет {cny_2}  рублей - на {cny_1} 🕐"
        bot.send_message(message.from_user.id, cny_4)
    elif message.text == "💰UZS/RUB💰":
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url)
        data = response.json()
        uzs_1 = data["Date"]
        uzs_2 = data["Valute"]["UZS"]["Value"]
        uzs_3 = data["Valute"]["UZS"]["Name"]
        uzs_5 = data["Valute"]["UZS"]["Nominal"]
        uzs_4 = f" Актуальный курс 💲валюты c номиналом {uzs_5} {uzs_3} по данным ЦБ РФ составляет {uzs_2}  рублей - на {uzs_1} 🕐"
        bot.send_message(message.from_user.id, uzs_4)
    elif message.text == "💰KZT/RUB💰":
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url)
        data = response.json()
        kzt_1 = data["Date"]
        kzt_2 = data["Valute"]["KZT"]["Value"]
        kzt_3 = data["Valute"]["KZT"]["Name"]
        kzt_5 = data["Valute"]["KZT"]["Nominal"]
        kzt_4 = f"  Актуальный курс 💲валюты c номиналом {kzt_5} {kzt_3} по данным ЦБ РФ составляет {kzt_2}  рублей - на {kzt_1} 🕐"
        bot.send_message(message.from_user.id, kzt_4)
    elif message.text == "💵INR/RUB💵":
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url)
        data = response.json()
        inr_1 = data["Date"]
        inr_2 = data["Valute"]["INR"]["Value"]
        inr_3 = data["Valute"]["INR"]["Name"]
        inr_5 = data["Valute"]["INR"]["Nominal"]
        inr_4 = f"  Актуальный курс 💲валюты c номиналом {inr_5} {inr_3} по данным ЦБ РФ составляет {inr_2}  рублей - на {inr_1} 🕐"
        bot.send_message(message.from_user.id, inr_4)
    elif message.text == "💸BYN/RUB💸":
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url)
        data = response.json()
        byn_1 = data["Date"]
        byn_2 = data["Valute"]["BYN"]["Value"]
        byn_3 = data["Valute"]["BYN"]["Name"]
        byn_5 = data["Valute"]["BYN"]["Nominal"]
        byn_4 = f"  Актуальный курс 💲валюты c номиналом {byn_5} {byn_3} по данным ЦБ РФ составляет {byn_2}  рублей - на {byn_1} 🕐"
        bot.send_message(message.from_user.id, byn_4)
    elif message.text == "💵THB/RUB💵":
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url)
        data = response.json()
        thb_1 = data["Date"]
        thb_2 = data["Valute"]["THB"]["Value"]
        thb_3 = data["Valute"]["THB"]["Name"]
        thb_5 = data["Valute"]["THB"]["Nominal"]
        thb_4 = f" Актуальный курс 💲валюты c номиналом {thb_5} {thb_3} по данным ЦБ РФ составляет {thb_2}  рублей - на {thb_1} 🕐"
        bot.send_message(message.from_user.id, thb_4)
    elif message.text == "💰JPY/RUB💰":
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url)
        data = response.json()
        jpy_1 = data["Date"]
        jpy_2 = data["Valute"]["JPY"]["Value"]
        jpy_3 = data["Valute"]["JPY"]["Name"]
        jpy_5 = data["Valute"]["JPY"]["Nominal"]
        jpy_4 = f"  Актуальный курс 💲валюты c номиналом {jpy_5} {jpy_3} по данным ЦБ РФ составляет {jpy_2}  рублей - на {jpy_1} 🕐"
        bot.send_message(message.from_user.id, jpy_4)
        
        
        
        
        
        
    elif message.text == "Курсы биткоинов ₿":
        markup = types.ReplyKeyboardMarkup(
            resize_keyboard=True, input_field_placeholder="Выбери курсы биткоинов ₿"
        )                                              
                              # 18  -create btn course bitcoin
        
        btn80 = types.KeyboardButton("LTC/BTC ₿")
        btn81 = types.KeyboardButton("LTC/ETH ₿")
        btn82 = types.KeyboardButton("LTC/USD  ₿")
        btn83 = types.KeyboardButton("LTC/RUR  ₿")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.row(btn80, btn81).row(btn82,
            btn83
        ).row(back)
        bot.send_message(
            message.chat.id, "Выбери курсы биткоинов ₿", reply_markup=markup)   
       
       
                            # 18/2  -create get requset
    elif message.text == "LTC/BTC ₿":
        url = "https://yobit.net/api/3/ticker/ltc_btc"
        response = requests.get(url)
        respnoce1 =response.json()
        url12 = "https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url12)
        data = response.json()
        ltc_12 = data["Date"]
        ltc_22 = respnoce1["ltc_btc"]["high"]
        ltc_32 = respnoce1["ltc_btc"]["low"]
        ltc_42 = respnoce1["ltc_btc"]["avg"]
        ltc_52 = respnoce1["ltc_btc"]["buy"]
        ltc_62 =respnoce1["ltc_btc"]["sell"]
        ltc_72 = f" По данным криптобиржи 'yobinet' на {ltc_12} самый высокий курс биткоина ltc/eth составляет {ltc_22}, самый низкий курс {ltc_32}. При этом среднее значение биткоина составляет {ltc_42}. Цена покупки = {ltc_52}. Цена продажи = {ltc_62}. "
        bot.send_message(message.from_user.id, ltc_72)
    elif message.text == "LTC/ETH ₿":
        url = "https://yobit.net/api/3/ticker/ltc_eth"
        response = requests.get(url)
        respnoce1 =response.json()
        url1 = "https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url1)
        data = response.json()
        ltc_1 = data["Date"]
        ltc_2 = respnoce1["ltc_eth"]["high"]
        ltc_3 = respnoce1["ltc_eth"]["low"]
        ltc_4 = respnoce1["ltc_eth"]["avg"]
        ltc_5 = respnoce1["ltc_eth"]["buy"]
        ltc_6 =respnoce1["ltc_eth"]["sell"]
        ltc_7 = f" По данным криптобиржи 'yobinet' на {ltc_1} самый высокий курс биткоина ltc/eth составляет {ltc_2}, самый низкий курс {ltc_3}. При этом среднее значение биткоина составляет {ltc_4}. Цена покупки = {ltc_5}. Цена продажи = {ltc_6}. "
        bot.send_message(message.from_user.id, ltc_7)
    elif message.text == "LTC/USD  ₿":
        url6 = "https://yobit.net/api/3/ticker/ltc_usd"
        response = requests.get(url6)
        respnoce1 =response.json()
        url13 = "https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url13)
        data = response.json()
        ltc_14 = data["Date"]
        ltc_24 = respnoce1["ltc_usd"]["high"]
        ltc_34 = respnoce1["ltc_usd"]["low"]
        ltc_44 = respnoce1["ltc_usd"]["avg"]
        ltc_54 = respnoce1["ltc_usd"]["buy"]
        ltc_64 =respnoce1["ltc_usd"]["sell"]
        ltc_74 = f" По данным криптобиржи 'yobinet' на {ltc_14} самый высокий курс биткоина ltc/eth составляет {ltc_24}, самый низкий курс {ltc_34}. При этом среднее значение биткоина составляет {ltc_44}. Цена покупки = {ltc_54}. Цена продажи = {ltc_64}. "
        bot.send_message(message.from_user.id, ltc_74)
    elif message.text == "LTC/RUR  ₿":
        url23 = "https://yobit.net/api/3/ticker/ltc_rur"
        response = requests.get(url23)
        respnoce1 =response.json()
        url13 = "https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url13)
        data = response.json()
        ltc_13 = data["Date"]
        ltc_23 = respnoce1["ltc_rur"]["high"]
        ltc_33 = respnoce1["ltc_rur"]["low"]
        ltc_43 = respnoce1["ltc_rur"]["avg"]
        ltc_53 = respnoce1["ltc_rur"]["buy"]
        ltc_63 =respnoce1["ltc_rur"]["sell"]
        ltc_73 = f" По данным криптобиржи 'yobinet' на {ltc_13} самый высокий курс биткоина ltc/eth составляет {ltc_23}, самый низкий курс {ltc_33}. При этом среднее значение биткоина составляет {ltc_43}. Цена покупки = {ltc_53}. Цена продажи = {ltc_63}. "
        bot.send_message(message.from_user.id, ltc_73)
     
                                 # 17  - using message 
    elif message.text == "🎙🎚 Прослушивание музыки":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(
            message.chat.id,
            text="Для прослушивания музыки зайди по следующей ссылке https://zaycev.net/)",
        )
    elif message.text == "Как тебя зовут?":
        bot.send_message(message.chat.id, " Меня зовут информационно-поисквой  бот🤖")
    elif message.text == "Что ты можешь?":
        bot.send_message(
            message.chat.id,
            text="Я могу найти тебе информацию о последних новостях,прогноз погоды, астропрогноз, курс биржи, прослушивания музыки и просмотра видео и помочь тебе с вычислением",
        )
    elif message.text == "Что ты можешь мне найти?":
        bot.send_message(
            message.chat.id,
            text="Я могу найти тебе только то, что запрограммировали в поисковой программе",
        )
        
                            # 18  - writting datetime
    elif message.text == "Ты можешь мне сказать сколько сейчас времени?":
        bot.send_message(message.chat.id, text="Конечно могу")
        nowdate = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        offset = datetime.timedelta(hours=3)
        timezone = datetime.timezone(offset)
        now_with_offset = datetime.datetime.now(tz=timezone)
        w_time = (
            "Сейчас в городе Омске 🏙 "
            + str(nowdate)
            + " 🕐"
            + " в столице РФ = Москве "
            + str(now_with_offset)
            + " 🕐"
        )
        bot.send_message(message.chat.id, w_time)
    elif message.text == "Хотелось бы узнать, какие твои любимые блюда?":
        bot.send_message(message.chat.id, text="У меня есть два любимых мной блюда 🍔")
        bot.send_message(message.chat.id, text="Первое блюдо это:Лазанья")
        bot.send_photo(
            message.chat.id,
            "https://static.1000.menu/img/content-v2/b4/50/54271/lazanya-nastoyaschaya_1619886996_1_min.jpg",
        )
        bot.send_message(message.chat.id, text="Второе блюдо это:торт Наполеон ")
        bot.send_photo(
            message.chat.id,
            "https://sun6-22.userapi.com/s/v1/ig2/MtKx2HsC9ncRrjp4QLkyE2PBDceGQR3FSHKAkAQttPP8vRWSUFCKj1v3l5aF7sK5bQBuHAAa7G9DdZqz4PGqzCvt.jpg?size=100x100&quality=95&crop=294,4,1103,1103&ava=1",
        )
    elif message.text == "А ты можешь мне рассказать о путешествиях  и показать их?":
        bot.send_message(
            message.chat.id,
            text="Да. Я могу рассказать тебе о путешествиях 🛩🗽🗿⛪️🏛🗼 и рекомендовать сайты для покупки туристических путевок",
        )
        bot.send_message(
            message.chat.id,
            text="Посмотри видео отдохни от суеты дня: https://youtu.be/cEEfl-if4-M",
        )
        bot.send_message(
            message.chat.id,
            text="Как я и обещал тебе. Я скинул сайты для покупок путевок от проверенных туроператоров 1 сайт-это пегас туристик https://pegas-turistik.ru/?yclid=1765779833184059391 и 2 сайт- это анекс тур https://attour.ru/?yclid=11692340695538597887",
        )
    elif message.text == "Чем ты занимаешься?":
        bot.send_message(
            message.chat.id,
            text="Я работаю на благо пользователя и постоянно улучшаю свои функции",
        )
        file = open("F:\фото и видео\египет\DSC03013.jpg", "rb")
        bot.send_photo(message.chat.id, file, " Это Египет я там отдыхал😎")
    elif message.text == "Как твои дела?":
        bot.send_message(message.chat.id, text="Спасибо все хорошо!!!👍🙂")
        bot.send_message(
            message.chat.id,
            text="https://avatars.yandex.net/get-music-content/118603/7721091c.a.8088924-1/300x300",
        )
    elif message.text == "А в каком городе ты живешь?":
        
                             # 18  - send video files
        bot.send_message(message.chat.id, text="Я живу в городе Омске  ")
        file = open('F:\фото и видео\Видео разное\Видео разное\Видео-0001.mp4', 'rb')
        bot.send_video(message.chat.id, file)
        bot.send_message(message.chat.id, text="https://youtu.be/fNnFMT9HkTk?t=84")
        bot.send_message(
            message.chat.id,
            text=" Путеводитель по Омску(Классные мероприятия и места для посещения в городе) подпишись по этой ссылке https://t.me/omsk_putevoditel и  это  сайт о актуальных событиях культурной столицы Сибири - Омска по подпишись по этой ссылке https://t.me/pro_omsk",
        )
    elif message.text == "Новостной сайт🖥⌨️💻":
        bot.send_message(
            message.chat.id,
            text=" Это рекомендованный мной сайт новостей https://lenta.ru/?ysclid=lvmn7a6qh6182649346 ",
        )
    elif message.text == "Калькулятор 💻⌨️":
        bot.send_message(
            message.chat.id, text=" Онлайн калькулятор https://okcalc.com/ru/"
        )
        
        
                               # 19  - def weather
    elif message.text == ("🌎 Прогноз погоды"):
        start_1(message)
        
        
    elif message.text == "👩‍⚕️💂‍♂️👩‍✈️👨‍❤️‍👨Сайты для общения":
        bot.send_message(
            message.chat.id,
            text=" Я могу тебе рекомендовать несколько сайтов для общения вконтакте - https://vk.com/?ysclid=lvqzhspcig651018619  одноклассники - https://ok.ru/?ysclid=lvqzj31ri9831586258",
        )
    elif message.text == "А сколько тебе лет?":
        my_birthdate = 1983
        birthdate_now = datetime.datetime.now().year
        delta = birthdate_now - my_birthdate
        w_years = "Мне сейчас " + str(delta) + " год"
        bot.send_message(message.chat.id, w_years)
        
                              # 20 - writting return on main menu
    elif message.text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(
            resize_keyboard=True, input_field_placeholder="Напишите что вас интересует"
        )
        btn1 = types.KeyboardButton(" Привет пользователь👋 ")
        btn2 = types.KeyboardButton("Задайте вопрос боту ❓")
        btn13 = types.KeyboardButton(" Wikipedia  📚📰📖")
        btn3 = types.KeyboardButton("📺📽 Просмотр видео")
        btn4 = types.KeyboardButton("🌎 Прогноз погоды")
        btn5 = types.KeyboardButton("🌟 Астропрогноз")
        btn6 = types.KeyboardButton("💵📈 Курс валют")
        btn7 = types.KeyboardButton("🎙🎚 Прослушивание музыки")
        btn8 = types.KeyboardButton(
            text="🏙 Местоположение пользователя", request_location=True
        )
        btn9 = types.KeyboardButton(
            text="Запрос номера телефона ☎️", request_contact=True
        )
        btn10 = types.KeyboardButton(text="Новостной сайт🖥⌨️💻 ")
        btn11 = types.KeyboardButton(text="Калькулятор 💻⌨️ ")
        btn12 = types.KeyboardButton(text="👩‍⚕️💂‍♂️👩‍✈️👨‍❤️‍👨Сайты для общения")
        btn14 = types.KeyboardButton(text="Опрос по оценки бота ⁉️❤️❤️❤️")
        btn15 = types.KeyboardButton(text="Курсы биткоинов ₿")
        markup.add(btn1).row(btn2, btn13).row(btn3, btn7).row(btn4, btn5).row(
            btn6, btn11, btn15
        ).row(btn8, btn9).row(btn10, btn12).row(btn14)
        bot.send_message(
            message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup
        )
    else:
        bot.send_message(message.chat.id, text="Извините,я не знаю ответа!!")

                          # 21 writting def wiki
def start_2(m, res=False):
    bot.send_message(m.chat.id, "Отправьте мне любое слово, и я найду его в Wikipedia")
    bot.register_next_step_handler(m, handle_text)

    # bot.register_next_step_handler(message, handle_text)
    # if message.text == " next":
    #   return bot.register_next_step_handler(message, handle_text
    # elif message.text == "stop":
    #  return bot.register_next_step_handler(message, start)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, question_wiki(message.text))

wikipedia.set_lang("ru")


def question_wiki(q): #  write def wiki
    try:  #  try except
        ny = wikipedia.page(q) # 2 -using function page with params
        # 1- Получаем первые 500 символов
        wikitext = ny.content[:500]
        # 2 -Разделяем по точкам using function split
        wikimas_1 = wikitext.split(".")
        # 3- Отбрасываем всЕ после последней точки
        wikimas_1 = wikimas_1[:-1]
        # 4- Создаем пустую переменную для текста
        wikitext5 = ""
        for x in wikimas_1:
            if not ("==" in x):
                # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                if len((x.strip())) > 5:  # 3- write cycle if else and len >5
                    wikitext5 = wikitext5 + x + "." 
            else:
                break
        wikitext5 = re.sub("\([^()]*\)", "", wikitext5) # 2 -using module re with sub func
        wikitext5 = re.sub("\([^()]*\)", "", wikitext5)
        wikitext5 = re.sub("\{[^\{\}]*\}", "", wikitext5)
        # return text str
        return wikitext5
    # handler except with class Exception
    except Exception as e:
        return "В wikipedia нет информации об этом, поищи в другом источнике"


# bot.register_next_step_handler(q, start)

                     # 22 write handler locaton 
@bot.message_handler(content_types=["location"])
def check_contact(message):
    bot.send_message(message.chat.id, message.location)


                        # 23 write weather def for start bot
start_txt = "Привет! Это встроенный бот прогноза погоды 🌎 \n Напиши город, где ты хочешь узнать погоду."
def start_1(message):
    bot.send_message(message.from_user.id, start_txt, parse_mode="Markdown")
    bot.register_next_step_handler(message, weather)

                      # 24 write handler text with def weather
@bot.message_handler(content_types=["text"])
def weather(message):
              # 25 write city text
    city = message.text
    url = (
        "https://api.openweathermap.org/data/2.5/weather?q="       # 25 getting url requests
        + city
        + "&units=metric&lang=ru&appid=aeb953cb7af779e4d1ee36c7993255c8"
    )
    weather_data = requests.get(url).json()    
    
    
                                 # 26 writting response for url
    coord_lon = round(weather_data["coord"]["lon"])
    coord_lat = round(weather_data["coord"]["lat"])

    nowdate = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    offset = datetime.timedelta(hours=3)
    timezone = datetime.timezone(offset)
    now_with_offset = datetime.datetime.now(tz=timezone)

    wind_speed = round(weather_data["wind"]["speed"])
    if wind_speed < 5:
        bot.send_message(message.from_user.id, "✅ Погода хорошая, ветра почти нет")
        bot.send_photo(
            message.from_user.id,
            "https://4.bp.blogspot.com/-uQ008xOS7gA/W1NHyDquYuI/AAAAAAAACsM/46V_u7gKtC4Hb79K4-_sY-C_7CsY2cIPgCLcBGAs/s1600/382389_461489750542615_1387397981_n.jpg",
        )
    elif wind_speed < 10:
        bot.send_message(
            message.from_user.id, "🤔 На улице ветрено, оденьтесь чуть теплее"
        )
        bot.send_photo(
            message.from_user.id,
            "https://www.litprichal.ru/upload/515/c310c9775d923a087cdf583ef0a9aec8.jpg",
        )
    elif wind_speed < 20:
        bot.send_message(
            message.from_user.id,
            "❗️ Ветер очень сильный, будьте осторожны, выходя из дома",
        )
        bot.send_photo(
            message.from_user.id, "https://img.youtube.com/vi/tdTHp5y5ffY/mqdefault.jpg"
        )
    else:
        bot.send_message(
            message.from_user.id, "❌ На улице шторм, на улицу лучше не выходить"
        )
        bot.send_photo(
            message.from_user.id, "https://www.nastol.com.ua/mini/201901/317410.jpg"
        )

    temperature = round(weather_data["main"]["temp"])
    if temperature > 30:
        bot.send_message(
            message.from_user.id, "💥 На улице очень жарко. Оденьте головной убор "
        )
        bot.send_photo(
            message.from_user.id,
            "https://www.shutterstock.com/image-photo/very-hot-day-summer-temperature-260nw-293047637.jpg",
        )
    elif temperature > 20:
        bot.send_message(message.from_user.id, "☀️ На улице жарко. Идите на пляж ")
        bot.send_photo(
            message.from_user.id,
            "http://1.bp.blogspot.com/-AUfp6pPdzNw/T8al4K4othI/AAAAAAAAAFo/OAPIE0KYUws/s320/6196.jpg",
        )
    elif temperature > 10:
        bot.send_message(
            message.from_user.id, "🌈 На улице тепло. Самое время погулять"
        )
        bot.send_photo(
            message.from_user.id,
            "https://im.jigsawplanet.com/?rc=img&pid=385fbf5a417b&size=160",
        )
    elif temperature > 0:
        bot.send_message(message.from_user.id, "🏀 Погода хорошая ")
        bot.send_photo(
            message.from_user.id,
            "https://wallbox.ru/resize/320x240/wallpapers/main/201328/b479da9d3f6f532.jpg",
        )
    elif temperature < 0:
        bot.send_message(message.from_user.id, "⛄️ На улице холодно ")
        bot.send_photo(
            message.from_user.id, "https://images.newsnowgreece.com/32/325883/1.jpg"
        )
    elif temperature < -20:
        bot.send_message(
            message.from_user.id, "❄️ На улице холодно, оденьтесь в теплую одежду"
        )
        bot.send_photo(
            message.from_user.id,
            "https://dl-media.viber.com/5/share/2/long/vibes/roll/image/400/3668/32da0acd80c201e0223b80e9a9474ede20a18a11fc3f3717cb45c87af2103668.jpg",
        )
    else:
        bot.send_message(
            message.from_user.id,
            " 👎🌡 На улице сильный холод или сильная жара, на улицу лучше не выходить",
        )
        bot.send_photo(
            message.from_user.id,
            "https://lastfm.freetls.fastly.net/i/u/avatar170s/cef5fdb7068f008fcf1a11599512ff60",
        )

    temperature_feels = round(weather_data["main"]["feels_like"])

    pressure = round(weather_data["main"]["pressure"])
    if pressure == 1013:
        bot.send_message(message.from_user.id, " 😊 Атмосферное давление в норме")
    elif pressure < 1013:
        bot.send_message(
            message.from_user.id,
            " 🙁 Повышенное атмосферное давление. Берегите здоровье",
        )
    elif pressure > 1013:
        bot.send_message(
            message.from_user.id,
            "😕 Повышенное атмосферное давление. Берегите здоровье",
        )

    humidity = round(weather_data["main"]["humidity"])
    if humidity > 30 or humidity < 60:
        bot.send_message(
            message.from_user.id, " 😊 Показатель влажности  в норме для человека"
        )
    elif humidity < 30:
        bot.send_message(
            message.from_user.id, " 🙁  Пониженная влажность. Следите за своим здоровье"
        )
    elif humidity > 60:
        bot.send_message(
            message.from_user.id, "😕 Повышенная влажность. Следите за своим здоровье"
        )

    clouds = round(weather_data["clouds"]["all"])
    if clouds > 50:
        bot.send_message(message.from_user.id, " ☁️Большая облачность.")
    elif clouds < 50:
        bot.send_message(message.from_user.id, "⛅️ Мало облачно на улице ")
    else:
        bot.send_message(message.from_user.id, "☀️ Ясно ")

    visibility = round(weather_data["visibility"])

    sunrise_timestamp_1 = round(weather_data["sys"]["sunrise"])
    sunrise_timestamp = datetime.datetime.fromtimestamp(sunrise_timestamp_1)

    sunset_timestamp_1 = round(weather_data["sys"]["sunset"])
    sunset_timestamp = datetime.datetime.fromtimestamp(sunset_timestamp_1)

    wind_deg = round(weather_data["wind"]["deg"])
    if wind_deg == 360 or 0:
        bot.send_message(message.from_user.id, "🌬 Ветер северный ⬆️")
    elif wind_deg > 0 or wind_deg < 90:
        bot.send_message(message.from_user.id, "🌬 Ветер северо-восточный ↗️")
    elif wind_deg == 90:
        bot.send_message(message.from_user.id, "🌬 Ветер восточный ⬇️")
    elif wind_deg > 90 or wind_deg < 180:
        bot.send_message(message.from_user.id, "🌬 Ветер юго-восточный ↘️")
    elif wind_deg == 180:
        bot.send_message(message.from_user.id, "🌬 Ветер южный ⬇️")
    elif wind_deg > 180 or wind_deg < 270:
        bot.send_message(message.from_user.id, "🌬 Ветер юго-западный ↙️")
    elif wind_deg == 270:
        bot.send_message(message.from_user.id, "🌬 Ветер западный ⬅️")
    elif wind_deg > 270 or wind_deg < 360:
        bot.send_message(message.from_user.id, "🌬 Ветер северо-западный ↖️")
    else:
        bot.send_message(message.from_user.id, "🌈  На улице безветренно ⏹")

    # wind_gust = round(weather_data['wind']['gust'])

    length_of_the_day = datetime.datetime.fromtimestamp(
        weather_data["sys"]["sunset"]
    ) - datetime.datetime.fromtimestamp(weather_data["sys"]["sunrise"])
    temperature_feels_min = round(weather_data["main"]["temp_min"])
    temperature_feels_max = round(weather_data["main"]["temp_max"])

    w_time = (
        "Сейчас в городе Омске 🏙 "
        + str(nowdate)
        + " 🕐"
        + " в столице РФ "
        + str(now_with_offset)
        + " 🕐"
    )
    cl_now = f" Географические координаты города 🌎 {city} - долгота: {coord_lon} : широта {coord_lat}"
    w_now = "Сейчас в городе 🏙 " + city + " " + str(temperature) + " °C🌡 "
    w_feels = "Ощущается как " + str(temperature_feels) + " °C 🌡"
    w_temp_m = f" Минимальная температура🌡 : {temperature_feels_min } °C🌡.  Максимальная температура🌡: {temperature_feels_max} °C🌡"
    w_pr = (
        " Атмосферное давление 🔔: "
        + str(pressure)
        + " Па ;  Барометрическое давление 👁‍🗨: "
        + str(round(math.ceil(pressure) / 1.333))
        + " мм.рт.ст. ; Влажность "
        + str(humidity)
        + " %"
    )
    w_cl = (
        " Облачность ☁️"
        + str(clouds)
        + " %"
        + " Видимость 👀"
        + str(math.ceil(visibility) / 1000)
        + " км "
    )
    w_pr_wind = (
        "Скорость ветра 🌪 "
        + str(wind_speed)
        + " м/с "
        + " Направление ветра по розе ветров ➡️"
        + str(wind_deg)
        + " градусов"
        + "  Порыв ветра ⏩"
    )  # + str(wind_gust) + ' м/с'
    w_sun = (
        " Время восхода солнца 🌞"
        + str(sunrise_timestamp)
        + " ч "
        + " Время захода солнца 🌚  "
        + str(sunset_timestamp)
        + " ч"
    )
    w_length_of_the_day = "Продолжительность дня  ⏲" + str(length_of_the_day) + " ч"


                          # 27 inpit ob display 
    bot.send_message(message.from_user.id, w_time)
    bot.send_message(message.from_user.id, cl_now)
    bot.send_message(message.from_user.id, w_now)
    bot.send_message(message.from_user.id, w_feels)
    bot.send_message(message.from_user.id, w_temp_m)
    bot.send_message(message.from_user.id, w_pr)
    bot.send_message(message.from_user.id, w_cl)
    bot.send_message(message.from_user.id, w_pr_wind)
    bot.send_message(message.from_user.id, w_sun)
    bot.send_message(message.from_user.id, w_length_of_the_day)
    bot.register_next_step_handler(message, weather)

                             
                             
                                   # 28 write if name == main     
if __name__ == "__main__":
    while True: # 28/1 write while TRUE  
        # в бесконечном цикле постоянно опрашиваем бота о сообщениях
        try:
            bot.polling(none_stop=True, interval=0)
        # если возникла ошибка — сообщаем про исключение и продолжаем работу
        except Exception as e:
            print("⛔️❌⭕️⛔️ Сработало исключение! ⛔️❌⭕️⛔️")




bot.polling(none_stop=True)  # 29 start bot   
