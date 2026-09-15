class Student:
    def __init__(self):
        self.name=input("Enter Name:")
        self.rn=int(input("Enter Roll No:"))
        self.m1=int(input("Enter Marks:"))
        self.m2=int(input("Enter Marks:"))
        self.m3=int(input("Enter Marks:"))

    def total(self):
        self.t=self.m1+self.m2+self.m3
        print("Total:",self.t)
    def percent(self):
        self.p=(self.t*100)/300
        print("Percentage:",self.p)
    
    def result(self):
        if(self.p>=90):
            print("Grade:A")
            print("Result:Pass")
        elif(self.p>=75 and self.p<90):
            print("Grade:B")
            print("Result:Pass")
        elif(self.p>=50 and self.p<75):
            print("Grade:C")
            print("Result:Pass")
        elif(self.p>=37 and self.p<50):
            print("Grade:D")
            print("Result:Pass")
        else:
            print("Result:Fail")

    def display(self):
        print("====STUDENT RESULT====")
        print("Name:",self.name)
        print("Roll No:",self.rn)


s=Student()
s.display()
s.total()
s.percent()
s.result()


