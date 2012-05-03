#!/usr/bin/python

import markov
import sys

def main ():
	if len (sys.argv) < 2:
		sys.stderr.write ('Usage: ' + sys.argv [0] + ' text_source [chain_length=1]\n')
		sys.exit (1)

	filename = sys.argv [1]
	markovLength = 1
	if len (sys.argv) == 3:
		markovLength = int (sys.argv [2])

	markov.buildMapping (markov.wordlist (filename), markovLength)
	print markov.genSentence (markovLength)

if __name__ == "__main__":
	main()
	