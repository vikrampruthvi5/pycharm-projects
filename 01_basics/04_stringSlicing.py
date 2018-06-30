user = "Pruthvi Vikram"
'''Strings are by default converted into arrays.'''

# Accessing individual characters from string
print (user[2])  # print char u
print (user[-2]) # print character 'a' (- 1 is last next to last is -2)

# : for slicing
# Here 2 is not the index after colon
print ( user[2:] ) # print from 2nd character till the end
print ( user[:2] ) # print from 1st character till the 2nd
print ( user[2:4] ) # print from 2nd character till the 4th

# To print Pruthvi print from 0 to 7 or start to 7
print(user[:7])
print(user[0:7])

# Identify length of string
print(len(user))
print(len(user[:7]))
