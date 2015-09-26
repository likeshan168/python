#!/usr/bin/env python
# -*- coding:utf-8 -*-
# finename prime.py

def GetPrimeNumber(n):
	"""Get all the prime numbers from 0-n

	It will print all the prime numbers
	"""

	return n % 2 !=0 and n % 3 != 0

print filter(GetPrimeNumber, range(2,25))
