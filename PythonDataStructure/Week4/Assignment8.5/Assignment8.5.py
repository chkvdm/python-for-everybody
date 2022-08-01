fname = input("Enter file name: ")
# /Users/....../Assignment8.5/mbox-short.txt

fh = open(fname)
count = 0
for line in fh:
    if not line.startswith('From '):
        continue
    words = line.split()
    if len(words) < 2:
        continue
    count += 1
    print (words[1])

print("There were", count, "lines in the file with From as the first word")