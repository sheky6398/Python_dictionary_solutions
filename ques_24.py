# Write a Python program to count the values associated with key in a dictionary.


student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]

# sum =0
# for i in student:
#     for j in i.values():
#         if isinstance(j,int):
#             sum+=j
# print(sum)

#Another Method
print(sum(d['id'] for d in student))
print(sum(d['success'] for d in student))