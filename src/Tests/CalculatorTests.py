import unittest
from Calculator.Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(calculator.result, 0)

    def test_add_method_calculator(self):
        self.assertEqual(calculator.add(2, 2), 4)
        self.assertEqual(calculator.result, 4)

    def test_subtract_method_calculator(self):
        self.assertEqual(calculator.subtract(2, 2), 0)
        self.assertEqual(calculator.result, 0)

if __name__ == '__main__':
    unittest.main()