#Assuming the user enters the correct data type in each case
#Write a program to convert an unsigned number in one radix ‘A’ to the equivalent number in another radix ‘B’, where A and B can be any positive integer.

#Function to return ASCII value of a numeric character
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
        if (val(strr[i]) >= base):
            print("Invalid Number")
            return -1
        num += val(strr[i]) * power
        power = power * base
    return num

#Function to return equivalent character of a given value
def reVal(num):
    if num >= 0 and num<= 9:
        return chr(num + 48)
    else:
        return chr(num - 10 + 65)

#Function to convert a given decimal number to a given base
def fromDeci(base, inputNum):
    res = ''
    while (inputNum > 0):
        res += reVal(inputNum % base)
        inputNum //= base
    res = res[::-1]
    return res

#Driver Code
s = input('Enter the number you wish to be converted : ')
a = int(input('Enter base A : '))
b = int(input('Enter base B : '))
num = toDeci(s, a)
print('Answer :', fromDeci(b,num))
