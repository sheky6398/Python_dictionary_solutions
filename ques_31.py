# Write a Python program to create a dictionary from two lists without losing duplicate values.

class_list = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
id_list = [1, 2, 2, 3]
d = {}
for i,j in zip(class_list,id_list):
    d[i]={j}
print(d)