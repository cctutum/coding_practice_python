
# Given an array (1 to n), find the missing integer
# O(n) time complexity, O(1) space complexity
# Example: [1, 2, 6, 7, 9, 3, 4, 10, 8] is given and 5 is missing

a = [10, 8, 1, 2, 6, 7, 9, 3, 4, 1, 2]

#%% Generate a list of random integers
import random

n = 10
def randomIntegerList(n):
    a = list(range(1, n))
    random.shuffle(a)
    missing = a[0]
    return a[1:], missing

print(f"Given list: {randomIntegerList(n)[0]}, missing {randomIntegerList(n)[1]}")

#%% If we are allowed to use sorted() function

def find_missing(x):
    y = sorted(x)
    for i in range(len(y)-1):
        if y[i+1] - y[i] > 1:
            return y[i]+1
        
print(f"Missing integer is {find_missing(a)}")
    