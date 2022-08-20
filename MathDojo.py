
class Mathdojo:
    def __init__(self):
        self.result = 0
    
    def add_num(self, num1, *numx):
        for num in numx:
            self.result += (num1 + num)
        return self

    def minus_num(self, num1, *numx):
        for num in numx:
            self.result -= (num1 + num)
        return self
    
md = Mathdojo()
x = md.add_num(2).add_num(2,5,1).minus_num(3,2).result
print(x)
