class ContaBancaria:

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance
        self._active = False

    def __str__(self):
        return f'Holder account: {self.holder} | Balance R$ {self.balance}'
    
    @classmethod
    def activate_account(cls, account):
        account._active = True

holder_acoount1 = ContaBancaria('Joseph', '1.500,00')
holder_acoount2 = ContaBancaria('Roselin', '3.050,00')
holder_acoount3 = ContaBancaria('Mathew', '3.500,00')
ContaBancaria.activate_account(holder_acoount3)
print(holder_acoount3._active)


