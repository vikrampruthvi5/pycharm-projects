""" For loop """

#count = int(input("Enter value: "))
count = 4

#Ranges from 1 to 4 automatically
for i in range(count):
    print("Pruthvi Vikram - Samyuktha")

# Ranges from 2 to 4
for i in range(2, count):
    print("Samyuktha")

# with incrementation
for i in range(10, 50, 10):
    print(i)

#Dealing with Strings
foods = ["berries", "juice", "watermelon", "bananas", "beer"]

for j in foods:
    print(j)
    print(len(j))