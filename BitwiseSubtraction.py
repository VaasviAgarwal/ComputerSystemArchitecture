#Program to perform bitwise subtraction on two numbers entered by the users
#Assuming user enters the correct datatype in each case

# A function to convert decimal into binary
def toBin(n):
    s=""
    while n>0:
        r=n%2 
        s = s + str(r)
        n=int(n/2)
    s=s[::-1]
    return s

#To return digit using ASCII
def val(c):
    if c >= '0' and c <= '9':
        return ord(c) - 48
    else:
        return ord(c) - 65 + 10


#Function to convert a number from given base to decimal base
def toDeci(strr, base):
    lenn = len(strr)
    power = 1
    num = 0
    for i in range(lenn - 1, -1, -1):
        num += val(strr[i]) * power
        power = power * base
    return num

a = int(input('Enter the first postive integer number : '))
b = int(input('Enter the second positive integer number : '))
a = toBin(a)
b = toBin(b)

a = a.zfill(8)
b = b.zfill(8)

print('Binary of a :', a)
print('Binary of b :', b)

#For 2's complement
def comp2(a):   
    c=""
    i=len(a)-1
    while a[i]=="0":
        c+="0"
        if i==0:
        	break
        i-=1         
    if i==0:
        c="0"
    else:
        c="1"+c                
    length=i
    b=""
    for j in range(length):
        if a[j]=="0":
            b+="1"
        elif a[j]=="1":
            b+="0"
        else:
            print("Not a binary input")
            A=bin(int(a))
            print("binary ",a," = ",A)
            c=comp2(A)
            break
    d=b+c
    return d

b = comp2(b)
print("2's Compliment of b -", b)

result = ''
carry = 0
i = 7
while(i>=0):
    s = int(a[i]) + int(b[i])
    if s == 2:
        if carry == 0:
            carry = 1
            result = '0' + result
        else:
            result =  '1' + result
    elif s == 1:
        if carry == 1:
            carry = 1
            result = '0' + result
        else:
            result = '1' + result
    else:
        if carry == 0:
            result = '0' + result
        else:
            result =  '1' + result
            carry = 0
    i = i - 1

if result[0] == '1':
    print("Answer (in binary) : -", result, sep='')
    result = comp2(result)
    result = toDeci(result, 2)
    print("Answer (in decimal) : -", result, sep='')
else:
    print("Answer (in binary) : ", result)
    result = toDeci(result, 2)
    print("Answer (in decimal) : ", result)

