class Acc:
    def __init__(self,AN,AP):
        self.AN=AN
        self.__AP=AP
S=Acc("1234","9829")
print(S.AN)
print(S.__AP)