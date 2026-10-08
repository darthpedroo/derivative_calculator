import unittest
from main import MonomialExpression,PolynomialExpression

class TestsMonomial(unittest.TestCase):
    
    def test_sum_monomial_with_same_base(self):
        a = MonomialExpression(coefficient=2,base="x",exponent=2)
        b = MonomialExpression(coefficient=2,base="x",exponent=2)
        
        sum = a + b
        expected_res = MonomialExpression(coefficient=4,base="x",exponent=2) 
        
        self.assertEqual(sum,expected_res)
    
    def test_sum_monomial_with_different_base(self):
        a = MonomialExpression(coefficient=2,base="x",exponent=2)
        b = MonomialExpression(coefficient=2,base="y",exponent=2)
        
        with self.assertRaises(ArithmeticError):        
            sum = a + b
    
    def test_sum_monomial_with_different_exponent(self):
        a = MonomialExpression(coefficient=2,base="x",exponent=2)
        b = MonomialExpression(coefficient=2,base="x",exponent=3)
                        
        with self.assertRaises(ArithmeticError):        
            sum = a + b
            
    def test_sum_scalar_to_monomial(self):
        a = MonomialExpression(coefficient=2,base="x",exponent=3)
        b = 1
        
        with self.assertRaises(NotImplementedError):
            sum = a + b
            
    def test_sub_monomial_with_same_base(self):
            a = MonomialExpression(coefficient=1,base="x",exponent=2)
            b = MonomialExpression(coefficient=2,base="x",exponent=2)
            
            sub = a - b
            expected_res = MonomialExpression(coefficient=-1,base="x",exponent=2) 
            
            self.assertEqual(sub,expected_res)
        
    def test_sub_monomial_with_different_base(self):
        a = MonomialExpression(coefficient=2,base="x",exponent=2)
        b = MonomialExpression(coefficient=2,base="y",exponent=2)
        
                
        with self.assertRaises(ArithmeticError):        
            sub = a - b
        
    def test_sum_monomial_with_different_exponent(self):
        a = MonomialExpression(coefficient=2,base="x",exponent=2)
        b = MonomialExpression(coefficient=2,base="x",exponent=3)
                        
        with self.assertRaises(ArithmeticError):        
            sub = a - b
    
    def test_multiply_monomial_that_works(self):
        a = MonomialExpression(coefficient=2,base="x",exponent=1)
        b = MonomialExpression(coefficient=3,base="x",exponent=1)
        
        multiplication = a * b
        expected_res = MonomialExpression(coefficient=6,base="x",exponent=2)
        self.assertEqual(multiplication,expected_res)
        
    def test_multiply_monomials_with_different_exponents(self):
        a = MonomialExpression(coefficient=6,base="x",exponent=2)
        b = MonomialExpression(coefficient=3,base="x",exponent=8)
                
        multiplication = a * b
        expected_res = MonomialExpression(coefficient=18,base="x",exponent=10)
        self.assertEqual(multiplication,expected_res)
    
    def test_multiply_monomial_and_scalar(self):
        a = MonomialExpression(coefficient=3,base="x",exponent=5)
        b = 10
        c = 1/2
        
        multiplication = a * b * c
        expected_res = MonomialExpression(coefficient=15,base="x",exponent=5)
        
        self.assertEqual(multiplication,expected_res)
    
    def test_multiply_monomial_raises_arithmetic_error(self):
        a = MonomialExpression(coefficient=6,base="x",exponent=2)
        b = "Test"
        
        with self.assertRaises(ArithmeticError):      
            multiplication = a * b
    
    def test_derivate_simple_monomial_expression(self):
        a = MonomialExpression(coefficient=2,base="x",exponent=3)
        expected_res = MonomialExpression(coefficient=6,base="x",exponent=2)

        self.assertEqual(a.derivate(),expected_res)
    
class TestsPolynomial(unittest.TestCase):
    def test_sum_monomial_to_polynomial(self):
        b = MonomialExpression(coefficient=10, base="y",exponent=7)
        a2 = PolynomialExpression()
        
        sum = a2 + b
        expected_res = PolynomialExpression(monomials=[b])
        
        self.assertEqual(sum,expected_res)
    
    def test_sum_polynomial_to_polynomial(self):
        
        b = MonomialExpression(coefficient=10, base="y",exponent=7)
        
        a1 = PolynomialExpression(monomials=[b,b,b])
        a2 = PolynomialExpression(monomials=[b,b,b])
        
        with self.assertRaises(NotImplementedError):
            sum = a1 + a2
        
        
if __name__ == "__main__":
    unittest.main()