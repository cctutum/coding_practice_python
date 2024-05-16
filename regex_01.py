# Some Regex Practice

# Given a long string containing words
string = 'apple orange pear pineapple durian crabapple redapple banana'

# We want to replace every word ending with "apple" with the word "pie"
# Result = 'pie orange pear pie durian pie pie banana'

#%% Version-1: Solving without regex
# Use type hinting

def replace_words_inString_twoLoops(string: str, 
                                    word2remove: str, 
                                    word2replace: str) -> str:
    
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
                
    # replace word2remove with word2replace
    output = ""
    for idx, word in enumerate(string2list):
        if word2remove in word:
            output += f"{word2replace} "
        else:
            output += f"{word} "          
    output = output[:-1]
    return output
        
# Two-step procedure
output = replace_words_inString_twoLoops(string, 
                                         word2remove= "apple", 
                                         word2replace= "pie")
print(f"Print strings for comparison (Version-1):\n{string}\n{output}")

#%% Version-1.1: Use positional and keyword arguments in function definition

def replace_words_inString_twoLoops_args(*args, **kwargs):
    
    string = args[0]
    word2remove = kwargs['word2remove']
    word2replace = kwargs['word2replace']
    
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
                
    # replace word2remove with word2replace
    output = ""
    for idx, word in enumerate(string2list):
        if word2remove in word:
            output += f"{word2replace} "
        else:
            output += f"{word} "          
    output = output[:-1]
    return output
        
# Two-step procedure
output = replace_words_inString_twoLoops_args(string, 
                                              word2remove= "apple", 
                                              word2replace= "pie")
print(f"\nPrint strings for comparison (Version-1.1):\n{string}\n{output}")

#%% Version-2: Combine two for-loops into 1 from Version-1

def replace_words_inString_oneLoop(string: str, 
                                   word2remove: str, 
                                   word2replace: str) -> str:

    temp_word = ""
    output = ""
    
    for i, letter in enumerate(string):
        if letter != " ":
            temp_word += letter
        elif letter == " ":
            if "apple" in temp_word:
                output += "pie "
            else:
                output += f"{temp_word} "  
            temp_word = ""
    output += temp_word    
    return output
    
output = replace_words_inString_oneLoop(string, 
                                        word2remove= "apple", 
                                        word2replace= "pie")
print(f"\nPrint strings for comparison (Version-2):\n{string}\n{output}")

#%% Version-3: Another one-loop version

def replace_words_inString(string: str,
                           word2remove: str,
                           word2replace: str) -> str:

    output = ''
    words = string.split() # this exactly performs the first loop in Version-1
    for word in words:
        if word.endswith(word2remove):
            output += f"{word2replace} "
        else:
            output += f"{word} "
    return output.strip()

output = replace_words_inString(string, 
                                word2remove= "apple", 
                                word2replace= "pie")
print(f"\nPrint strings for comparison (Version-3):\n{string}\n{output}")

#%% Solving with regex








