# Write a Python program to drop empty Items from a given Dictionary. Go to the editor
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}

d = {'c1': 'Red', 'c2': 'Green', 'c3': None}
dict = {}
for i,j in d.items():
    if j!=None:
        dict[i]=j
print(dict)
