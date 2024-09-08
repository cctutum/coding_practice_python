import re

string = "I am about just about to publish an article on Medium.com"

# Question: Find the Platform name (Medium.com)
# result -> Platform: Medium.com

pattern = 'on(.*com).*'
platform = re.search(pattern, string)[1].strip()

print("Platform:", platform)

#%% re.findall()

string = "Mr. Channing went for swimming after dancing from there will head to dining"

# Question: Find a list of all those words in the given sentence, 
# that have "ing" as a substring in them

print(re.findall('\S*ing\S*', string))

#%% re.search()

string = "When the going gets tough, the tough get going"

# Question: Find a list of all "going"s
print(re.search('going', string).start()) # this only gives the index of the first occurence