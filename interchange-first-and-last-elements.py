# 1. Using temporary variable
def swap_first_last(lst):
    if len(lst) < 2:
        return lst
    tmp = lst[0]
    lst[0] = lst[-1]
    lst[-1] = tmp
    return lst


# 2. Using indexing
def swap_first_last_v2(lst: list) -> list:
    if len(lst) < 2:
        return lst
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst


# 3. Using list slicing
def swap_first_last_v3(lst: list) -> list:
    if len(lst) < 2:
        return lst
    return lst[-1:] + lst[1:-1] + lst[:1]


functions = [swap_first_last, 
             swap_first_last_v2,
             swap_first_last_v3]


for f in functions:
    print(f(list(range(7))))