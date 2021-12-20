# . Write a Python program to sum all the items in a dictionary

my_dict = {'data1':100,'data2':-54,'data3':247}
print(sum(my_dict.values()))


#Another method
sum = 0
for i,j in my_dict.items():
    sum+=j
print(sum)