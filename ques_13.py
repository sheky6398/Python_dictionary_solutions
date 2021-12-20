# Write a Python program to map two lists into a dictionary.


keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
d = {}
for i,j in zip(keys,values):
    d[i]=j
print(d)