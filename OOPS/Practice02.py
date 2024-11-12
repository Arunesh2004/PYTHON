class Fraction:
    
    # Using different magic methods :
    
    def __init__(self, x, y):
        
        self.num = x
        self.den = y
        
    def __str__(self):
        return "{}/{}".format(self.num, self.den)
    
    def __add__(self, other):
        temp_num = self.num*other.den + self.den*other.num
        temp_den = self.den*other.den
        
        return Fraction(temp_num, temp_den)
        
    def __sub__(self, other):
        temp_num = self.num*other.den - self.den*other.num
        temp_den = self.den*other.den
        
        return Fraction(temp_num, temp_den)
        
    def __mul__(self, other):
        temp_num = self.num*other.num
        temp_den = self.den*other.den
        
        return Fraction(temp_num, temp_den)
        
    def __truediv__(self, other):
        temp_num = self.num*other.den
        temp_den = self.den*other.num
        
        return Fraction(temp_num, temp_den)

# Creating two fractions and performing operations on them.


    
x = Fraction(6, 5)
y = Fraction(9, 8)

print(x + y)
print(x - y)
print(x * y)
print(x / y)
