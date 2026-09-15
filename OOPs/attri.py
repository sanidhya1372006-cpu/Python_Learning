class Stu:
    cn="Arya"
    def __init__(self):
        self.name=input("Enter Name:")
        self.rn=int(input("Enter Roll No:"))
    
    def info(self):
        print(Stu.cn)
        print(self.name)
        print(self.rn)


s=Stu()
s.info()