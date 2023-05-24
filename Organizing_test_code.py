import unittest

'''
assertEqual(first, second, msg=None) # Test if first == second
assertTrue(expr, msg=None) # Test if the expression is TRUE
assertFalse(expr, msg=None) # Test if the expression is FAlSE
assertIn(member, container, msg=None) # Test if member is IN container
assertNotIn(member, container, msg=None) # Test if member is NOT IN container
'''


class TestTrials(unittest.TestCase):
    # Setup variables for testing
    def setUp(self):
        self.s = "foo bar"
        self.d = {0: 'x', 1: 'y', 2: 'z'}
        self.lst = [7 for i in range(len(self.s))]
        self.num1 = 10
        self.num2 = 20

    # Test for greater than
    def test_greater(self):
        self.assertTrue(self.num2 > self.num1)
        self.assertTrue(len(self.d) > 1)
        self.assertTrue(self.lst[0] > len(self.d))

    # Test for less than
    def test_lesser(self):
        self.assertTrue(len(self.s[:6]) < (self.num2-self.num1))
        self.assertTrue(len(self.lst) < self.num2)

    # Test for value equivalence
    def test_equal(self):
        self.assertEqual(self.s.upper(), "FOO BAR")
        self.assertEqual(self.d[1], 'y')
        self.assertTrue(self.s[:3] == "foo")
        self.assertTrue(self.num1 == (self.num2/2))

    # Test for value non equivalence
    def test_notEqual(self):
        self.assertFalse(len(self.lst) != len(self.s))
        self.assertFalse(len(self.d[2]) == 'j')
        self.assertFalse(self.num1 == self.num2)

    # Test split variables
    def test_split(self):
        self.assertEqual(self.s.split(), ["foo", "bar"])

    # Test for membership
    def test_contains(self):
        self.assertIn(0, self.d)
        self.assertIn(7, self.lst)
        self.assertIn("foo", self.s)

    # Test for empty
    def test_empty(self):
        s = ''
        self.assertEqual(len(s), 0)

    # Clean up function
    def tearDown(self):
        pass


# Customize building of test suite to pick and choose which tests to run
# Returns a TestSuite
def suite_bundle():
    suite = unittest.TestSuite()
    suite.addTest(TestTrials("test_greater"))
    suite.addTest(TestTrials("test_lesser"))
    suite.addTest(TestTrials("test_equal"))
    return suite


# Driver function
if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite_bundle())
    # unittest.main()
