
class Store:
    def __init__(self, name):
        self.name = name
        self.product = []

    def add_product(self,new_product):  #actualiza para que recorrar lista de productos
        self.product.append(new_product)
        print(f"{new_product.name} added to the store")
        return self  

    def sell_product(self, id):
        print(f"{self.product[id].name} sold!")
        del self.product[id]
        return self

    def inflation(self, add_percentage):
        for thing in self.product:
            thing.update_cost(add_percentage, is_higher=True)
        return self

    def sale_promo(self,category,discount):
        for thing in self.product:
            if thing.type == category:
                thing.update_cost(discount, is_higher=False)
        return self

    #Metodo de "inventario"
    def inventory(self):
        for thing in self.product:
            thing.print_info()
        return self
