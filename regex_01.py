# Some Regex Practice

# Given a long string containing words
string = 'apple orange pear pineapple durian crabapple redapple banana'

# We want to replace every word ending with "apple" with the word "pie"
# Result = 'pie orange pear pie durian pie pie banana'

#%% Version-1: Solving without regex

# decompose the string into a list of words
string2list = []
temp_word = ""
for i, letter in enumerate(string):
    if letter != " ":
        temp_word += letter
    elif letter == " ":
        string2list.append(temp_word)
        temp_word = ""
string2list.append(temp_word)
            
# action
new_string = ""
for idx, word in enumerate(string2list):
    if "apple" in word:
        new_string += "pie "
    else:
        new_string += f"{word} "          
new_string = new_string[:-1]
        
# Two-step procedure
print(new_string)

#%% Version-2: Combine two for-loops into 1 from Version-1

temp_word = ""
new_string = ""

for i, letter in enumerate(string):
    if letter != " ":
        temp_word += letter
    elif letter == " ":
        if "apple" in temp_word:
            new_string += "pie "
        else:
            new_string += f"{temp_word} "  
        temp_word = ""
new_string += temp_word    
print(f"Print strings for comparison:\n{string}\n{new_string}")
        
#%% Solving with regex








