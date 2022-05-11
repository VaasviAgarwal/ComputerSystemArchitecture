#Program to perform bitwise addition on two numbers entered by the users
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

result = ''
carry = 0
a = a.zfill(8)
b = b.zfill(8)

print('Binary of a -', a)
print('Binary of b -', b)

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

if carry>0:
    result = '1' + result
print("Answer (in binary) - ", result)
result = toDeci(result, 2)
print("Answer (in decimal)- ", result)
            
