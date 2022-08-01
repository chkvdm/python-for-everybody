fname = input("Enter file name: ")
# /Users/vadim/Documents/PythonForEverybody/PythonDataStructure/Week4/Assignment8.4/romeo.txt

fh = open(fname)
words = list()
for line in fh:
    string_lst = line.split()
    for word in string_lst:
        if word not in words:
            words.append(word)
words.sort()

print(words)