#!/usr/bin/env python

# markov chains text gen
# gm@stackunderflow.com

import os, re, json, random, time

f = open("markov_out.json",'r')

markov = json.loads(f.read())
f.close()

userlist = markov.keys()


def getmessage():
	user = random.choice(userlist)
	if markov[user].keys():
		word = random.choice(markov[user].keys()) # pick an initial word
	else:
		return ""
	message = "< %s> " % user
	for i in range(30):
		message += word + " "
		if word in markov[user]:
			nextwords = markov[user][word]
			if len(nextwords):
				nextword_weighted_array = []
				for nextword in nextwords.keys():
					for i in range(nextwords[nextword]):
						nextword_weighted_array += [nextword]
				nextword = random.choice(nextword_weighted_array)
				word = nextword
		else:
			break
	return message

if __name__ == "__main__":
	while 1:
		print getmessage()
		time.sleep(1)