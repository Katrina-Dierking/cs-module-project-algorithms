#!/usr/bin/python

import sys

def making_change(amount, denominations):
  # Your code here
  #if we are making change for 10 cents, we could give them a penny, which would take off 9 cents, we can give dimes, or nickles
  # we're doing n-1 or n-5 or n-10, etc instead of cookie scenario
  

  pass


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")