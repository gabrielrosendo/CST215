#Gabriel Marcelino
#This is my own work
#9/15/22
#Lab Question 2

import random

# create empty sets
set_1 = set()
set_2 = set()
set_3 = set()
# populate sets with random ints from 0 to 100
for j in range(3):
    set_1.add(random.randint(0,100))
for j in range(3):
    set_2.add(random.randint(0,100))
for j in range(3):
    set_3.add(random.randint(0,100))
# print sets
print(set_1)
print(set_2)
print(set_3)

# print cartesian products
cart_prod = [(a,b,c) for a in set_1 for b in set_2 for c in set_3]
print(cart_prod)


        
