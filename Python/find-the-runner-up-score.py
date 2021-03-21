"""
author   :   cyberwr3nch
date     :   21st March 2021
platform :   hackerrank.com
"""

if __name__ == '__main__':
    n = int(input())
    # The map() function executes a specified function for each item in an iterable. 
    # input() - gets the input
    # split() - makes a list by seperating elements based on " "{space}
    # the map() splits the input by space and performs int() on each of the items 
    arr = map(int, input().split())
    
    # your code goes here
    # logic: sort the input, and index from last. The second charcter form the last is the runners up score
    # first we remove the duplicate entries in the arr map item with the set()
    # now as the set() changes the type from map item to set item
    # we can convert the set item to an list object to index the items
    # now we have a indexable list with no duplicate values now lets sort the list and index the second item from the last to get the runners up score sorted()[-2]
    print(sorted(list(set(arr)))[-2])
    
    # input: 
    # 5
    # 2 3 6 6 5
    
    # Expected ouput
    # 5
