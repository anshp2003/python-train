import unittest

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b


class Testtask(unittest.TestCase):
    def Test_add(self):
        self.assertEqual(add(5,5),10)

    def Test_sub(self):
        self.assertEqual(sub(5,5),0)

    def Test_mul(self):
        self.assertEqual(mul(5,5),25)        

    def Test_div(self):
        self.assertEqual(div(5,5),0)    


if __name__ =="__main__":
    unittest.main()        


class MathOperations:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
import unittest

class TestMathOperations(unittest.TestCase):
    
    def setUp(self):
        self.math_ops = MathOperations()
    
    def test_add(self):
        self.assertEqual(self.math_ops.add(1, 2), 3)
        self.assertEqual(self.math_ops.add(-1, 1), 0)
        self.assertEqual(self.math_ops.add(-1, -1), -2)
    
    def test_subtract(self):
        self.assertEqual(self.math_ops.subtract(5, 3), 2)
        self.assertEqual(self.math_ops.subtract(3, 5), -2)
        self.assertEqual(self.math_ops.subtract(-1, -1), 0)
    
    def test_multiply(self):
        self.assertEqual(self.math_ops.multiply(2, 3), 6)
        self.assertEqual(self.math_ops.multiply(-1, 1), -1)
        self.assertEqual(self.math_ops.multiply(-1, -1), 1)
    
    def test_divide(self):
        self.assertEqual(self.math_ops.divide(6, 3), 2)
        self.assertEqual(self.math_ops.divide(-6, -3), 2)
        self.assertEqual(self.math_ops.divide(-6, 3), -2)
        with self.assertRaises(ValueError):
            self.math_ops.divide(1, 0)

if __name__ == '__main__':
    unittest.main()

