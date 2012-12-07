#!/usr/bin/env python

import os, re, json, random, time

f = open("markov_out.json",'r')

markov = json.loads(f.read())
f.close()

userlist = markov.keys()


while 1:
	user = random.choice(userlist)
	if markov[user].keys():
		word = random.choice(markov[user].keys()) # pick an initial word
	else:
		pass
	print "< %s> " % user,
	for i in range(30):
		print word,
		if word in markov[user]:
			nextwords = markov[user][word]
			if len(nextwords):
				nextword_weighted_array = []
				for nextword in nextwords.keys():
					for i in range(nextwords[nextword]):
						nextword_weighted_array += [nextword]
				#print nextword_weighted_array
				nextword = random.choice(nextword_weighted_array)
				word = nextword
		else:
			break
	print ""
	time.sleep(1)