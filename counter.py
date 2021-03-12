"""
count how many times the character occurs in a string 
"""


string = 'banana'

dct = {list(set(string))[i] : list(string).count(string[i]) for i in range(len(set(string)))}

print(dct) # output: {'b': 1, 'a': 3, 'n': 2}
