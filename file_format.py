import json
import os
import re
import win32com.client
import win32api
import random 
import Tkinter as tk

speaker = win32com.client.Dispatch("SAPI.SpVoice")



m = tk.Tk()



shell = win32com.client.Dispatch("WScript.Shell")
word_pattern = re.compile("[A-Za-z][a-z\-]+")
spelling_list = []
words = []




class spell_word:
	def __init__(self, word, diff):
		self.word = word
		self.diffs = diff
		if word not in words:
			spelling_list.append(self)
		else:
			current_word = spelling_list[words.index(word)]
			current_word.diffs= diff
	
	def __repr__(self):
		return str(self.word) + " ---> " + str(self.diffs)
				

def load_words():
	file_names = os.listdir("texts")
	ind = 1
	for file_name in file_names:
		word_file = open("texts/" + file_name, "r")
		words = word_pattern.findall(word_file.read())
		for word in words:
			if word == "or":
				continue
			spell_word(word, ind)
		
		ind += 1

def get_random_word(diff = 0):
	possible_words = spelling_list
	if diff == 0:
		return random.choice(possible_words)
	else:
		possible_words = filter(lambda word: word.diffs[0] == diff, possible_words)
		return random.choice(possible_words)







load_words()

speller_word = get_random_word()


user_guess = tk.StringVar() 
def display_userguess():
	print user_guess.get()	

serializable_list = []
for item in spelling_list:
	serializable_list.append({"word":item.word, "diff":item.diffs})

print json.dumps(serializable_list)
