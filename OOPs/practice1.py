class Student:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    def avg(self):
        avg=(self.m1+self.m2+self.m3)/3
        print("Average:",avg)
    
s=Student(99,98,99)
s.avg()

