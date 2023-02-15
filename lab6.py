#Gabriel Marcelino
#This is my own work
#10/15/22
#Lab Question 6

from tkinter import OFF
from tabulate import tabulate
import random

def gcd(a,b):
    a = num1
    b = num2
    while(a!=b):
        if(a>b):
            a = a-b
        else:
            b = b-a
    return a

for i in range(100):
    num1 = random.randint(1,9999999)
    num2 = random.randint(1,9999999)
    a = gcd(num1,num2)
    print(tabulate([[str(num1), str(num2), str(a)]]).replace('-',''), end="") 
