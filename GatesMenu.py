#Program to create gates in menu driven format

#Funciton for AND Gate
def AND(a,b):
    if a==1 & b==1:
        return 1
    else:
        return 0

#Function for OR Gate
def OR(a,b):
    if a==1 or b==1:
        return 1
    else:
        return 0

#Funciton for NOT Gate
def NOT(a):
    if a==1:
        return 0
    else:
        return 1

#Function for NAND Gate
def NAND(a,b):
    if a==1 & b==1:
        return 0
    else:
        return 1

#Function for NOR Gate
def NOR(a,b):
    if(a == 0) and (b == 0):
        return 1
    elif(a == 0) and (b == 1):
        return 0
    elif(a == 1) and (b == 0):
        return 0
    elif(a == 1) and (b == 1):
        return 0

#Funciton for XOR Gate
def XOR(a,b):
    if a != b:
        return 1
    else:
        return 0

#Function for XNOR Gate
def XNOR(a,b):
    if (a==b):
        return 1
    else:
        return 0

#Accepting the values (Asssuming that the user enters them correctly (Nothing other than 0 or 1 is entered)
f=int(input("Enter the value of a i.e.,either 0 or 1 - "))
d=int(input("Enter the value of b i.e.,either 0 or 1 - "))
print()

#Running a menu driven program
while True:
    #Printing the Menu
    print("Enter 1 for AND Gate")
    print("Enter 2 for OR Gate")
    print("Enter 3 for NOT Gate")
    print("Enter 4 for NAND Gate")
    print("Enter 5 for NOR Gate")
    print("Enter 6 for XOR Gate")
    print("Enter 7 for XNOR Gate")
    print("Enter 8 to EXIT")
    print()
    c = input("Enter your Choice - ")
    print()
    if c=='1':
        print("|A | B |  A.B |")
        print(f,'|', d,'|', AND(f,d),"|")
    elif c=='2':
        print("|A | B |  A+B |")
        print(f,'|', d,'|',OR(f,d),"|")
    elif c=='3':
        print("A | A' |")
        print(f,"|",NOT(f),'|')
        print(d,"|",NOT(d),'|')
    elif c=='4':
        print("|A| B |  (A.B)' |")
        print(f,"|" ,d,"|",NAND(f,d), "|")
    elif c=='5':
        print("|A| B |  (A+B)' |")
        print(f,"|" ,d,"|",NOR(f,d), "|")
    elif c=='6':
        print("|A | B |  AB'+A'B |")
        print(f,"|" ,d,"|",XOR(f,d), "|")
    elif c=='7':
        print("|A | B |  AB+A'B' |")
        print(f,"|" ,d,"|",XNOR(f,d), "|")
    elif c=='8':
        print("Program in exited")
        break
    else:
        print("Invalid Input Entered")
    print('-----------------------------------------------------------------------------------------------')
#Program ends here

        
        

