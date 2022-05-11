def toBinary(n):
    x = ''
    while n>0:
        x = str(n%2) + x
        n = n//2
    return x
def toDeci(n):
    c = 0
    d = 0
    for i in range(len(n)-1, -1, -1):
        d = d + (int(n[i])*(2**c))
        c = c+1
    return d

def upcounter(n):
    while n<=30:
        a = toBinary(n).zfill(5)
        b = ''
        if a[4] == '0':
            b = a[0:4]+'1'
        else:
            x = a.rindex('0')
            b = a[0:x]+'1'
            c = a[x+1:]
            c = c.replace('1', '0')
            b = b+c
        print(b , '=', toDeci(b))
        n = n+1

def downcounter(n):
    while n>0:
        a = toBinary(n).zfill(5)
        b = ''
        if a[4] == '1':
            b = a[0:4]+'0'
        else:
            x = a.rindex('1')
            b = a[0:x]+'0'
            c = a[x+1:]
            c = c.replace('0', '1')
            b = b+c
        print(b, '=', toDeci(b))
        n = n-1
               


def main():
    print("Enter 1 for upcounter")
    print("Enter 2 for downcounter")
    choice = input("Enter your choice : ")
    n = input("Enter the start value of the counter in decimal (Value should be between 0 and 31) : ")
    if not (n.isnumeric and int(n)<=31):
        print("Invalid value entered")
        return
    n = int(n)
    if choice == '1':
        upcounter(n)
    elif choice == '2':
        downcounter(n)
    else:
        print("Invalid choice")

if __name__ =="__main__":
    main()
