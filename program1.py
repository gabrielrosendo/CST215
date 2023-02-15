#Gabriel Marcelino
#This is my own work
#10/5/22
#Program 1

from pickle import TRUE

def HALF_ADDER(a,b,on):
    sum = a ^ b
    carry = a & b
    if(on):
        print("c =", carry, " s =", sum)
    return carry, sum

def FULL_ADDER(a,b,c,on):
    c1, s1 = HALF_ADDER(a,b, False)
    c2, totalsum = HALF_ADDER(s1,c, False)
    carry = c1 or c2
    if(on):
        print("c = ",carry,"s = ", totalsum)
    return carry, totalsum


def PARALLEL_ADDER(a,b):
    arr1=[]
    arr2=[]
    res=[]
    for i in iter(a):
        arr1.append(i)
    for i in iter(b):
        arr2.append(i)
    carry1, sum1 = HALF_ADDER(int(arr1[2]), int(arr2[2]), False)
    res.insert(0,sum1)
    carry2, sum2 = FULL_ADDER(int(arr1[1]), int(arr2[1]), carry1, False)
    res.insert(0,sum2)
    carry3, sum3 = FULL_ADDER(int(arr1[0]), int(arr2[0]), carry2,False)
    res.insert(0,sum3)
    res.insert(0,carry3)
    print(*arr1, " + ", *arr2," = ", *res, sep='')
    

print("Half-adder")
print("i = 0  j = 0", end=' | ')
HALF_ADDER(0,0,TRUE)
print("i = 0  j = 1", end=' | ')
HALF_ADDER(0,1,TRUE)
print("i = 1  j = 0", end=' | ')
HALF_ADDER(1,0,TRUE)
print("i = 1  j = 1", end=' | ')
HALF_ADDER(1,1,TRUE)
print()

print("Full-adder")
print("i = 0  j = 0  k = 0", end=' | ')
FULL_ADDER(0,0,0,TRUE)
print("i = 0  j = 0  k = 1", end=' | ')
FULL_ADDER(0,0,1,TRUE)
print("i = 0  j = 1  k = 0", end=' | ')
FULL_ADDER(0,1,0,TRUE)
print("i = 0  j = 1  k = 1", end=' | ')
FULL_ADDER(0,1,1,TRUE)
print("i = 1  j = 0  k = 0", end=' | ')
FULL_ADDER(1,0,0,TRUE)
print("i = 1  j = 0  k = 1", end=' | ')
FULL_ADDER(1,0,1,TRUE)
print("i = 1  j = 1  k = 0", end=' | ')
FULL_ADDER(1,1,0,TRUE)
print("i = 1  j = 1  k = 1", end=' | ')
FULL_ADDER(1,1,1,TRUE)
print()

PARALLEL_ADDER("011","110")
