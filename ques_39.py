# Write a Python program to get the total length of all values of a given dictionary with string values. Go to the editor
# Original dictionary:
# {'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
# Total length of all values of the said dictionary with string values:
# 20

d = {'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
print(sum(map(len,d.values())))


#Another Method
sum = 0
for i in d.values():
    sum+=len(i)
print(sum)
