#  Write a Python program to sort Counter by value. Go to the editor
# Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
# Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]

d = {'Math':81, 'Physics':83, 'Chemistry':87}
l = []
for i in sorted(d.items(),key=lambda x:x[1],reverse=True):
    l.append(i)
print(l)