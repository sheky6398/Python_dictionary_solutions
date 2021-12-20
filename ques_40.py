# Write a Python program to convert a list of dictionaries into a list of values corresponding to the specified key. Go to the editor
# Sample Output:
# Original list of dictionaries:
# [{'name': 'Theodore', 'age': 18}, {'name': 'Mathew', 'age': 22}, {'name': 'Roxanne', 'age': 20}, {'name': 'David', 'age': 18}]
# Convert a list of dictionaries into a list of values corresponding to the specified key:
# [18, 22, 20, 18]

d = [{'name': 'Theodore', 'age': 18}, {'name': 'Mathew', 'age': 22}, {'name': 'Roxanne', 'age': 20}, {'name': 'David', 'age': 18}]
l = []
for i in d:
    for j in i.values():
        if isinstance(j,int):
            l.append(j)
print(l)