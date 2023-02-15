def rec(x):
    if x==1:
        return 5 
    else:
        return(rec(x-1)*4/3)

def exp(x):
    return ((4/3)**(x-1))*5

print("Recursive \t  Explicit")
print("--------------------------")
for i in range (1,21):
    print(round(rec(i)),"\t\t " , round(exp(i)))
