class Shape:
    def __init__(self, area):
        self.area = 0
class Rectangle(Shape):
    def __init__(self, length, width, area):
        self.length = length
        self.width = width
        super().__init__(area)
    def get_area(self):
        return self.length*self.width
S1 = Rectangle(4, 5, 0)
S2 = Rectangle(6, 4, 0)  
print(S1.get_area(), S2.get_area(), sep = '\n') 
