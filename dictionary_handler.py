import json
import difflib
from random import choice

class Dictionary:
	"""
	when initialized, will import a json file and prepare it as a python dictionary if the given file path exists or will set an empty dictionary as the dataset. 
	"""
	def __init__(self, fp:str):
		self.__dictionary = None

		try:
			with open(fp, encoding="utf-8", mode="r") as file:
				self.__dictionary = json.load(file)
			file.close()
		except:
			self.__dictionary = {}

	def __repr__(self) -> str:
		return "dictionary object."

	def __contains__(self, word:str) -> bool:
		return True if word in self.__dictionary else False

	def translate(self, word:str) -> list:
		'''
		will translate the word from the dictionary and return a list of definitions(strings) or will throw an error that will need to be handled elsewhere. use this method after checking that the enquiry exists in the dictionary
		'''
		return self.__dictionary[word]

	def get_close_match(self, word: str) -> str:
		'''
		will get the closest match from the dictionary for the word requested and return it as a string or will return an empty string indicating the word requested for is not close to a real word that exists in the dictionary. use this class if there is no definition for the word in question
		'''
		close_matches = difflib.get_close_matches(word, self.__dictionary.keys(), n = 1, cutoff=0.8)
		if close_matches:
			return close_matches[0]
		else:
			return ""

	def is_loaded(self) -> bool:
		'''
		returns a boolean indicating if a dictionary is properly loaded
		'''
		return self.__dictionary != {}

	def random(self) -> list:
		'''
		will return a list containing a random word and it's definition
		'''
		random_word = choice(list(self.__dictionary.keys()))
		return [random_word, self.__dictionary[random_word]]