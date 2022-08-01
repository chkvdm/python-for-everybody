# Use words.txt as the file name

fname = input("Enter file name: ")
# /Users/...../Assignment7.1/words.txt

fh = open(fname)
for line in fh:
    print ((line.rstrip()).upper())