def toBinary(n):
    d = ''
    while n>0:
        d = str(n%2)+d
        n=n//2
    return d.zfill(8)

def toDeci(n):
    d = 0
    c = 0
    for i in range(len(n)-1,-1,-1):
        d = d+ (int(n[i])*(2**c))
        c = c+1
    return d

def addbits(a,b):
    a = toBinary(int(a))
    b = toBinary(int(b))
    print("Binary of a :", a)
    print("Binary of b :", b)

    result = ""
    carry = 0

    for i in range(7,-1,-1):
        s = int(a[i])+int(b[i])
        if s == 2:
            if carry == 1:
                result = '1' + result
            else:
                carry = 1
                result = '0' + result
        elif s == 1:
            if carry == 1:
                result = '0' + result
            else:
                result = '1'+result
        else:
            if carry == 1:
                result = '1' + result
                carry = 0
            else:
                result = '0' + result
    if carry>0:
        result = '1'+result
    print("Answer in binary :", result)
    print("Answer in decimal :", toDeci(result))

def main():
    a = input("Enter the first integer between 0 and 255(a) : ")
    b = input("Enter the second integer between 0 and 255 (b) : ")
    if not a.isnumeric() or not b.isnumeric():
        print("Invalid Entry")
        return
    addbits(a,b)

if __name__ =="__main__":
    main()
