class AlwayPositive:
    
    def __init__(self,n):
        self.number = n
        
    def __add__(self,other):
        return abs(self.number + other.number)
        
a = AlwayPositive(20)
b = AlwayPositive(-100)

print(a+b)
