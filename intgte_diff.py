#Two functions which calculate the integral and differential of given functions over a given value.

import sys
def sqr(x):
	return x*x

def cube(x):
	return x*x*x

def integrate(fn,l,u):
	a=0
     	x=l
     	while x<u:
             a=a+fn(x)*0.01
             x=x+0.01
     	return a
	print a

def differentiate(fn,x):
    a = (fn(x+0.001)-fn(x))/0.001  #this is the implimentation of the differentiation. Note that 0.001 tends to zero.
    return a
    print a

fn=raw_input()

