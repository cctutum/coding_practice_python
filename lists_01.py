
# Given an array (1 to n), find the missing integer
# O(n) time complexity, O(1) space complexity
# Example: [1, 2, 6, 7, 9, 3, 4, 10, 8] is given and 5 is missing

# a = [10, 8, 1, 2, 6, 7, 9, 3, 4, 1, 2]

import random

def generate_random_integer_list(n):
    # Generate a shuffled list of random integers (1 to n)
    a = list(range(1, n))
    random.shuffle(a)
    missing = a[0]
    return a[1:], missing

def find_missing_int(x):
    # Find the missing integer in a given list (sorted() is used)
    y = sorted(x)
    for i in range(len(y)-1):
        if y[i+1] - y[i] > 1:
            return y[i]+1


if __name__ == "__main__":
    
    n = 10
    given_list, missing = generate_random_integer_list(n)
    print(given_list, missing)
    print(find_missing_int(given_list))
    
    