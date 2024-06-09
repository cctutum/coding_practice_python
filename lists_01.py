
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

def find_missing_int_sorted(x):
    # Find the missing integer in a given list (sorted() is used)
    y = sorted(x)
    if y[0] != 1:
        return 1
    for i in range(len(y)-1):
        if y[i+1] - y[i] > 1:
            return y[i]+1
    return len(x)+1
        
def find_missing_int_naive(lst):
    # SPace complexity is higher
    missing_int_set = set(lst) # space complexity O(n)
    int_set = {i for i in range(1, len(lst)+2)} # space complexity O(n)
    missing_int = int_set.difference(missing_int_set)
    iterator = iter(missing_int)
    return next(iterator) # list(missing_int)[0]

def find_missing_int(lst):
    missing_sum = sum(lst)
    complete_sum = sum([i for i in range(len(lst)+2)])
    return complete_sum - missing_sum

def find_missing_formula(lst):
    missing_sum = sum(lst)
    complete_sum = (len(lst)+1) * (len(lst)+2) / 2 # formula= n*(n+1)/2
    return int(complete_sum - missing_sum)


if __name__ == "__main__":
    
    n = 10 # it starts getting slover at 1000000
    given_list, missing = generate_random_integer_list(n)
    
    print("\nGenerated list and the missing value:")
    print(given_list, missing)
    
    print("\nFirst method: Using sorted()")
    print(find_missing_int_sorted(given_list))
    
    print("\nSecond method (naive): Using set.difference() and iterator")
    print(find_missing_int_naive(given_list))
    
    print("\nThird method: Using sum()")
    print(find_missing_int(given_list))
    
    print("\nFourth method: Using summation formula")
    print(find_missing_formula(given_list))
    
    assert find_missing_int_sorted([9, 6, 8, 2, 4, 7, 3, 5]) == 1
    assert find_missing_int_sorted([7, 3, 8, 6, 4, 5, 2, 1]) == 9