#!/usr/bin/env python
# markov chains IRC bot
# gm@stackunderflow.com

import markovtextgen
import time, asyncore
from thread import *
from ircasync import *
import random

channel = "#compsci.bots"

def handle_welcome(_,__):
	start_new_thread(markovpost, (irc,))

def markovpost(irc):
	while True:
		time.sleep(random.uniform(1,5))
		irc.tell(channel, markovtextgen.getmessage().encode("ascii",errors="ignore"))

irc = IRC(nick="markovbot", start_channels=[channel], version="1.0")
irc.make_conn("irc.freenode.net", 6667)
irc.bind(handle_welcome, RPL_WELCOME)
asyncore.loop()


