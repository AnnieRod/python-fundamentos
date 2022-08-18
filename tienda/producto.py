class Product: 
    def __init__(self, prod_name, cost, type):
        self.name = prod_name
        self.cost = cost
        self.type = type

    def update_cost(self,change_percent,is_higher): #nope
        if is_higher == True:
            self.cost += self.cost*change_percent
        else:
            self.cost -= self.cost*change_percent
        return self

    def print_info(self):
        print(f"Name: {self.name} - Category: {self.type} - Price: ${self.cost}")
        return self