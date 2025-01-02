class BankAccount:

    def __init__(self, holder='', balance=0):
        self.holder = holder
        self.balance = balance 
        self.active = False


class BankClient:
    def __init__(self, name='', age=0, address='', identity=0, profession=''):
        self.name = name
        self.age = age
        self.address = address
        self.identity = identity
        self.profession = profession

    @classmethod
    def create_account(cls, holder, inicial_balance):
        account = BankAccount(holder, inicial_balance)
        return account

client1 = BankClient("Anny", 30, "Street A", "123.456.789-01", "Backend")
client2 = BankClient("Tom", 25, "Street B", "987.654.321-01", "Student")
client3 = BankClient("Peter", 40, "Street C", "111.222.333-44", "Frontend")
client_account = BankClient.create_account("Anny", 2000)
print(f"{client_account.holder}'s account successfully created. Inicial balance R${client_account.balance}")