class Person:
    name="ASSSSS"

    def C(self,name):
        self.__class__.name=name

P=Person()
P.C("Saani")
print(P.name)
print(Person.name)

