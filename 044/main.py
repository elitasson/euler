"""
Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?
"""

"""
n^2-n/3 = 2x/3

n = 1/6 +- sqrt( 1/36 + 2x/3 )

n = 1/6 +- sqrt( 1/36 + 44/3 )
"""

import math as m

def isPentagon(n):
	return (m.sqrt( 1/36 + 2*n/3) + 1/6) % 1 == 0

def pentagon(i):
	return int(i*(3*i-1)/2)

jp = 0
kp = 0
j = 2
found = False
while not found:
	jp = pentagon(j)
	for k in range(1, j):
		kp = pentagon(k)

		if jp != kp and isPentagon(abs(jp-kp)) and isPentagon(jp+kp):
			print(abs(jp-kp))
			exit(0)

	j += 1