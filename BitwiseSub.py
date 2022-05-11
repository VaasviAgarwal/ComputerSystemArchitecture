def toBinary(n):
    d = ""
    while n > 0:
        d = str(n%2)+d
        n = n//2
    return d.zfill(8)

def toDeci(n):
    c = 0
    d = 0
    for i in range(len(n)-1, -1, -1):
        d = d + (int(n[i]) * (2**c))
        c = c+1
    return d

def twoComp(n):
    x = n.rindex('1')
    d = ''
    for i in range(x):
        if n[i]=='1':
            d = d + "0"
        else:
            d = d + '1'
    d = d + n[x:]
    return d

def addbit(a,b):
    print(a)
    print(b)
    result = ""
    carry = 0
    for i in range(7, -1, -1):
        s = int(a[i]) + int(b[i])
        if s==2:
            if carry ==1:
                result = '1' + result
            else:
                result = '0'+result
                carry = 1
        elif s==1:
            if carry ==1 :
                result = '0' + result
            else:
                result = '1' + result
        else:
            if carry == 1:
                result = '1' + result
                carry = 0
            else:
                result = '0' + result
    print(result)
    return result

def subbit(a,b):
    a = toBinary(int(a))
    b = toBinary(int(b))
    print("Binary of a :", a)
    print("Binary of b :", b)
    b = twoComp(b)
    print("Two's compliment of b :", b)

    result = addbit(a,b)
    print("Result in binary :", result)

    if result[0] == '1':
        print("Result in decimal : -",toDeci(twoComp(result)))
    else:
        print("Result in decimal :", toDeci(result))

def main():
    a = input("Enter a positive integer between 0 and 255 (a) : ")
    b = input("Enter the second positive integer between 0 and 255 (b) : ")
    if not a.isnumeric() or not b.isnumeric() :
        print("Invalid numbers entered")
        return
    subbit(a,b)

if __name__ == "__main__":
    main()
