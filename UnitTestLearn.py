import unittest


class TestStringMethod(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO', msg='this is fine')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper(), msg='true')
        self.assertFalse('foo'.isupper(), msg='false')

    def test_split(self):
        string = 'unit test'
        self.assertEqual(string.split(), ['unit', 'test'], msg='yes')

        with self.assertRaises(TypeError):
            string.split(2)

    # def test_length(self):
    #     s = 'AOK'
    #     self.assertFalse(len(s) == 3)
    #     self.assertTrue(len(s) == 5, "testing")


if __name__ == '__main__':
    unittest.main()
