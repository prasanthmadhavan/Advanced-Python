#! usr/bin/env python
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
#Find out using a Python program

from math import *
def factor(x):
	if 600851475143%x==0:
		return 1
a=filter(factor,range(2,int(sqrt(600851475143)))) # func factor(x) given valuess in the range defined by range()
print a  			# a will contain only those factors that are a factor of 600851475143.

def pf(x):
	d=range(2,int(sqrt(x)))
	value=0
	for i in d:
		if x%i==0:
			value=0
			break
		else:
			value=1
	return value
ans=filter(pf,a)    # pass a and pf() through a function. Filter output contains only those numbers which returns a !=0.
print ans
print ans[-1]
