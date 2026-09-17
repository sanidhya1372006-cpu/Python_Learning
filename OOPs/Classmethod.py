class Person:
    name="SAnidhya"

    @classmethod
    def Change(cls,name):
        cls.name=name

P=Person()
P.Change("Saaani")
print(P.name)
print(Person.name)
