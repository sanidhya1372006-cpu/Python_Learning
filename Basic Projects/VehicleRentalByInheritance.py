class Vehicle:
    def __init__(self,brand,model,rent):
        self.brand=brand
        self.model=model
        self.rent=rent

    def display(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        print("Rent:",self.rent)

class Car(Vehicle):

    def __init__(self, brand, model, rent,seats):
        super().__init__(brand, model, rent)
        self.seats=seats
    
    def Calculate_rent(self,days):
        return self.rent*days
    
    def Display(self):
        super().display()
        print("Seats:",self.seats)
    
class Bike(Vehicle):
    def __init__(self, brand, model, rent,cc):
        super().__init__(brand, model, rent)
        self.cc=cc
    
    def Calc(self,day):
        return self.rent*day
    
    def Dsply(self):
        super().display()
        print("Seats:",self.cc)
    


a=int(input("Enter Days U want Rental For Car:"))
l=int(input("Enter Days U want Rental For Bike:"))

C=Car("Toyota","Innova",2000,7)
C.Display()
print("TOTAL RENT:",C.Calculate_rent(a))
B=Bike("Honda","HERO",500,2)
B.Dsply()
print("Total Rent",B.Calc(l))