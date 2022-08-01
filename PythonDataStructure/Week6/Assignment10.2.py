name = input("Enter file: ")
# /Users/...../Assignment8.5/mbox-short.txt

handle = open(name)
hours = dict()
for line in handle:
    if not line.startswith('From '):
        continue
    words = line.split()
    if not len(words) >= 5:
        continue
    time_code = words[5].split(':')
    hours[time_code[0]] = hours.get(time_code[0], 0) + 1

for k,v in sorted(hours.items()):
    print (k, v)