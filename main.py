import random
import telebot
import webbrowser
from telebot import types
import requests

bot = telebot.TeleBot('6728379188:AAGURXHQk1KUjQUYaMTZcVLthJivPuyKJr4')

answers=['(→_→)', '┐(￣ヘ￣;)┌', '(•ิ_•ิ)?', '╮(︶▽︶)╭','ー ー','ヽ(　￣д￣)ノ']



@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🟢 Услуги❗')
    button2 = types.KeyboardButton('🟢 Товары❗ ')
    button3=types.KeyboardButton('🟢 Написать нам 📞❗')
    
    # Разделяю кнопки по строкам так, чтобы товары были отдельно от остальных кнопок
    markup.row(button1,button2,button3)
    if message.text == '/start':
        bot.send_message(message.chat.id,f' 👋 Привет❗ {message.from_user.first_name}', reply_markup=markup)
    else:
        bot.send_message(message.chat.id,text='🟣Перекинул тебя в главном меню ⤴️❗ Выбирай ❗', reply_markup=markup)




@bot.message_handler()
def info(message):
    if message.text == '🟢 Услуги❗':
        goodsChapter(message)
    elif message.text =='🟢 Товары❗':
        ONAS(message)
    elif message.text =='🟢 Написать нам 📞❗': 
        markup = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text='🟢 Написать нам 📞❓ ', url='https://t.me/+Dga3bvvxL3M0NzRi')
        markup.add(url_button)
        bot.send_message(message.chat.id,f'Желаете перейти по ссылке ❓', reply_markup=markup)     
    elif message.text == '⭕ Назад❗':
       welcome(message)
    elif message.text == '⭕  Назад❗':
          welcome(message)
    elif message.text =='🟢 Написать нам 📞❗':                                 #ссылку доделать!
        markup = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text='🟢 Написать нам 📞❓ ', url='https://t.me/+Dga3bvvxL3M0NzRi')
        markup.add(url_button)
        bot.send_message(message.chat.id,f'Желаете перейти по ссылке ❓', reply_markup=markup)                 
    elif message.text =='✅ 🚗 РЕМОНТ И ДИОГНОСТИКА АВТОМОБИЛЕЙ❗🔧❗':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        file=open("avto1.jpg",'rb')
        bot.send_photo(message.chat.id,file,'инфа\nинфа\nинфа\nинфа\nинфа\nинфа\nинфа\nинфа\nинфа\nинфа\n', reply_markup=markup)
    elif message.text =='✅ 📻РЕМОНТ И ДИОГНОСТИКА КУХОННОЙ ЭЛЕКТРОТЕХНИКИ❗🔧❗':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        file=open("kuchina2.jpg",'rb')
        bot.send_photo(message.chat.id,file,'инфа\nинфа\nинфа\nинфа\nинфа\nинфа\nинфа\nинфа\nинфа\nинфа\n', reply_markup=markup)   
    elif message.text =='✅ 📺 РЕМОНТ И ДИОГНОСТИКА БЫТОВОЙ ЭЛЕКТРОТЕХНИКИ❗🔧❗':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        file=open("bit3.jpg",'rb')
        bot.send_photo(message.chat.id,file,'инфа\nинфа\nинфа\nинфа\nинфа\nинфа\nинфа\nинфа\nинфа\nинфа\n', reply_markup=markup)
    elif message.text =='🟪 Истукан 🗿❗':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        file=open("istukan.jpg",'rb')
        bot.send_photo(message.chat.id,file,'', reply_markup=markup)
        markup = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text='💰 Купить 🛍️ ', url='https://t.me/+Dga3bvvxL3M0NzRi')
        url_button2 = types.InlineKeyboardButton(text='📌 Узнать о наличии товара❗ 📌', url='https://t.me/+Dga3bvvxL3M0NzRi')
        markup.row(url_button,url_button2)
        bot.send_message(message.chat.id,f'До сих пор в СМИ и не самой научной литературе продолжают мусолить тему «загадочных» истуканов острова Пасхи.\n С какой целью это делается? — В этом заинтересована туриндустрия, и сами островитяне.\n С тайнами и мистикой этот клочок земли становится в разы привлекательнее. \nВот туда и нарастает поток туристов. А местные работают в сфере их обслуживания; после того, как у них построили нормальную инфраструктуру, \nнаконец, могут сыто и спокойно жить (чего не могли позволить себе столетиями), постепенно растворяясь среди призжих чилийцев с материка',reply_markup=markup) 
            

    else:
         bot.send_message(message.chat.id, answers[random.randint(0, 3)])
         
def goodsChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button05 = types.KeyboardButton('🟢 Написать нам 📞❗')
    button10 = types.KeyboardButton('✅ 🚗 РЕМОНТ И ДИОГНОСТИКА АВТОМОБИЛЕЙ❗🔧❗')
    button20 = types.KeyboardButton('✅ 📻РЕМОНТ И ДИОГНОСТИКА КУХОННОЙ ЭЛЕКТРОТЕХНИКИ❗🔧❗')
    button30 = types.KeyboardButton('✅ 📺 РЕМОНТ И ДИОГНОСТИКА БЫТОВОЙ ЭЛЕКТРОТЕХНИКИ❗🔧❗')
    button40 = types.KeyboardButton('⭕  Назад❗')
    markup.add(button20)
    markup.add(button30)
    markup.add(button10)
    markup.row(button05,button40)
    bot.send_message(message.chat.id, 'Выберите услугу!', reply_markup=markup)
    
    
        

def ONAS(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button56 = types.KeyboardButton('🟢 Написать нам 📞❗')
    button57 = types.KeyboardButton('⭕ Назад❗')
    button55 = types.KeyboardButton('🟪 Истукан 🗿❗')
    button54 = types.KeyboardButton('🟪 🌈🚀❗')
    button53 = types.KeyboardButton('🟪 🌈🚀❗')
    button52 = types.KeyboardButton('🟪 🌈🚀❗')
    button51 = types.KeyboardButton('🟪 🌈🚀❗')
    button50 = types.KeyboardButton('🟪 🌈🚀❗')
    button49 = types.KeyboardButton('🟪 🌈🚀❗')
    button48 = types.KeyboardButton('🟪 🌈🚀❗')
    button47 = types.KeyboardButton('🟪 🌈🚀❗')
    button46 = types.KeyboardButton('🟪 🌈🚀❗')
    button45 = types.KeyboardButton('🟪 🌈🚀❗')
    button44 = types.KeyboardButton('🟪 🌈🚀❗')
    button43 = types.KeyboardButton('🟪 🌈🚀❗')
    button42 = types.KeyboardButton('🟪 🌈🚀❗')
    button41 = types.KeyboardButton('🟪 🌈🚀❗')
    markup.add(button55)
    markup.add(button54)
    markup.add(button53)
    markup.add(button52)
    markup.add(button51)
    markup.add(button50)
    markup.add(button49)
    markup.add(button48)
    markup.add(button47)
    markup.add(button46)
    markup.add(button45)
    markup.add(button44)
    markup.add(button43)
    markup.add(button42)
    markup.add(button41)
    markup.row(button56,button57)
    bot.send_message(message.chat.id, '🟣 Выберите товар 🛍️', reply_markup=markup)


bot.polling(none_stop=True)





