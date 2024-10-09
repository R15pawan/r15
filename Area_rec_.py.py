class Rectangle():
    def __init__(self,l,w):
        self.length =l
        self.width = w
        
    def reactangle_area(self):
        return self.length * self.width
    
newReactangle = Rectangle(12,8)
print("Area of rectangle is:", newReactangle.reactangle_area())