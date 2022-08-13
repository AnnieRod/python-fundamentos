
class User:
    def __init__(self,name,mail_dir):
        self.name = name
        self.mail = mail_dir
        self.account = 0

    #metodo de deposito a cuenta
    def deposit_amount(self, amount):
        self.account += amount
    
    #metodo de retiro a cuenta
    def take_money (self, debit):
        if(self.account - debit <= 0):
            print("Insufficient funds. . . Ask for a loan or wait until payday!")
        else:
            self.account -= debit
    
    #metodo para mostrar saldo
    def show_balance(self):
        print(f"Hi {self.name}, your balance is: {self.account}.")

    #BONUS: transferir a otro usuario
    def transfer_user(self,user2,transfer):
        user2.deposit_amount(transfer)
        self.take_money(transfer)
        print("successful transfer!")

#Creación de 3 instancias
annie = User("Annie","annie@mail.com")
carpe = User("Carpe", "diem@mail.com")
charlo = User("Charlo","lec@mail.com")

#Movimientos del primer usuario
annie.deposit_amount(100)
annie.deposit_amount(50)
annie.deposit_amount(200)
annie.take_money(125)
annie.show_balance()

#Movimientos del segundo usuario
carpe.deposit_amount(200)
carpe.deposit_amount(250)
carpe.take_money(100)
carpe.take_money(150)
carpe.show_balance()


#Movimientos del tercer usuario
charlo.deposit_amount(300)
charlo.take_money(100)
charlo.take_money(80)
charlo.take_money(230)
charlo.show_balance()

#transferir entre usuarios
annie.transfer_user(charlo,100)
annie.show_balance()
charlo.show_balance()