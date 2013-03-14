#!/usr/bin/env python

import sys

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    dictionary = {}
    corpus = corpus.split()
    corpus.append(" ")
    i = 1
    for words in corpus:
        dictionary[words] = corpus[i]
        i += 1
        if i == (len(corpus) - 1):
            break
    print dictionary

    return dictionary

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    return "Here's some random text."

def main(argv):
    args = sys.argv
    # argv = script, filename
    script, filename = argv

    #opens txt file form command line
    input_text = open(filename).read()
    make_chains(input_text)

    chain_dict = make_chains(input_text)
    #random_text = make_text(chain_dict)
    #print random_text

if __name__ == "__main__":
    main(sys.argv)
