# Gabriel Marcelino
# This is my own work
# 10/1/22
# Lab Question 4

def AND(a, b):
    if (a == True and b == True):
        return True
    else:
        return False

def NAND(a, b):
    if (a == True and b == True):
        return False
    else:
        return True

def OR(a,b):
    if (a == True):
        return True
    if (b == True):
        return True
    else:
        return False

def NOR(a,b):
    if(a ==True or b == True):
        return False
    else:
        return True

def XOR(a,b):
    if (a != b):
        return True
    else:
        return False

def NOT(a):
    if (a==False):
        return True
    else:
        return False

print("+------------------------------------+")
print("|\tAND TRUTH TABLE\t             |")
print("+------------------------------------+")
print("| A = F, B = F  |  A AND B =  ", AND(0,0), "|")
print("| A = F, B = T  |  A AND B =  ", AND(0,1), "|")
print("| A = T, B = F  |  A AND B =  ", AND(1,0), "|")
print("| A = T, B = T  |  A AND B =  ", AND(1,1), " |")

print("+------------------------------------+")
print("|\tOR TRUTH TABLE\t             |")
print("+------------------------------------+")
print("| A = F, B = F  |  A OR B =  ", OR(0,0), " |")
print("| A = F, B = T  |  A OR B =  ", OR(0,1), "  |")
print("| A = T, B = F  |  A OR B =  ", OR(1,0), "  |")
print("| A = T, B = T  |  A OR B =  ", OR(1,1), "  |")

print("+------------------------------------+")
print("|\tNAND TRUTH TABLE             |")
print("+------------------------------------+")
print("| A = F, B = F  |  A OR B =  ", NAND(0,0), "  |")
print("| A = F, B = T  |  A OR B =  ", NAND(0,1), "  |")
print("| A = T, B = F  |  A OR B =  ", NAND(1,0), "  |")
print("| A = T, B = T  |  A OR B =  ", NAND(1,1), " |")

print("+------------------------------------+")
print("|\tNOR TRUTH TABLE              |")
print("+------------------------------------+")
print("| A = F, B = F  |  A OR B =  ", NOR(0,0), "  |")
print("| A = F, B = T  |  A OR B =  ", NOR(0,1), " |")
print("| A = T, B = F  |  A OR B =  ", NOR(1,0), " |")
print("| A = T, B = T  |  A OR B =  ", NOR(1,1), " |")

print("+------------------------------------+")
print("|\tXOR TRUTH TABLE              |")
print("+------------------------------------+")
print("| A = F, B = F  |  A OR B =  ", XOR(0,0), " |")
print("| A = F, B = T  |  A OR B =  ", XOR(0,1), "  |")
print("| A = T, B = F  |  A OR B =  ", XOR(1,0), "  |")
print("| A = T, B = T  |  A OR B =  ", XOR(1,1), " |")

print("+-------------------------------------------+")
print("|\tNOT TRUTH TABLE                     |")
print("+-------------------------------------------+")
print("|A = F, B = F| A NOT =", NOT(0), " B NOT = ", NOT(0), " |")
print("|A = F, B = T| A NOT =", NOT(0), " B NOT = ", NOT(1), "|")
print("|A = T, B = F| A NOT =", NOT(1), "B NOT = ", NOT(0), " |")
print("|A = T, B = T| A NOT =", NOT(1), "B NOT = ", NOT(1), "|")
