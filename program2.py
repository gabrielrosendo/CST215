#Gabriel Marcelino
#This is my own work
#10/27/22
#Program 2

import random

def gcd(a, b):
    a = num1
    b = num2
    while (a != b):
        if (a > b):
            a = a-b
        else:
            b = b-a
    return a

# find ax + by = 1
def find_xy(a,b):
    x = 1
    y = 0
    x1 = 0
    y1 = 1

    a1 = a
    b1 = b

    while(b1!=0):
        div = a1 // b1
        a2 = a1
        x2 = x
        y2 = y

        a1 = b1
        x = x1
        y = y1

        b1 = a2 % b1
        x1 = x2 - div * x1
        y1 = y2 - div * y1
    return f'{a} * ({x}) + {b}*({y}) = {a1}'    

for i in range(50):
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    if((gcd(num1,num2))==1):
        print(num1,"\t",num2,"\t",gcd(num1,num2),"\t", find_xy(num1,num2))
    else:
        print(num1,"\t", num2,"\t",gcd(num1,num2),"\t", "  ")

