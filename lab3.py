#Gabriel Marcelino
#This is my own work
#9/23/22
#Lab Question 3

# return T/F insted of True/False
def getVal(x):
    if x:
        return "T"
    else:
        return "F"
         
# print layout and values
print("+------------------------------------+")
print("+ p\tq | p^q\t pvq\tp->q\tp<->q+")
print("+------------------------------------+")
(p,q) = (True,True)
print("+",getVal(p),"\t",getVal(q),"|",getVal((p and q)),"\t",getVal((p or q)),"\t",getVal(((not p) or q)),"\t",getVal(((not p) or q) and ((not q) or p))," +")
(p,q)=(True,False)
print("+",getVal(p),"\t",getVal(q),"|",getVal((p and q)),"\t",getVal((p or q)),"\t",getVal(((not p)) or q),"\t",getVal(((not p) or q) and ((not q) or p))," +")
(p,q)=(False,True)
print("+",getVal(p),"\t",getVal(q),"|",getVal((p and q)),"\t",getVal((p or q)),"\t",getVal(((not p)) or q),"\t",getVal(((not p) or q) and ((not q) or p))," +")
(p,q)=(False,False)
print("+",getVal(p),"\t",getVal(q),"|",getVal((p and q)),"\t",getVal((p or q)),"\t",getVal(((not p)) or q),"\t",getVal(((not p) or q) and ((not q) or p))," +")
print("+------------------------------------+")

