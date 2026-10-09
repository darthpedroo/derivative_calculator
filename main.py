from __future__ import annotations
from core.polynomials import MonomialExpression, PolynomialExpression, Sin,Cos,Expression

def main():
    print("derivative calculator\n")
    
    a = MonomialExpression(coefficient=2,base="x",exponent=1)
    b = MonomialExpression(coefficient=1, base="x",exponent=3)
    c = MonomialExpression(coefficient=10, base="x",exponent=7)
    d = MonomialExpression(coefficient=6,base="x",exponent=0) 

    print("--- a y su derivada ---")
    print(a)
    print(a.derivate())
    
    polynomial = PolynomialExpression(monomials=[a,b,b*c,d])
    
    print("polynomial")
    print(polynomial)
    
    print("derivated polynomial")
    print(polynomial.derivate())
    
    a1 = PolynomialExpression(monomials=[b,b,b])
    a2 = PolynomialExpression(monomials=[b,b,b])

    
    cos = MonomialExpression(coefficient=1, base=Cos(b),exponent=1)

    a*cos 

    print(isinstance(cos,Expression))

    print(cos)

    print(cos.derivate())
    
    #print(a1 + a2)
        
    return 

if __name__ == "__main__":
    main()
