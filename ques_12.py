# Write a Python program to remove a key from a dictionary.

myDict = {'a':1,'b':2,'c':3,'d':4}
# myDict.pop('a')
# print(myDict)



#Another method
if 'a' in myDict:
    del myDict['a']
print(myDict)