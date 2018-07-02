
# This program illustrates the difference between continue and break keywords in python

# BREAK
"""
Break keyword is used to skip a loop. For example if you want to print numbers between 1 - 10 and if you want to
stop printing when 6 is found, you can use break in the loop
"""
print("With BREAK")
for i in range(10):
    if i is 6:
        break
    print(i)

# CONTINUE
"""
Continue is similar to break but the only difference is that unlike break, continue just skipps the command execution
instead of completely coming out of the loop 
"""
print("With CONTINUE")
for i in range(10):
    if i is 6:
        continue
    print(i)

""" OUTPUT
With BREAK
0
1
2
3
4
5
With CONTINUE
0
1
2
3
4
5
7
8
9
"""