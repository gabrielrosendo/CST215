def ceasarcypher(arr):
    encptd = []
    for i in arr:
        if 32 <= i <= 47:
            encptd.append(i)
        else: 
            new = i - 3
            if new < 97:
                encptd.append(new + 26)
            else:
                encptd.append(new)
    return encptd

with open("lab13/in.txt", 'r') as file:
    str = file.read()
    str = str.lower()
    orig = []
    for char in str:
        orig.append(ord(char))
    out = ceasarcypher(orig)
    newStr = ""  
    for i in out:
        newStr += chr(i)
    print(str)
    print(newStr)

