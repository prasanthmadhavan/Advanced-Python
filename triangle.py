# This is a Euler Probem.
# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7^(th) triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

#Let us list the factors of the first seven triangle numbers:

#     1: 1
#     3: 1,3
#     6: 1,2,3,6
#    10: 1,2,5,10
#    15: 1,3,5,15
#    21: 1,3,7,21
#    28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?

# the logic used here is simple. the number of factors upto the root of a number is half the factors of the full number.
# hence this logic helps to speed up the algorithm.


def triangle():
  s=4
  b = div(s)
  while len(b)<250:
    s=s+12   
    b = div(s)
    print s,2*len(b)

  if len(b) >= 250:
    print s,2*len(b)

def div(a):
  b=[]
  limit = reduce(lambda x,y: x+y,range(1,a))
  for x in range(1,int(pow(limit,0.5))):
    if not limit%x: b.append(x)
  return b

triangle()
