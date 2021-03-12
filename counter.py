"""
count how many times the character occurs in a string 
"""

string = 'banana'

lst = sorted(list(set(string)))
dct = {lst[i] : string.count(lst[i]) for i in range(len(set(string)))}

print(dct)
