fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    word_line = line.split()
    for word in word_line:
        if word not in lst : lst.append(word)
lst.sort()
print(lst)