def fib(n):
    #basecase
    if n == 1 or n == 0:
        return 1
    #recursive case
    else:
        return fib(n-1) + fib(n-2)
    
    #the problem with this is that the "tree" gets really big very quickly
    #we make the same recursive call over and over again
    #tree grows every time n goes up by 1
    #doesn't run fast
    #see picture (fibonocchi)
    
print (fib(5))
print(fib(15))
print(fib(30))

#looking at the tree again (picture)
#doing the same thing over again unnecessarily slows it down
#no need to make a recursive call repeatedly. 

#Cache = stores data (something)
#as we calculate the terms in the fib, we could be caching something
#


def fib_mem(n, cache = {}):  #adding as argument, it can be added between all the recursive function calls
    #makes it "global"

    #basecase
    if n == 1 or n == 0:
        return 1
    #recursive case
    elif n in cache.keys(): #check the cache to see if a value is in it using a key
        return cache[n] 
    else:
        value = fib_mem(n-1) + fib_mem(n-2)
        cache[n] = value
        return value
    
    
    #see fib2 picture
print (fib_mem(5))
print(fib_mem(15))
print(fib_mem(30))