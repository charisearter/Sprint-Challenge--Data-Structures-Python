import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = set(f.read().split("\n"))  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = set(f.read().split("\n"))  # List containing 10000 names
f.close()

# Return the list of duplicates in this data structure
'''
listName = [ variableName (declare first) for variableName in WhateverCheckingA if variableName in WhateverCheck2IcompareItto]

my runtime was les than 1 second this way
terminal after mulitple tries: 
1. runtime: 0.007040739059448242 seconds
2. runtime: 0.007941007614135742 seconds
3. runtime: 0.0045588016510009766 seconds
4. runtime: 0.005752086639404297 seconds
5. runtime: 0.004940032958984375 seconds

I guess this would be O(n) because it is searching and I think Sets are like Object is Javascript (at least it looks like it to me). 
'''

duplicates = [name for name in names_1 if name in names_2]

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# a.difference_update(b)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
