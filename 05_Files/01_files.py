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
