
class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode(val)      #crea nodo
        current_head = self.head    #guarda quien es head ACTUAL
        new_node.next = current_head    #pone nodo nuevo junto a head actual
        self.head = new_node        #fija nodo creado a head
        return self

    def add_to_back(self, val):
        #si lista esta VACÍA
        # if self.head == None:
        #     self.add_to_front(val)
        #     return self         #saca de bucle y no ejecuta abajo
        new_node = SLNode(val)
        runner = self.head              #necesita de nuevo el iterador
        while(runner.next != None):     #"mientras runner tenga vecino"
            runner = runner.next        #sigue avanzando
        runner.next = new_node
        return self          #agrega nuevo nodo al final (al que no tenía next)

    def print_values (self):        #necesita un iterador diferente al no tener index
        runner = self.head          #puntero al primer nodo (asi define inicio)
        while (runner !=None):      #"mientras runner tenga un nodo"
            print(runner.value)
            runner = runner.next    #avanza a siguiente nodo
        return self

    #LOS 3 BONUS NINJAS: remover de inicio,medio,final
    def remove_from_front(self):
        current_head = self.head        #guarda head actual
        new_head = self.head.next       #guardo a donde apunta head actual 
        current_head.next = None        #le quita pointer a head "eliminandolo"
        self.head = new_head            #asigno head al que apuntaba anterior head
        print(f"Nodo eliminado: {current_head.value}")
        return self
    
    def remove_from_back (self):
        runner = self.head
        while(runner.next.next != None):  #mueve final al nodo siguiente del actual
            runner = runner.next
        print(f"Nodo eliminado: {runner.next.value}")    
        runner.next = None      #con estos None elimino el ultimo y dejo al nuevo ultimo sin pointer para que sea final de la lista
        return self
        

    def remove_val (self, val):
        runner = self.head
        if (runner.value == val):   #si el val a quitar esta de head
            return self.remove_from_front()
        while (runner.next.value != val):  #si esta en cualquier otra parte
            runner = runner.next
        newEnd = runner.next.next   #cuando encuentra el valor igual, cambia pointers del anteror y el siguiente para quitar este
        print(f"Nodo eliminado: {runner.next.value}") 
        runner.next = None 
        runner.next = newEnd  #conexta pointer al nodo siguiente al eliminado
        return self

class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

my_list= SList()
my_list.add_to_front("son").add_to_front("listas enlazadas").add_to_back("divertidas!").print_values().remove_from_back().print_values()

my_list2= SList()
my_list2.add_to_front("una lista").add_to_front("Esta es").add_to_back("enlazada simple").print_values().remove_from_front().print_values()

my_list3= SList()
my_list3.add_to_front("otra lista").add_to_front("Esta es").add_to_back("enlazada de prueba").print_values().remove_val("otra lista").print_values()

