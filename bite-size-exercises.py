# Given a string, return the string reversed
def ReverseString(string):
    return string[::-1]

print(ReverseString("Apple"))

#%%

# Find the longest word in a string and return its length
def FindLongestWord(string):
    words = string.split()
    longest = max(words, key=len)
    return len(longest)

print(FindLongestWord("Find the longest word in a string and return its length"))

#%%

# Replace vowels with numbers based on their position in the alphabet
def Replace_Vowels_With_Numbers(string):
    vowels = ['a', 'e', 'o', 'u', 'i']
    new_string = []
    for char in string:
        if char.lower() in vowels:
            position = ord(char.lower()) - ord('a') + 1
            new_string.append(str(position))
        else:
            new_string.append(char)
    return "".join(new_string)
    
print(Replace_Vowels_With_Numbers("Replace vowels with numbers based on their position in the alphabet"))

#%%

# Determine if a string has the same number of 'x' and 'o' characters

def compare_Numbers(string):
    xs, os = 0, 0
    for char in string:
        if char.lower() == 'x':
            xs += 1
        elif char.lower() == 'o':
            os += 1
    return xs, os

print(compare_Numbers("RXxloxe vOwXls with nuxXxrs bxsOd ox thoir position in the olohxOxOX"))

#%%