#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # Make the starting variables to check which item is the smallest in the array, and which difference is the largest in the array 
  small = prices[0]
  difference = prices[1] - prices[0]
  # For the length of the array check all values aside from the initial value, since that has already been set as the smallest
  for x in range(1, len(prices)-1):
    # If there is a new smallest found swap
    if prices[x-1] < small:
      small = prices[x-1]
    # If a new high difference has been found then swap
    if prices[x] - small > difference:
      difference = prices[x] - small
  return difference


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))