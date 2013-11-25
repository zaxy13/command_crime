#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time, os, sys

def clear():
	 os.system(['clear','cls'][os.name == 'nt'])

def waitForUser(disp):
	# press any key
	dummy = raw_input(disp)

## look in to classes for these funcs ##

def typing(words, speed, disp):
	for l in words:
		sys.stdout.write(str(l))
		sys.stdout.flush()
		time.sleep(speed)
	waitForUser(disp)
	clear()

def story(words, dstime, speed, cler):
	for l in words:
		sys.stdout.write(str(l))
		sys.stdout.flush()
		time.sleep(speed)
	time.sleep(dstime)
	if cler == True:
		 clear()

## end  ##

## functions that use files ##

def prog_ins(level):
	progs = {1:"file browser <files>", 2:"Email reader <email>", 3:"noting" }
	if level == 1:
		for p, prog in progs.items():
			print (p,prog)
	# plan more for add-ons....
	else:
		return -1

def email():
	pass # look in to Json for emails... and other save actions

## end ##

## functions that deal with the commands ##
def cmdCheck(raw, expe): #maybe
	if raw == expe:
		return True

	elif raw == "zaxy -o":
		print "nope" # bad, this is a side effect
		return True

	else:
		return False


def cmdLoop(cmd):
	if cmd == "help" or cmd == "Help" or cmd == "H":
		prog_ins(1)
	elif cmd == "exit":
		return 2
	elif cmd == "email":
		email()
		return 3
	else:
		story("I don't know that, try help for help",2,0.05,True)
		return -1

## end ##

def main():
	story("hello world", 1, 0.2, True)
	while True:
		d = raw_input("zOS:> ")
		print cmdLoop(d)

	return 0

if __name__ == '__main__':
	main()

