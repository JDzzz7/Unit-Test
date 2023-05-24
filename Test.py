import unittest

# Testing Unittest decorators and features


class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")


def suite():
    s = unittest.TestSuite()
    s.addTest(ExpectedFailureTestCase("test_fail"))
    return s


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
    # unittest.main()
