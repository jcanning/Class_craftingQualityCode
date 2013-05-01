import a1
import unittest

class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    # Add your test methods for a1.num_buses here.
    def test_numbuses_example_1(self):
        """ Test num_buses with 75. """

        actual = a1.num_buses(75)
        expected = 2
        self.assertEqual(actual, expected)

    def test_numbuses_example_2(self):
        """ Test num_buses with 49."""

        actual = a1.num_buses(49)
        expected = 1
        self.assertEqual(actual, expected)

    def test_numbuses_example_3(self):
        """ Test num_buses with 222."""

        actual = a1.num_buses(222)
        expected = 5
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
