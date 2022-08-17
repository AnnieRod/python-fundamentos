
class Bankaccount: 
    
    #creacion  de instancias de cuentas
    def __init__(self, interest_rate, balance_acc):
        self.interest = interest_rate
        self.balance = balance_acc
    
    #metodo de deposito
    def deposit(self,amount):
        self.balance += amount
        return self

    #metodo de mostrar info de la cuenta
    def account_info(self):
        print(f"Balance: ${self.balance} - Interest Rate: {self.interest}")        
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

#añade clase de User y se asocia con metodos de Bankaccount
class User: 

    def __init__ (self, name, mail_dir):
        self.name = name
        self.mail = mail_dir
        #BONUS SENSEI: PERMITE AL USER TENER MÁS DE UNA CUENTA
        self.account = {}

    #agrega cuenta nueva al usuario BONUS SENSEI
    def createAcc (self, acc_name,interest,balance):
        self.account[acc_name] = Bankaccount(balance_acc=balance, interest_rate=interest)
        print(f"account named {acc_name} created!")
        return self

    #metodos para movimientos bancarios
    def deposit_amount(self, amount, acc_name):
        self.account[acc_name].deposit(amount)
        return self

    def take_money(self, debit, acc_name):
        self.account[acc_name].draft_money(debit)
        return self

    def show_balance(self, acc_name):
        self.account[acc_name].account_info()
        return self

    def gen_interest(self, acc_name):
        self.account[acc_name].generate_interest()
        return self
        

annie = User("Annie", "annie@mail.com")
annie.createAcc("main", balance=4000, interest=0.01).createAcc("savings", balance=2000, interest=0.03).deposit_amount(500, "main").take_money(800, "savings").gen_interest("savings").show_balance("main").show_balance("savings")
