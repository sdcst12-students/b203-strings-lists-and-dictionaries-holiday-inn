#!python3

"""
Write a python script display the values of the dictionary
  1. that are sorted by their keys (ascending values) 
  2. that are sorted by their values (ascending) 
  
(3 points)
"""
sortMe = {1: -2, 2: 6, 4: 0, 6: 1, 9: 2, 10: 3, 11: 0, 13: 3, 14: 4, 15: -2, 17: 0, 18: -1, 20: 3}
keys = []
vals = []
for i in sortMe:
    vals.append(sortMe[i])
  
vals.sort()

for i in vals:
    for j in sortMe:
        if i == sortMe[j] and j not in keys:
          keys.append(j)
print(keys)
print(vals)
