## Finding Numbers in a Haystack.  

In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

Data Files.  
Actual data you need to process for the assignment.  
Actual data: http://py4e-data.dr-chuck.net/regex_sum_1584015.txt (There are 71 values and the sum ends with 334).  
Make sure to save the file into the same folder as you will be writing your Python program.

Handling The Data.  
The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.