def toBinary(n):
    x = ''
    while n>0:
        x = str(n%2)+x
        n=n//2
    return x

def toDeci(n):
    c = 0
    d = 0
    for i in range(len(n)-1, -1, -1):
        d = d+(int(n[i]) * (2**c))
        c=c+1
    return d

def EXOR(a, b):
    for i in range(8):
        if a[i]==b[i]:
            a = a[0:i]+'0'+a[i+1:]
        else:
            a = a[0:i]+'1'+a[i+1:]
    print("Answer in binary :", a)
    print("Answer in decimal :", toDeci(a))

def OR(a,b):
    for i in range(8):
        if a[i]=='1' or b[i]=='1':
            a = a[0:i]+'1'+a[i+1:]
        else:
            a = a[0:i]+'0'+a[i+1:]
    print("Answer in binary :", a)
    print("Answer in decimal :", toDeci(a))

def  AND(a,b):
    for i in range(8):
        if a[i]=='1' and b[i]=='1':
            a = a[0:i]+'1'+a[i+1:]
        else:
            a = a[0:i]+'0'+a[i+1:]
    print("Answer in binary :", a)
    print("Answer in decimal :", toDeci(a))
    
def main():
    a = input("Enter first number (a) : ")
    b = input("Enter second number (b) : ")
    if not a.isnumeric() or not b.isnumeric():
        print("Invalid numbers entered")
        return
    a = (toBinary(int(a))).zfill(8)
    b = (toBinary(int(b))).zfill(8)
    print("Binary of a :", a)
    print("Binary of b :",b)
    print("Enter 1 for Exclusive Or of the first number by the second number")
    print("Enter 2 for OR of the first number by the second number")
    print("Enter 3 for AND of the first number by the second number")
    choice = input("Enter your choice : ")
    if choice == '1':
        EXOR(a,b)
    elif choice == '2':
        OR(a,b)
    elif choice == '3':
        AND(a,b)
    else:
        print("Invalid Choice")
    
if __name__ == "__main__":
    main()
