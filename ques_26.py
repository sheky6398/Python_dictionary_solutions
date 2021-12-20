# Write a Python program to remove spaces from dictionary keys.

d = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
print({i.replace(" ",""):j for i,j in d.items()})