# Write a Python program to convert more than one list to nested dictionary.

l1,l2,l3 = ['S001', 'S002', 'S003', 'S004'],['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards'],[85, 98, 89, 92]


d = {}
for (i,j,k) in zip(l1,l2,l3):
    d[i]={j:k}
print(d)

#Another Method
print([{i:{j:k}} for (i,j,k) in zip(l1,l2,l3)])
