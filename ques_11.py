# Write a Python program to multiply all the items in a dictionary.

mul = 1
my_dict = {'data1':100,'data2':-54,'data3':247}
for i in my_dict.values():
    mul*=i
print(mul)
