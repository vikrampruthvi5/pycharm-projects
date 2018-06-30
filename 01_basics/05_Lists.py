# Lists are mutable in python

'''List creation'''
players = [10, 12, 29, 39, 93]

'''Accessing values from list'''
# List in python uses indexing
print(players)  # prints all values
print(players[2])  # Print 2nd value in list i.e. 29

# Modify value in the list
# eg. replace 29 with 49
players[2] = 49
print(players[2])

'''Appending values to list'''
# Appends value at the last
players + [99]  # This is doesn't change the list permanently
players.append(99)  # This makes permanent change to the list
print(players)
players

'''Multiple replacements'''
players[0], players[len(players)-1] = [0, 100]
print(players)

'''Sort lists'''
players.sort()
print(players)

'''Pop - remove last value from list'''
for i in range(1, 3):
    players.pop()   # Removes last value
    print(players)

'''Count number of occurrences of x in list'''
players.append(12)
print(players.count(12))

'''Other'''
players *= 2        # Multiply list contents by 2
print(players)
players.reverse()   # Reverse contents of list
# Can also be written as list.reverse(players)
print(players)

