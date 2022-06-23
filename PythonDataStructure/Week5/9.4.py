name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

from_val = dict()

for line in handle:
    if not line.startswith('From '): continue
    word = line.split()
    if len(word) > 2:
        from_val[word[1]] = from_val.get(word[1], 0) + 1

most_sender = ""
most_val = 0
for key,val in from_val.items():
    if val > most_val:
        most_sender = key
        most_val = val
        
print(most_sender, most_val)