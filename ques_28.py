#  Write a Python program to get the key, value and item in a dictionary.

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("key value count")
for i,(j,k) in enumerate(d.items(),1):
    print(i," ",j," ",k)