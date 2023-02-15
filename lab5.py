#Gabriel Marcelino
#This is my own work
#10/5/22
#Lab Question 5

def countBits(a):
    num = str(bin(a)).lstrip('-0b')
    res = num.count('1')
    print("(", res,",'",num,"'",")")

countBits(12)
