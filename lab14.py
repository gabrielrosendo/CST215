import random

d1 = []
d1copy = []
B = []
C = []
n = int(input("Enter total ammount of cards: "))
for i in range(1,n+1):
    d1.append(i)
    d1copy.append(i)
print('Original Deck:\n' , d1)
for i in range(n):
    rand1 = random.choice(d1)
    B.append(rand1)
    d1.remove(rand1)
    rand2 = random.choice(d1copy)
    C.append(rand2)
    d1copy.remove(rand2)
count = 0
for k in range(n):
    if(B[k] == C[k]):
        count+=1
print('After First Draw:\n' , B)
print('After Second Draw:\n' , C)
print('There are' , count , 'Fixed Points')