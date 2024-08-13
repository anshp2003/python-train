
# import unittest

# # Function to be tested
# def add(a, b):
#     return a + b

# # Test case
# class TestAddFunction(unittest.TestCase):
#     def test_add_integers(self):
#         self.assertEqual(add(1, 2), 3)

#     def test_add_floats(self):
#         self.assertEqual(add(1.1, 2.2), 3.3000000000000003)

#     def test_add_strings(self):
#         self.assertEqual(add("hello", " world"), "hello world")

# if __name__ == '__main__':
#     unittest.main()


# """
# Another method of Assert in unittesting

# """


# import unittest

# def is_even(n):
#     return n % 2 == 0


# class Test_example(unittest.TestCase):
#     def test_even_number(self):
#         self.assertTrue(is_even(4))
    
#     def test_odd_number(self):
#         self.assertFalse(is_even(5))

# if __name__ == '__main__':
#     unittest.main()        



import unittest

def get_fruits():
    return ["apple","banana","mango"]


class testfruit(unittest.TestCase):
    def test_fruits(self):
        self.assertIn("mango",get_fruits())



if __name__ == '__main__':
    unittest.main()        


"""summary of Assert Methods
assertTrue(expr): Checks that the expression expr is true.
assertFalse(expr): Checks that the expression expr is false.
assertIn(item, container): Checks that item is in container.
assertNotIn(item, container): Checks that item is not in container.
assertIsNone(obj): Checks that obj is None.
assertIsNotNone(obj): Checks that obj is not None.
assertRaises(exception, callable, *args, **kwargs): Checks that callable raises the specified exception when called with args and kwargs.
assertEqual(first, second): Checks that first and second are equal.
assertNotEqual(first, second): Checks that first and second are not equal."""
