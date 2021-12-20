# Write a Python program to count number of items in a dictionary value that is a list.

dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
print((sum(map(len,dict.values()))))

#Another Method
sum = 0
for i in dict.values():
    for j in i:
        sum+=1
print(sum)
