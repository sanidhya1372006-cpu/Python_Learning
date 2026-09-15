b=10000
while True:
    
    print("----ATM MENU----")
    print("1.Check Balance")
    print("2.Deposit")
    print("3.Withdrawal")
    print("4.Exit")

    c=int(input("Enter Your Choice:"))

    if(c==1):
        print("Your Current Balance Is:",b)

    elif(c==2):
        a=int(input("Enter Amount To Deposit:"))
        b=b+a
        print("Your Current Balance Is:",b)

    elif(c==3):
         w=int(input("Enter Amount To Withdraw:"))
         if(w>b):
             print("Insufficient Balance")
         else:
            b=b-w
            print("Your Current Balance Is:",b)

    elif(c==4):
        print("Thank You")
        break

    else:
        print("Invalid Option Choosen")



