import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    def test_swapk_example_1(self):
        """Test swap_k with nums = [1, 2, 3, 4, 5, 6].
        and swap the last 2
        """

        nums = [1, 2, 3, 4, 5, 6]
        nums_expected = [ 5, 6, 3, 4, 1, 2]
        a1.swap_k(nums, 2)
        
        self.assertEqual(nums, nums_expected)

    def test_swapk_example_2(self):
        """Test swap_k with nums = [1, 2, 3].
        and dont swap any | nums, 0
        """

        nums = [1, 2, 3]
        nums_expected = [1, 2, 3]
        a1.swap_k(nums, 0)
        
        self.assertEqual(nums, nums_expected)


    def test_swapk_example_3(self):
        """Test swap_k with nums = [1, 1, 1, 1, 1, 1].
        and have all the numbers the same and swap 4
        """

        nums = [1, 1, 1, 1, 1, 1]
        nums_expected = [1, 1, 1, 1, 1, 1]
        a1.swap_k(nums, 4)
        
        self.assertEqual(nums, nums_expected)

    def test_swapk_example_4(self):
        """Test swap_k with nums = [2, 3]
        swapping a list with only 2 in the list but askign for 2 to be swapped
        """

        nums = [2, 3]
        nums_expected = [2, 3]
        a1.swap_k(nums, 2)
        
        self.assertEqual(nums, nums_expected)

        
if __name__ == '__main__':
    unittest.main(exit=False)
