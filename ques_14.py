# Write a Python program to sort a given dictionary by key.


color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}
d = {}
for i in sorted(color_dict.items(),key=lambda x:x[0]):
    print(i)
    