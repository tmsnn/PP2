class Shape:
    def __init__(self, area):
        self.area = 0
class Square(Shape):
    def __init__(self, length, area):
        self.length = length
        super().__init__(area)
    def get_area(self):
        return self.length*self.length
S1 = Square(4, 0)
S2 = Square(6, 0)  
print(S1.get_area(), S2.get_area(), sep = '\n') 
