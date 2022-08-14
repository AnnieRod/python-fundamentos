
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

    def deposit_amount(self, amount):
        self.account.deposit(amount)
        return self

    def take_money(self, debit):
        self.account.draft_money(debit)
        return self

    def show_balance(self):
        self.account.account_info()
        return self


#creacion de instancias de usuarios
annie = User("Annie","annie@mail.com") 
# PREGUNTA: ¿como hago para darle argumentos diferentes a los default a la cuenta de cada usuario al crearlo? Para que cada usuario tenga balances e intereses diferentes desde el inicio

# prueba de que si le esta dando la cuenta con los valores default
print(annie.account["main_account"].interest, annie.account["main_account"].balance) 
print(annie.account["savings_account"].interest, annie.account["savings_account"].balance) 

#test de funcionamiento de los metodos de Class User sobre la cuenta del usuario
annie.account["savings_account"].deposit(2000).draft_money(800).generate_interest().account_info()

"""
PREGUNTA: No me esta tomando los metodos de User, he puesto directamente los de Bankaccount para que funcione (Linea 83)
    ¿Como hacer para que los tome? Cuando habia una sola cuenta por usuario si funcionaban sin problema
    ¿Como hacer para que los metodos sepan a cual de las cuentas aplicar el metodo ahora que se ha creado un diccionario con varias cuentas?
"""
