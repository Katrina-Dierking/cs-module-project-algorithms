#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
    # Your code here

    pass


if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')
    
    
    
    def knapsack(weight_limit, items):
      items.sort(key=lambda x:x.value, reverse=True)
      #could be better if we sorted by value/wt ratio
      
      sack = []
      cur_weight = 0
      for i in range(len(items)):
        if cur_weight + items[i].weight <= weight_limit:
          sack.append(items[i])
          
      return sack
    
    #BruteForce
   
      #what to do to generate all combos? 
      #is there a python module we could use? 
      #cocs.pythong.org/ python itertools //permutations//combinations
      #combinations will work best
      
      #PROS: you will find best solution
      #CONS: will take a really long time
      
      #we need to determine what we could be pulling things from 
     
     #create an empty list to save combos
    import itertools
     
    def sack_brute(weight_limit, items):
      all_combos = []
     
     #how many different items are allowed to be in our combos? 
     #there is no limit. (n)
     
      for i in range(1, len(items) + 1):
       #why are we starting at 1 instead of 0
       #we want to create all the combos of 1 item, 2 items, 3 items,etc
       # we are using 1 to signify the number of items and there can't be 0 items
       
        list_of_combos = list(combinations(items, i)) #what items and how many - have to generate all combos
        for combo in list_of_combos:
          #check weight and value - if it exceeds weight limit, we don't have to add it
          all_combos.append(combo)
          #so far, this is very inefficient 
          
        #we have to eliminate everything that exceeds the weight limit
        
        max_value = -1
        best_combo = None
        for combo in all_combos: 
          value = 0 #of entire combo
          weight = 0 #of combo
          for item in combo:
            value += item.value
            weight += item.weight
          if weight <= weight_limit:  #could fit in sack
            if value > max_value:
              max_value = value  
              best_combo = combo
              
        #after searching every combo
        return best_combo
       
      
      
#GREEDY STRATEGY  // would use with maps and navigation. Get a result quickly //good enough
#PROS:
  # faster than brute force
  # smarter than naive approach
  # usually more efficient in space and run time
#CONS:
  #wont' give the best solution. But a good one. 
  #doesn't care about edge cases

def sack_greedy(wt_limit, items):
  for i in items: #look through all items
    i.efficiency - i.value/i.weight #calculate efficiency in linear time. 
    #start off with items with most value but least weight
    #adds wt to wt counter and checks it. Only if it's acceptable does it add it to the sack .
    
    
  items.sort(key=lambda x:x.efficiency, reverse= True) #sort smallest to largest
  
  sack = [] 
  weight = 0
  for i in items: 
    weight += i.weight
    if weight > wt_limit:
      return sack
    else:
      sack.append(i)
      
  return sack
    