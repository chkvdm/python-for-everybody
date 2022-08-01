# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
# /Users/.../Assignment7.2/mbox-short.txt

fh = open(fname)
count = 0
val = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count += 1
    val += float(line[line.find('0'): ])

print('Average spam confidence: ' + str(val / count))