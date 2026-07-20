a=int(input("Enter Year:"))
if (a%4==0 and (a%400==0 or a%100!=0 )):
    print("LEap Year")
else:
    print("NOt A Leap Year")