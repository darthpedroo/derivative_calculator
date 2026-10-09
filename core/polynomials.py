from __future__ import annotations
from abc import ABC
from math import cos

class Derivable(ABC):
    def derivate():
        return 

class Expression(Derivable):
    
    def derivate():
        pass


class Sin(Expression):
    def __init__(self,value:Expression):
        self.value = value

    def __str__(self):
        return f"sin({str(self.value)})"
    
class Cos(Expression):
    def __init__(self, value: Expression):
        self.value = value

    def __str__(self):
        return f"cos({str(self.value)})"

    def derivate(self) -> Expression:
        return MonomialExpression(
            coefficient=-1,
            base=Sin(self.value),
            exponent=1,
        )

class Product(Expression):
    def __init__(self, terms: list[Expression]):
        self.terms = terms

class MonomialExpression(Expression):
    
    def __init__(self,coefficient:int, base:Expression,exponent:float):
        self.coefficient = coefficient
        self.base = base
        self.exponent = exponent

    def __str__(self):

        if self.exponent == 0:
            return f"{self.coefficient}"
        
        if self.coefficient == 0:
            return "0"

        if self.exponent == 1:
            return f"{self.coefficient}{self.base}"    
        
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
            
            print(type(self.base))
            print(type(other.base))
            
            return MonomialExpression(
                coefficient=self.coefficient * other.coefficient,
                base = self.base * other.base,
                exponent=1
            )

        raise ArithmeticError(f"Error trying to multiply monomials of type: {type(self)} and {type(other)}")               
    
    def derivate(self) -> MonomialExpression:
        
        return MonomialExpression(
            coefficient=self.coefficient*(self.exponent),
            base=self.base,
            exponent=self.exponent-1)
        
class PolynomialExpression(Expression):
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