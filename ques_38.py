#  Write a Python program to count the frequency in a given dictionary. Go to the editor
# Original Dictionary:
# {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
# Count the frequency of the said dictionary:
# Counter({10: 2, 40: 2, 20: 2, 70: 1, 80: 1})

d = {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
dict = {}
for i in d.values():
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)

#Another method
from collections import Counter
print(Counter(d.values()))