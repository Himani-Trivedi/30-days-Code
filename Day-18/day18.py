# Day 18: In the GitHub repository, Infinity-AI(Infinite Learn and Grow)/30-days-code inside the Day-18 folder create your_name.py 
# file as defined in the readme.md file.

# 1. Write a pattern which identifies if a string is a valid python variable



import re


def is_valid_variable(name):
    pattern=re.compile("^([a-z]|[A-Z]|_)([a-z]|[A-Z]|[0-9]|_)*$")
    match=pattern.match(name)
    if match: 
        print(True)
    else:
        print(False)

is_valid_variable('first_name') # True
is_valid_variable('first-name') # False
is_valid_variable('1first_name') # False
is_valid_variable('first 89name') # False
is_valid_variable('firstname') # True

# 2. Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(sen):
    repalce=''
    patten=re.compile(r"[^a-zA-Z\s]")
    new_sen=re.sub(patten,repalce,sen)
    return new_sen

# [^a-zA-Z\s] means any character that IS NOT a-z OR A-Z or white space
print(clean_text(sentence));

# I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
# print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
