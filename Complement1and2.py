def checkbin(n):
    for i in n:
        if i!='0' and i!='1':
            print("Not a binary value")
            return False
    return True

def comp1(n):
    x = ''
    for i in n:
        if i == '0':
            x = x+'1'
        else:
            x = x + '0'
    print("1's complement of the number :", x)

def comp2(n):
    x = ''
    c = n.rindex('1')
    for i in n[0:c]:
        if i == '0':
            x = x + '1'
        else:
            x = x + '0'
    x = x + n[c:]
    print("2's complement of the number : ", x)
    

def main():
    n = input("Enter a binary number : ")
    if not checkbin(n):
        return
    print("Enter 1 for calculating 1's compliment of the number")
    print("Enter 2 for calculating 2's compliment of the number")
    choice = input("Enter your choice : ")
    print("Number entered by you in 8 bit format :", n.zfill(8))
    if choice == '1':
        comp1(n.zfill(8))
    elif choice == '2':
        comp2(n.zfill(8))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
