'''
Input: an integer
Returns: an integer
'''

    # 3 options for first bite
        # 1, 2, or 3 cookies
        # leaves, 2, 1, or 0 left
        # when we have 0 cookies left, I don't have to continue eating
        # if I have 2 left, and I had 1, 2, or 3 I would have 1, 0, or -1 left
        # if 0 is a valid way to eat cookies, + is valid, but - is not
        #any neg number is an invalid path
        #recursion path should end at any case smaller than 1
        # making 3 recursive calls at a time - 12 total
        # so if he could eat 1,2, or 4....would the fibanacci sequence be   (n-4) (n-2) and (n-1)
        
def eating_cookies(n):
    #base case
    if n == 0: #valid
        return 1
     
    elif n < 0: #invalid
        return 0      

    #what are we trying to return - the number of combos for eating the cookies
    #from the description, the number of ways to eat 3 cookies is 4. 
    
    else:
        #make 3 recursive calls
        # if we start off with n = 3
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
