name = input("Enter file: ")
# File name: mbox-short.txt.
# The file is not in the list because the assignment was run online. 
# Downloading the file is not provided by the condition.

handle = open(name)
from_val = dict()
for line in handle:
    if not line.startswith('From '):
        continue
    words = line.split()
    if len(words) > 2:
        from_val[words[1]] = from_val.get(words[1], 0) + 1

most_sender = " "
most_val = 0
for key,val in from_val.items():
    if val > most_val:
        most_sender = key
        most_val = val
    
print(most_sender, most_val)