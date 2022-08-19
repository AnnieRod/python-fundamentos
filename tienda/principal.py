from producto import Product
from tienda import Store

#Creación de instancias
annies_shop = Store("Annie's market")
goldfish = Product("Goldfish Crackers", 5000, "Snacks") 
doritos = Product("Doritos", 2000, "Chips")
snickers = Product("Snickers",1000,"Candy")
sour = Product("Sour patch", 3000, "Candy")


#prueba de metodos de producto
goldfish.update_cost(is_higher=True, change_percent=0.5).print_info()
doritos.update_cost(is_higher=False, change_percent=0.5).print_info()

#prueba de metodos de tienda
annies_shop.add_product(goldfish).add_product(doritos).add_product(sour).add_product(snickers)
annies_shop.inflation(0.5).sale_promo(discount=0.2, category="Candy").inventory()
annies_shop.sell_product(2).inventory()
