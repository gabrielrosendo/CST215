arr = []

def collatzSeq(c0):
    if (c0 == 1):
        print(c0)
        arr.append(c0)
        return 0
    if(c0%2==0):
        print(c0)
        arr.append(c0)
        cnext = int(c0/2)
        collatzSeq(cnext)
    else:
        print(c0)
        arr.append(c0)
        cnext = c0*3+1
        collatzSeq(cnext)

# test 65, 290, 98, 1202088120
n1 = int(input("Type the first number of the sequence: "))
collatzSeq(n1)
count = 0
for int in arr:
    count+=1
print ("C[0] = ", n1, " has ", count, " terms")