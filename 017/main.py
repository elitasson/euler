#!/bin/py

"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

def numberLetter(n):

	sumv = 0
	#example: 123
	a = int(n/100)			#1
	b = int(n/10 % 10)		#2
	c = int(n % 10)			#3
	d = int(n % 100)		#23

	if a != 0:
		sumv += dic[a] + len("hundred")
		if d != 0:
			sumv += len("and")
	if d < 20 and d != 0:
		sumv += dic[d]
	elif d != 0:
		sumv += dic[b*10]
		if c != 0:
			sumv += dic[c]

	return sumv


dic = {}
dic[1] = len("one")
dic[2] = len("two")
dic[3] = len("three")
dic[4] = len("four")
dic[5] = len("five")
dic[6] = len("six")
dic[7] = len("seven")
dic[8] = len("eight")
dic[9] = len("nine")
dic[10] = len("ten")
dic[11] = len("eleven")
dic[12] = len("twelve")
dic[13] = len("Thirteen")
dic[14] = len("fourteen")
dic[15] = len("Fifteen")
dic[16] = len("sixteen")
dic[17] = len("seventeen")
dic[18] = len("eighteen")
dic[19] = len("nineteen")
dic[20] = len("twenty")
dic[30] = len("thirty")
dic[40] = len("forty")
dic[50] = len("fifty")
dic[60] = len("sixty")
dic[70] = len("seventy")
dic[80] = len("eighty")
dic[90] = len("ninety")

sumv = 0
for i in range(1, 1000):
	
	sumv += numberLetter(i)

print(sumv + len("one") + len("thousand"))

