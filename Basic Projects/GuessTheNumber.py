import random 
print("==Guess The Number==")
a=input("Do U Want To Play:")
if(a=="yes"):
    print("Instructions: Guess Between 0 To 100")
    r=random.randint(0,100)
    while True:
        n=int(input("Enter The Number:"))
        if(n>r):
            print("Guess Something Smaller:")
        elif(n<r):
            print("Guess Something Bigger:")
        elif(n==r):
            print("Congratulations U Guessed It Right ")
            break
        else:
            print("Invalid Number")
elif(a=="no"):
    print("Thank You")
else:
    print("Invalid Choice")
        
