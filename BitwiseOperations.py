#Program to use Bitwiise shift operators

while True:
    print(' ----------------------------------------------')
    ch = input('Enter y or Y to continue the program - ')
    if ch!='y' and ch!='Y':
        break
    
    print("Choose operator :")
    print('Enter 1 for Left shift')
    print('Enter 2 for Right shift')
    choice = input('Enter your choice : ')

    if choice != '1' and choice != '2':
        print('Invalid Choice')
    else:
        print()
        n1 = int(input('Enter first number : '))
        n2 = int(input('Enter second number : '))
        print("n1 in binary =", bin(n1).replace("0b"," "))
        print()

        if n2 >= 0 and n2<n1:
            if choice == '1':
                x = n1<<n2
                print('Left shift -->', n1 ,'<<', n2,'=', x)    
                x = bin(x).replace("0b", " ")
                print('Answer as Binary Number :',x)
            elif choice == '2':
                x=n1>>n2
                print('Right shift -->', n1 ,'>>', n2,'=', x) 
                x = bin(x).replace("0b", " ")
                print('Answer as Binary Number :',x)
        else:
            print('Second number should be positive!!!')
