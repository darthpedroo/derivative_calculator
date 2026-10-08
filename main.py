import math

# https://docs.python.org/3/library/ast.html

class Derivable():
    def derivate():
        return 

class PolynomialExpression(Derivable):
    def __init__(self, monomials: list[MonomialExpression] =[]):
        self.monomials = monomials
    
    def __str__(self):
        polynomial = ""
        for monomial in self.monomials:
            polynomial += str(monomial) + " + "
        
        polynomial = polynomial[:-3]
        return polynomial
    
    def __eq__(self, value:PolynomialExpression):
        return self.monomials == value.monomials
    
    def __add__(self, other):

        if isinstance(other,MonomialExpression):
            self.monomials.append(other)
            return PolynomialExpression(self.monomials)
        
        raise NotImplementedError()
            
    def derivate(self) -> PolynomialExpression:
        derivated_polynomial = PolynomialExpression()
        
        for monomial in self.monomials:
            derivated_polynomial += (monomial.derivate())    
        
        return derivated_polynomial

class MonomialExpression(Derivable):
    
    def __init__(self,coefficient:int, base:str="x",exponent:float=0):
        self.coefficient = coefficient
        self.base = base
        self.exponent = exponent

    def __str__(self):
        
        if self.exponent == 0:
            return f"{self.coefficient}"
        
        if self.coefficient == 0:
            return "0"
        
        return f"{self.coefficient}{self.base}^{self.exponent}"
    
    def __eq__(self, value:MonomialExpression):
        return (self.coefficient == value.coefficient)and (self.base == value.base) and (self.exponent == value.exponent) 
        
    
    def __add__(self, other:MonomialExpression | float | int):

        if isinstance(other,MonomialExpression):
            if self.base == other.base and self.exponent == other.exponent:
                return MonomialExpression(coefficient=(self.coefficient + other.coefficient),
                                            base=self.base,
                                            exponent=self.exponent)
        
            raise ArithmeticError("Monomials must have the same base and exponent to Sum")

        raise NotImplementedError()

    def __sub__(self, other):
        if self.base == other.base and self.exponent == other.exponent:
                return MonomialExpression(
                    coefficient=(self.coefficient - other.coefficient),
                    base=self.base,
                    exponent=self.exponent)
                
        raise ArithmeticError("Monomials must have the same base and exponent to Sum")
    
    def __mul__(self, other):
        
        if isinstance(other, float) or isinstance(other, int):
            return MonomialExpression(
                coefficient=self.coefficient*other,
                base=self.base,
                exponent=self.exponent
            )
        
        if isinstance(other, MonomialExpression):
            
            if self.base == other.base:
                return MonomialExpression(
                    coefficient= self.coefficient * other.coefficient,
                    base=self.base,
                    exponent= self.exponent + other.exponent
                )
            
            raise NotImplementedError()
        
        raise ArithmeticError(f"Error trying to multiply monomials of type: {type(self)} and {type(other)}")               
    
    def derivate(self) -> MonomialExpression:
        
        return MonomialExpression(
            coefficient=self.coefficient*(self.exponent),
            base=self.base,
            exponent=self.exponent-1)
        

def main():
    print("derivative calculator\n")
    
    a = MonomialExpression(coefficient=2,base="x",exponent=3)
    b = MonomialExpression(coefficient=10, base="y",exponent=7)
    c = MonomialExpression(coefficient=10, base="y",exponent=7)
    d = MonomialExpression(coefficient=6) 
    
    print(a)
    print(a.derivate())
    
    polynomial = PolynomialExpression(monomials=[a,b,b*c,d])
    
    print("polynomial")
    print(polynomial)
    
    print("derivated polynomial")
    print(polynomial.derivate())
    
    a1 = PolynomialExpression(monomials=[b,b,b])
    a2 = PolynomialExpression(monomials=[b,b,b])
    
    print(a1 + a2)
    
    
    return 

if __name__ == "__main__":
    main()
