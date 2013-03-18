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
		if i ==(len(corpus)-3):
			break
		key = ' '.join(corpus[i:i+2])
		if key not in dictionary:
			dictionary[key] = [corpus[i +2]]
			print "Words not in dictionary", words
		else:
			print "Words in dictionary", words
	 		#appends changes the list
			dictionary[' '.join(corpus[i:i+2])].append(corpus[i+2])
		i += 1
	print 'TYPE!!!',type(dictionary[key])	
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

	# def next_word(dictionary, current_word):
	# 	next_word = dictionary[first_word][randint(0, len(dictionary[first_word]) - 1)]
	# 	return next_word

	"""Takes a dictionary of markov chains and returns random text
	based off an original text."""
	# for pair in range(0, 2):
	first_word = random.choice(chains.keys())
		#random_text = chains[first_word] #this value is an array
	random_int = chains[first_word][randint(0, len(chains[first_word]) - 1)]
	print first_word, random_int,
	# random_text = chains[first_word[randint(0,len(chains[first_word])]
	# first_word = first_word + next_word(chains, first_word)


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
