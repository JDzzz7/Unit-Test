import unittest


class AutomationTests(unittest.TestCase):
    def setUp(self):
        self.num = 0
        self.s = "Foo bar baz"
        self.lst = []
        for i in range(7):
            self.lst.append(i)

    def test_equal(self):
        self.assertEqual(self.num, self.lst[0], "0 == 0")
        self.assertFalse(self.s[:3] == self.s[4:7], "Foo != bar")
        self.assertTrue(len(self.lst)-1 == self.lst[6], "6 == 6")

    def test_match(self):
        self.assertIn("baz", self.s)
        self.assertEqual(len(self.s), 11)

    def test_zero(self):
        self.assertEqual(0, self.lst[0])

    def tearDown(self):
        self.num = 0
        self.s = ''
        self.lst = []


def suite():
    suites = unittest.TestSuite()
    suites.addTest(AutomationTests("test_equal"))
    suites.addTest(AutomationTests("test_match"))
    return suites


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
    unittest.main()
