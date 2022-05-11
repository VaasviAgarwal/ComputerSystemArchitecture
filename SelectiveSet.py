#Program to perform Selective Set
#Assuming user enters the correct datatype in each case

#To return ASCII 
def val(c):
    if c >= '0' and c <= '9':
        return ord(c) - 48
    else:
        return ord(c) - 65 + 10


# A function to convert decimal into binary
def toBin(n):
    s=""
    while n>0:
        r=n%2 
        s = s + str(r)
        n=int(n/2)
    s=s[::-1]
    return s

#Function to convert a number from given base to decimal base
def toDeci(strr):
    lenn = len(strr)
    power = 1
    num = 0
    base = 2
    for i in range(lenn - 1, -1, -1):
        num += val(strr[i]) * power
        power = power * base
    return num

def main():
    a = int(input('Enter the first natural number (a) : '))
    b = int(input('Enter the second natural number  (b) : '))
    a = (toBin(a)).zfill(8)
    b = (toBin(b)).zfill(8)
    print('Binary of a :',a)
    print('Binary of b :',b)

    result = ''
    for i in range(8):
        if b[i]=='1':
            a = a[0:i]+'1'+a[i+1:]
    print('Result in binary =',a)
    print('Result in decimal =',toDeci(a))

if __name__ == '__main__':
    main()
    

