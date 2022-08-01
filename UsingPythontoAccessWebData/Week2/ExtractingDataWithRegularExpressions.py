import re

# version_1

file = open('/Users/vadim/Documents/PythonForEverybody/UsingPythontoAccessWebData/Week2/regex_sum_1584015.txt')
nums = list()
text = file.read()
number = re.findall('[0-9]+', text)
for num in number:
    nums.append(float(num))

print (sum(nums))


# version_2

file = open('/Users/vadim/Documents/PythonForEverybody/UsingPythontoAccessWebData/Week2/regex_sum_1584015.txt')
print (sum([float(num) for num in re.findall('[0-9]+', file.read())]))