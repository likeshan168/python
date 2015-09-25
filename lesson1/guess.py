#!/usr/bin/env python
# -*- coding:utf-8 -*-
# filename guess.py

true_num = 80

guess_num = int(raw_input("\ninput the number:"));

if guess_num > true_num:
	print "sorry, it is greater than that...\n"
elif guess_num < true_num:
	print "sorry, it is less than that...\n"
else:
	print "Amazing, you guessed it...\n"

print "Game will exit: )"

