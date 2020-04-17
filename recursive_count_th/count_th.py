'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    th =2
    i = 1
    if len(word) < 1:
        return 0
    
    if word[:th] == 'th':
        return 1 + count_th(word[i:])
    else:
        return 0 + count_th(word[i:])

  
    
# must use recursion! no loops 
# establish base case
# find ONLY the 'th' in word
# setup a counter for each iteration of "th"
