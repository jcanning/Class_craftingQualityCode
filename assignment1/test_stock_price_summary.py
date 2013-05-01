import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_TSPS_example_1(self):
        """ Test stock_price_summary with [0.01, 0.03, -0.02, 0, 0, 0.10, -0.01]"""

        actual = a1.stock_price_summary([0.01, 0.03, -0.02, 0, 0, 0.10, -0.01])
        expected = (0.14, -0.03)
        self.assertEqual(actual, expected)


    def test_TSPS_example_2(self):
        """ Test stock_price_summary with no real vaules [0, 0, 0, 0]"""

        actual = a1.stock_price_summary([0, 0, 0, 0])
        expected = (0, 0)
        self.assertEqual(actual, expected)
                
    def test_TSPS_example_3(self):
        """ Test stock_price_summary with only negitive vaules [-0.12, -0.22, -0.01, -0.07]"""

        actual = a1.stock_price_summary([-0.12, -0.22, -0.01, -0.07])
        expected = (0, -0.42)
        self.assertEqual(actual, expected)

    def test_TSPS_example_3(self):
        """ Test stock_price_summary with only positive vaules [0.12, 0.22, 0.01, 0.07]"""

        actual = a1.stock_price_summary([0.12, 0.22, 0.01, 0.07])
        expected = (0.42, 0)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
