class Car:
    def __init__(self):
        self.name=input("Enter Car Name:")
        self.color=input("Enter Car Color:")
    def info(self):
        print(self.name)
        print(self.color)
c=Car()
c.info()
