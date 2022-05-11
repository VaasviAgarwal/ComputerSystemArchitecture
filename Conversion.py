#Write a program to convert an unsigned number in one radix 'A' to the equivalent number in another radix 'B', where A and B can be any positive integer

def checkBase(A, n):
    A = int(A)
    if A == 16:
        if not n.isalnum():
            return True
        for i in n:
            if not (48<=ord(i)<=57 or 65<=ord(i)<=70):
                return True
        return False
    if not n.isnumeric():
        return True
    if A == 10:
        return False
    for i in n:
        if int(i)>=A:
            return True
    return False

def toDecimal(A, n):
    A = int(A)
    d = 0
    c=0
    if A == 16:
        x = 0
        for i in range(len(n)-1, -1, -1):
            if n[i]=='A':
                x = 10
            elif n[i]=='B':
                x = 11
            elif n[i]=='C':
                x = 12
            elif n[i]=='D':
                x=13
            elif n[i]=='E':
                x=14
            elif n[i]=='F':
                x=15
            else:
                x=int(n[i])
            d = d + (x * (A**c))
            c = c+1
        return d
    for i in range(len(n)-1, -1, -1):
        d = d + (int(n[i])*(A**c))
        c=c+1
    return d

def toBinary(n):
    a = ''
    while n>0:
        a = str(n%2) + a
        n=n//2
    return a

def toOctal(n):
    a = ''
    while n>0:
        a=str(n%8)+a
        n=n//8
    return a

def toHexa(n):
    a = ''
    d = ''
    while n>0:
        d = n%16
        if d==10:
            d = 'A'
        elif d == 11:
            d = 'B'
        elif d == 12:
            d = 'C'
        elif d == 13:
            d = 'D'
        elif d == 14:
            d = 'E'
        elif d==15:
            d = 'F'
        else:
            d = str(d)
        a = d+a
        n=n//16
    return a
    
def main():
    A = input("Enter the base of the number you have used (radix A) : ")
    B = input("Enter the base in which the number has to be converted (radix B) : ")
    n = input("Enter the number you wish to be converted : ")
    if A!='2' and A!='8' and A!='10' and A!='16':
        print("The value of the radix entered is invalid")
        return
    if B!='2' and B!='8' and B!='10' and B!='16':
        print("The value of the radix entered is invalid")
        return
    #Checking if the number entered is in the correct base
    if checkBase(A, n):
        print('Number entered is not in radix A')
        return
    n = toDecimal(A, n)
    if B=='2':
        n = toBinary(n)
    elif B=='8':
        n = toOctal(n)
    elif B=='10':
        n = n
    elif B == '16':
       n = toHexa(n)
    print("Answer :", n)

if __name__ == "__main__":
    main()
