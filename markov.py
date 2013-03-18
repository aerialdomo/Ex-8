#!/usr/bin/env python

import sys
import random
from random import randint

def make_chains(corpus):
	"""Takes an input text as a string and returns a dictionary of
	markov chains."""
	dictionary = {}
	corpus = corpus.lower().split()
	#corpus is a list
	i = 0
	#words not in pairs
	for words in corpus:
		# keeps iterator within bounds of list
		if i ==(len(corpus)-3):
			break

		key = ' '.join(corpus[i:i+2])
		if key not in dictionary:
			dictionary[key] = [corpus[i +2]]
		else:
	 		#appends changes the list
			dictionary[key].append(corpus[i+2])
		i += 1
	print "NEW!!", dictionary

	# i = 1
	# for words in corpus:
	# 	if words not in dictionary:
	# 		#dictionary[words] is the value
	# 		dictionary[words] = [corpus[i]]
	# 	else:
	# 		#appends changes the list
	# 		dictionary[words].append(corpus[i])
	# 	i += 1
	# 	if i == (len(corpus) - 1):
	# 		break
	
	return dictionary

def make_text(chains):


	"""Takes a dictionary of markov chains and returns random text
	based off an original text."""
	first_word = random.choice(chains.keys())
	sentence = first_word


	for i in range(0,3):	
		# loop range(x,y) times
		# get random value from key, value is a list
		next_word = chains[first_word][randint(0, len(chains[first_word]) - 1)]
		#making a space " "
		next_word = " " + next_word
		sentence += next_word
		#split string first_word into a list
		split = first_word.split()
		#get second element of list and turns back into a string
		first_word = str(split[1])
		#concatenate first_word and next word
		first_word = first_word + next_word
		
	print "SENTENCE: ", sentence



def main(argv):
	args = sys.argv
	script, filename = argv

	#opens txt file form command line
	input_text = open(filename).read()
	dictionary = make_chains(input_text)

	random_text = make_text(dictionary)
	# print random_text

if __name__ == "__main__":
	main(sys.argv)
