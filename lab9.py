#Gabriel Marcelino
#This is my own work
#11/4/22
#Lab Question 9

first = int(input("Type the first term of the sequence: "))
dif = int(input("What's the commom difference of the sequence? "))
num = int(input("How many terms should be displayed? "))
curr = first
for i in range(num-1):
    print(curr, end=" ")
    curr+=dif
print(curr)