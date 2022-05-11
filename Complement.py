#Assuming that the values are in correct datatypes

#For ones complement
def comp1(a):
    
    c=""    
    for i in range(len(a)):  
        if a[i]=="0":
            c+="1"
        elif a[i]=="1":
            c+="0"
        else:
            print("Not a binary input!")
            A=bin(int(a))
            print("binary ",a," = ",A)
            c=comp1(A)
            break
    return c

#For two complement
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

def main():
        while True:
        	 print("1. one's compliment")
        	 print("2. two's compliment")
        	 ch = input("Enter your choice : ")
        	 if ch == '1':
        	    n = input("Enter a binary number : ")
        	    print("one's compliment :", comp1(n))
        	 elif ch == '2' :
        	     n=input("Enter a binary number : ")
        	     print("two's compliment :", comp2(n))
        	 else :
        	 	print("Invalid Choice")
        	 	break
              
if __name__=="__main__":
    main()
