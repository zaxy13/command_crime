#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time, os, sys

def clear():
	os.system(['clear','cls'][os.name == 'nt'])

def story(words, dstime, speed, end):
	for l in words:
		sys.stdout.write(str(l))
		sys.stdout.flush()
		time.sleep(speed)
	time.sleep(dstime)
	if end == True:
		clear()

def cmdCheck(raw, expe): #maybe
	if raw == expe:
		return True

	elif raw == "zaxy -o":
		print "nope" # bad, this is a side effect
		return True

	else:
		return False

def waitForUser():
	# press any key
	dummy = raw_input("")

def main():
	story("hello world", 1, 0.2, True)
	story("lodind zaxyOS",1, 0.2, False)
	story(".......",2,0.3, False)
	story("............ [DONE]",3,0.2, True)
	print ""
	username = raw_input("username : ")
	print cmdCheck(username, "bob hope")

	return 0

if __name__ == '__main__':
	main()

