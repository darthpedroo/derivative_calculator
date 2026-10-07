import math

# https://docs.python.org/3/library/ast.html

class Derivable():
    def derivar():
        return 

class ExponentialExpression(Derivable):
    def __init__(self, base: float, exponent: str):
        self.base = base
        self.exponent = exponent

    def __str__(self):
        return f"{self.base}^{self.exponent}"

    def derivar(self):
        return f"ln({self.base}) * {self.base}^{self.exponent}"

class PolynomialExpression(Derivable):
    def __init__(self,base:str,exponent:float):
        self.base = base
        self.exponent = exponent

    def __str__(self):
        return f"{self.base}^{self.exponent}" 

    def derivar(self):
        if self.exponent == 1:
            return "1"
        return f"{self.exponent}{self.base}^{self.exponent - 1}"


def derivate_sumed_expressions(expresiones: list[Derivable]):
    
    suma_final = ""

    for expresion in expresiones:
        suma_final+= f"\t{expresion.derivar()}\t+"

    return suma_final[:-1]

def derivate_product_expressions(expressions:list[Derivable]):
    return 

def main():
    print("derivative calculator")
    a = PolynomialExpression("x",1)
    b = ExponentialExpression(2, "x")
    res = derivate_sumed_expressions([a,b])
    print(res)
    return 

if __name__ == "__main__":
    main()
