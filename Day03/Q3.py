a=int(input("Enter Number A="))
b=int(input("Enter Number B="))
c=int(input("Enter Number C="))
if(a>b and a>c):
    print("A IS GREAT:",a)
elif(b>c and b>a):
    print("B IS GREAT:",b)
else:
    print("C IS GREAT:",c)