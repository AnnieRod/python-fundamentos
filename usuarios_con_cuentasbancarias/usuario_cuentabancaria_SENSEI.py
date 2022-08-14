
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

#añade clase de User y se asocia con metodos de Bankaccount
class User: 

    def __init__ (self, name, mail_dir):
        self.name = name
        self.mail = mail_dir
        #BONUS SENSEI: PERMITE AL USER TENER MÁS DE UNA CUENTA
        self.account = {     
            "main_account": Bankaccount(interest_rate=0.02, balance_acc=0),
            "savings_account": Bankaccount(interest_rate=0.03, balance_acc=2000)
        }

    def deposit_amount(self, amount, acc_name):
        self.account[acc_name].deposit(amount)
        return self

    def take_money(self, debit, acc_name):
        self.account[acc_name].draft_money(debit)
        return self

    def show_balance(self, acc_name):
        self.account[acc_name].account_info()
        return self


annie = User("Annie","annie@mail.com") 
# PREGUNTA: ¿como hago para darle argumentos diferentes a los default a la cuenta de cada usuario al crearlo? Para que cada usuario tenga balances e intereses diferentes desde el inicio

annie.account.deposit(200,"main_account")
annie.account.show_balance("main_account")

"""
Intenté hacer el bonus sensei pero los metodos no se estan aplicando, genera error al ejecutar
¿Como hacer que loS metodos de user funcionen para cada cuenta?
Cuando tenia una sola cuenta funcionaba normal
"""