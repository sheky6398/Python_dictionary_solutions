# Write a Python program to create a dictionary from a string. Go to the editor
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

dict ={}
d = 'w3resource'
for i in d:
    if i  in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)


#Another method
from collections import Counter
print(Counter(d))