"""
open() - To open file
file: path to file
mode - r/w/a, bin/text
encoding - Text encoding, python choses default encoding

Getting encoding right is very important
Its better to get default encoding
"""

import sys

print(sys.getdefaultencoding())

# To open a file
f = open('Test.txt', mode='wt', encoding='utf-8')
"""
Modes
r - Read
w - Write
a - Append
x - open for exlusive creation, failing if the file exists
b - Binary mode
t - Text(default)
+ - Open disk file
U - Universal new lines mode
"""

# Writing to the file
f.write('Hai friends this is first program for file operations\n')
f.write("Enjoy the new World!")
f.close()


"""
Reading the file
Mode : rt - read text
"""
g = open('Test.txt', mode='rt', encoding='utf-8')
print(g.read())      # reads all text
# print(g.read(33))    # No of bytes to read

# g.close() # To close the file after reading is completed.

# What if you want to move the pointer to first place.
g.seek(0)
print(g.readline())    # To read line by line
print(g.readline())    # To read 2nd line

# Read all lines but return in form of a list
g.seek(0)   # Move to start of file
print(g.readlines())   # reads and returns all lines as list


