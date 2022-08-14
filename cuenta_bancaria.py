
class Bankaccount: 
    allAccounts = []
    
    #creacion  de instancias de cuentas
    def __init__(self, interest_rate, balance_acc):
        self.interest = interest_rate
        self.balance = balance_acc
        Bankaccount.allAccounts.append(self)
    
    #metodo de deposito
    def deposit(self,amount):
        self.balance += amount
        return self

    #metodo de mostrar info de la cuenta
    def account_info(self):
        print(f"Balance: ${self.balance}")   
        return self 
    
    #metodo para generar intereses
    def generate_interest(self):
        if self.balance > 0:
            self.balance += (self.balance*self.interest)
        return self
    
    #metodo de retiro
    def draft_money(self, amount):
        if Bankaccount.approve_draft(self.balance, amount): #try to print this
            self.balance -= amount
        else:
            print("Insufficient funds, charging a $5 fee")
            self.balance-=5
        return self 

    #metodo estatico que verifica si hay fondos suficientes
    @staticmethod
    def approve_draft(balance,amount):
        if(balance - amount) < 0:
            return False
        else:
            return True
    #BONUS NINJA: Metodo que imprime información de todas las instancias
    @classmethod
    def list_accounts(cls):
        for account in cls.allAccounts:
            print(f"Balance: ${account.balance} - Interest Rate: {account.interest}")

#creacion de instancias: 2 cuentas
account1 = Bankaccount(0.02, 4000)
account2 = Bankaccount(0.03, 3500)

account1.deposit(200).deposit(500).deposit(300).draft_money(1800).generate_interest().account_info()
account2.deposit(800).deposit(300).draft_money(2500).draft_money(800).draft_money(1000).draft_money(350).generate_interest().account_info()
Bankaccount.list_accounts()
