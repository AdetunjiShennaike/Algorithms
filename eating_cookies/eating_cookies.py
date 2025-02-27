#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  # if n == 0 or n == 1:
  #   return 1
  # elif n == 2:
  #   return 2
  # if n > 2:
  #   return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

  # Fibonacci with 3 items for recursive no cache
  
  cache = cache or [0]*(n+1)

  return cache

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')