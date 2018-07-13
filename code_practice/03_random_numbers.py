
import random as rand

val = []
i = 0

while i < 10:
    r = rand.randrange(1, 12)
    if r not in val:
        val.append(r)
        i += 1


for n in val:
    print(n)