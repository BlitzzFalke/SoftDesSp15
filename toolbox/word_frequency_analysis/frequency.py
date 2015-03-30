""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string

persuassion_full_text = 'persuasion.txt'

def get_word_list(filename):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	f = open(filename, 'r')
	lines = f.readlines()
	dictionary = {'hello': 2}
	currentline = 0
	while lines[currentline].find('START OF THIS PROJECT GUTENBERG BOOK') == False:
		currentline += 1
	lines = lines[currentline+1:]

	for line in lines:
		for word in line.split():
			word = word.lower()
			word = word.strip(string.punctuation)
			if word in dictionary:
				dictionary[word] += 1
			
			else:
				dictionary[word] = 1
				
	return dictionary

dictionary = get_word_list(persuassion_full_text)

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	dictionary = word_list
	frequencydictionary = sorted(dictionary, key = dictionary.get, reverse = True)
	length = len(frequencydictionary)
	#print frequencydictionary
	print frequencydictionary[0:n]

top_n_words = get_top_n_words(dictionary, 100)

