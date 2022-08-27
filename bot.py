#библиотеки, которые загружаем из вне
import random
import telebot
import os
from telebot import types

TOKEN = '5166359900:AAGxib3Y-sSaVzITSWsjB1lzGr3vdjmNR2o'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	
	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Мой репозиторий")
	item2 = types.KeyboardButton("Написать мне в личку")
	item3 = types.KeyboardButton("Вконтакте")
	item4 = types.KeyboardButton("Почта")
	
	markup.add(item1, item2, item3, item4)

	bot.send_message(message.chat.id, "Привет тебе от Михаила, {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == 'Мой репозиторий':
			bot.send_message(message.chat.id, 'https://github.com/MikhailFadyushinQA')
		elif message.text == 'Написать мне в личку':
			bot.send_message(message.chat.id, 'https://t.me/MikhailFadyushin')
		elif message.text == 'Вконтакте':
			bot.send_message(message.chat.id, 'https://vk.com/fadyushinm')
		elif message.text == 'Почта':
			bot.send_message(message.chat.id, 'fadyushin.mikhail@yandex.ru')
		else:
			bot.send_message(message.chat.id, 'Если хочешь пообщаться, пиши мне в личку Telegram !')


bot.polling(none_stop=True)








#https://core.telegram.org/bots/api#available-methods