# Write a Python script to sort (ascending and descending) a dictionary by value.

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print({i:j for i,j  in sorted(d.items(),key=lambda x:x[1])})


#ANother Method
dict = {}
for i,j in sorted(d.items(),key=lambda x:x[1]):
    dict[i]=j
print(dict)

#ANother Method
dict = {}
for i,j in sorted(d.items(),key=lambda x:x[1],reverse=True):
    dict[i]=j
print(dict)


#ANother Method
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print({i:j for i,j  in sorted(d.items(),key=lambda x:x[1],reverse=True)})