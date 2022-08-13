
class User:
    def __init__(self,name,mail_dir):
        self.name = name
        self.mail = mail_dir
        self.account = 0

    #metodo de deposito a cuenta
    def deposit_amount(self, amount):
        self.account += amount
        return self
    
    #metodo de retiro a cuenta
    def take_money (self, debit):
        if(self.account - debit <= 0):
            print("Insufficient funds. . . Ask for a loan or wait until payday!")
        else:
            self.account -= debit
        return self
    
    #metodo para mostrar saldo
    def show_balance(self):
        print(f"Hi {self.name}, your balance is: {self.account}.")
        return self

    #BONUS: transferir a otro usuario
    def transfer_user(self,user2,transfer):
        user2.deposit_amount(transfer)
        self.take_money(transfer)
        print("successful transfer!")
        self.show_balance()
        user2.show_balance()
        return self

#Creación de 3 instancias
annie = User("Annie","annie@mail.com")
carpe = User("Carpe", "diem@mail.com")
charlo = User("Charlo","lec@mail.com")

#Movimientos del primer usuario
annie.deposit_amount(100).deposit_amount(50).deposit_amount(200).take_money(125).show_balance()

#Movimientos del segundo usuario
carpe.deposit_amount(200).deposit_amount(250).take_money(100).take_money(150).show_balance()

#Movimientos del tercer usuario
charlo.deposit_amount(300).take_money(100).take_money(80).take_money(230).show_balance()

#transferir entre usuarios
annie.transfer_user(charlo,100)
