#Marks % grade And pass/fail
name=input("Enter Student Name:")
m1=int(input("Enter Marks:"))
m2=int(input("Enter Marks:"))
m3=int(input("Enter Marks:"))

total=m1+m2+m3
print("Total Marks:",total)
percentage=(total*100)/300
print("Percentage:",percentage)

if(percentage<=100 and percentage>=90):
    print("Passed With A Grade")
elif(percentage<90 and percentage>=75):
    print("Passed With B Grade")
elif(percentage<75 and percentage>=50):
    print("Passed With C Grade")
elif(percentage<50 and percentage>=37):
    print("Passed With d Grade")
else:
    print("Failed")

