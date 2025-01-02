class BankAccount:

    def __init__(self, holder, balance):
        self._holder = holder
        self._balance = balance
        self._active = False

    @property
    def holder(self):
        return self._holder
    
    @property
    def balance(self):
        return self._balance
    
    @property
    def active(self):
        return self._active
    

account = BankAccount("Victory", 1500)
print(f"Holder account: {account.holder}")

