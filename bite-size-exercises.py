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
    x_count = string.count('x')
    o_count = string.count('o')
    return x_count == o_count

print(compare_Numbers("RXxloxe vOwXls with nuxXxrs bxsOd ox thoir position in the olohxOxOX"))

#%%

# Check if a string only contains digits and spaces

def CheckDigitsSpaces(string):
    digit_count = 0
    space_count = 0
    for char in string:
        if char.isdigit():
            digit_count += 1
        elif char == ' ':
            space_count += 1
    return len(string) == digit_count + space_count

print(CheckDigitsSpaces("Replace vowels with numbers based on their position in the alphabet"))

#%%

# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time

def TimeConversion(string):
    am_pm = string[-2:]
    hour, minute, second = map(int, string[:-2].split(':'))
    if am_pm == 'PM' and hour != 12:
        hour += 12
    elif am_pm == 'AM' and hour == 12:
        hour = 0
    return f'{hour:02d}:{minute:02d}:{second:02d}'
    
print(TimeConversion("12:34:56 AM"))

#%%

# Check if a given string is a palindrome (reads the same forward and backward)

def isPalindrome(string):
    return string == string[::-1]

print(isPalindrome("apfggfpa"))

#%%

# Find the length of the longest increasing subsequence in a given list of integers

def LongestIncreasingSubsequence(arr):
    if not arr:
        return 0
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

print(LongestIncreasingSubsequence([4, 5, 1, 2, 3, 6, 5, 7, 9, 13, 26]))

#%%



