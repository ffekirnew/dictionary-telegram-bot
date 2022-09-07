import telebot
import json
from dictionary_handler import Dictionary
from resources import *

API = '5425176431:AAFiwhPjNvvCTBiUYpXG1JsM1urBbgkgfY8'

bot = telebot.TeleBot(API)
dictionary = Dictionary('dictionaries/en-amh.json')
mode = None
dictionary_mode = None

def db_writer(message, word:str):
	with open(learned_json_file_path) as file:
		data = json.load(file)
	file.close()
	if str(message.chat.id) in data:
		if not word in data[str(message.chat.id)]:
			data[str(message.chat.id)].insert(0, word)
	else:
		data[str(message.chat.id)] = [word]
	with open(learned_json_file_path, mode='w') as file:
		json.dump(data, file)
	file.close()

def home(message, text:str, button:list = []):
	global dictionary, mode, dictionary_mode
	dictionary_mode = modes[mode]
	dictionary = Dictionary(dictionary_mode['file_path'])

	markup = telebot.types.ReplyKeyboardMarkup(row_width=3)
	for i in button:
		custombtn = telebot.types.KeyboardButton(i)
		markup.add(custombtn)
	itembtn1 = telebot.types.KeyboardButton(dictionary_mode['buttons'][0].format(bot_emoji))
	itembtn2 = telebot.types.KeyboardButton(dictionary_mode['buttons'][1].format(book_emoji))
	itembtn3 = telebot.types.KeyboardButton(dictionary_mode['buttons'][2].format(features_emoji))
	itembtn4 = telebot.types.KeyboardButton(dictionary_mode['buttons'][3].format(gear_emoji))
	markup.add(itembtn1, itembtn2)
	markup.add(itembtn3, itembtn4)
	bot.reply_to(message, text, reply_markup=markup)

@bot.message_handler(commands=['start'])
def start(message):
	global dictionary
	markup = telebot.types.ReplyKeyboardMarkup(row_width=3)
	itembtn1 = telebot.types.KeyboardButton("{}".format(en_to_en_emoji))
	itembtn2 = telebot.types.KeyboardButton("{}".format(en_to_amh_emoji))
	itembtn3 = telebot.types.KeyboardButton("{} What is this?".format(info_emoji))
	itembtn4 = telebot.types.KeyboardButton("{} About Us".format(computer_emoji))
	markup.add(itembtn1, itembtn2)
	markup.add(itembtn3, itembtn4)
	bot.send_message(message.chat.id, "Language {}".format(gear_emoji), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def translate(message):
	global mode
	if message.text == en_to_en_emoji or message.text == en_to_amh_emoji: # if user picked the options from the start page.
		mode = 0 if message.text == en_to_en_emoji else 1
		home(message, "You are now in the {} dictionary.".format(message.text))

	elif info_emoji in message.text:
		bot.send_message(message.chat.id, description)

	elif computer_emoji in message.text:
		bot.send_message(message.chat.id, contact)

	elif gear_emoji in message.text or mode == None or not dictionary.is_loaded(): # error handling for if the bot has not been loaded properly
		start(message)

	elif features_emoji in message.text:
		bot.send_message(message.chat.id, features)

	elif book_emoji in message.text:
		with open(learned_json_file_path) as file:
			data = json.load(file) 
		file.close()

		if str(message.chat.id) in list(data.keys()):
			home(message, "The below are words you have already learned. Select them if you want to refresh your memory on them.", data[str(message.chat.id)])
		else:
			home(message, "You have not learned words here so far. Search or get random words.")

	elif bot_emoji in message.text: # to randomly generate a word for user
		random_word = dictionary.random()
		bot.reply_to(message, "The random word picked for you is: {}.\nIt Means: ".format(random_word[0]))
		for i in range(len(random_word[1])):
			bot.send_message(message.chat.id, "Definition " + str(i + 1) + ": " + random_word[1][i])
		home(message, "Another " + dictionary_mode['buttons'][0].format(bot_emoji) + "?")
		db_writer(message, random_word[0])
	
	else:
		word = message.text
		if word in dictionary:
			bot.reply_to(message, "Your search '{}' means:".format(message.text))
			definition = dictionary.translate(word)
			for i in range(len(definition)):
				bot.send_message(message.chat.id, "Definition " + str(i + 1) + ": " + definition[i])
			home(message, "{} Search for anything here.".format(search_emoji))
			db_writer(message, word)

		else:
			close_match = dictionary.get_close_match(word)
			if close_match:
				home(message, "The enquiry '{}' does not exist in the dictionary. Did you mean '{}'?".format(word, close_match), [close_match])
			else:
				bot.reply_to(message, "The definition for '{}' does not exist. Check the spelling.".format(word))
				home(message, "{} Search for anything here.".format(search_emoji))

bot.infinity_polling()