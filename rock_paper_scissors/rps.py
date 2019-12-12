#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  length, origin = 3**n, n
  ans = [[] for x in range(0,length)]
  while n > 0:
    count, times = 3**(origin - n), 3**n
    n -= 1
    start = 0
    p = 3**n
    p2, p3 = p*2, p*3 
    if count == 0:
      for x in range(start,p):
        ans[x].append('rock')
      for x in range(p,p2):
        ans[x].append('paper')
      for x in range(p2,p3):
        ans[x].append('scissors')
    while count > 0:
      for x in range(start,p):
        ans[x].append('rock')
      for x in range(p,p2):
        ans[x].append('paper')
      for x in range(p2,p3):
        ans[x].append('scissors')
      start += times
      p += times
      p2 += times
      p3 += times
      count -= 1
  return ans


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')