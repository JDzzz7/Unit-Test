import unittest

# Testing Unittest decorators and features


class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")


class NumbersTest(unittest.TestCase):

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)


def suite():
    s = unittest.TestSuite()
    s.addTest((NumbersTest("test_even")))
    # s.addTest(ExpectedFailureTestCase("test_fail"))
    return s


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
    # unittest.main()
