#!/usr/bin/env python

import os, re, json, sys

logpath = "logs/"
loglist = os.listdir(logpath)
#loglist = [loglist[0]]

msg_re = re.compile("^[0-9][0-9]:[0-9][0-9]:[0-9][0-9]<.(.*?)> (.*)$")
underscores_re = re.compile("^(.*?)(_*)$")

markovtable = {}

sameusers_map = {}
if os.path.exists("sameusers"):
	sameusers = open("sameusers",'r').read().split("\n")
	for userlist in sameusers:
		userlist = userlist.split(" ")
		if len(userlist) > 1:
			for sameuser in userlist[1:]:
				sameusers_map[sameuser] = userlist[0]

for log in loglist:
	print "Reading %s" % (logpath + log)
	f = open(logpath + log, 'r')
	logcont = f.read().split("\n")
	for line in logcont:
		line = line.decode("UTF-8", errors="ignore")
		result = msg_re.match(line)
		if result:
			user = underscores_re.match(result.group(1)).group(1)
			if user in sameusers_map:
				user = sameusers_map[user]
			msg = result.group(2)
			#print "user %s, msg %s" % (user,msg)
			if not user in markovtable:
				markovtable[user] = {}
			msg = msg.split(" ")
			for i, word in enumerate(msg[:-1]):
				nextword = msg[i+1]
				#print "%s -> %s" % (word, nextword)
				if not word in markovtable[user]:
					markovtable[user][word] = {}
				if not nextword in markovtable[user][word]:
					markovtable[user][word][nextword] = 0
				markovtable[user][word][nextword] += 1
	f.close()
				

print "writing"

tableout = json.dumps(markovtable)
f = open("markov_out.json",'w')
f.write(tableout)
f.close()

f = open("userlist",'w')
f.write("\n".join(sorted(markovtable.keys())))
f.close()
