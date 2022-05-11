def toBinary(n):
    x = ''
    while n>0 :
        x = str(n%2) + x
        n=n//2
    return x

def toDeci(n):
    d = 0
    c = 0
    for i in range(len(n)-1, -1, -1):
        d = d + (int(n[i])* (2**c))
        c = c+1
    return d

def rightshift(a,b):
    a = toBinary(a)
    print('First value in binary :', a)
    if b>len(a):
        print("Answer in binary : 0")
    rs = a[0:len(a)-b]
    if rs=='':
        rs = '0'
    print("Answer in binary :", rs)
    print("Answer = ", toDeci(rs))

def leftshift(a,b):
    a = toBinary(a)
    print('First value in binary :', a)
    ls = a + ('0'*b)
    print("Answer in binary :", ls)
    print("Answer in decimal :", toDeci(ls))
def main():
    a = input("Enter the first integer (Value that has to be worked on) : ")
    b = input("Enter the second integer (Value by which the other number has to be shifted) : ")
    if not a.isnumeric() or not b.isnumeric():
        print("Invalid input")
        return
    a = int(a)
    b = int(b)
    choice = input("Enter 1 Left Shift and 2 for Right Shift : ")
    if choice == '1':
        leftshift(a,b)
    elif choice == '2':
        rightshift(a,b)
    else:
        print("Invalid Entry")

if __name__ == "__main__":
    main()
