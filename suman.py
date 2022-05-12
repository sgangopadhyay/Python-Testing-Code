import math 

class Guvi:

    def odd_even(self, number):
        if(number%2==0):
            return "EVEN"
        else:
            return "ODD"

    def NameUpper(self, data):
        return data.upper()

    def NameLower(self, data):
        return data.lower()
    
    def SquareRoot(self, number):
        return math.sqrt(number)
    
    def NumberSquare(self, number):
        return number*number
