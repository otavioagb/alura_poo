class ContaBancaria:

    def __init__(self, holder, balance):
        self._holder = holder
        self._balance = balance   #Estão protegidos, por isso a necessidade de ter properties
        self._active = False

    @property
    def holder(self):
        return self.holder
    
    @property
    def balance(self):
        return self.balance
    
    @property
    def active(self):
        return self._active
    

conta4 = ContaBancaria("Fernanda", 1500)
print(f"Titular da conta 4: {conta4.holder}")

