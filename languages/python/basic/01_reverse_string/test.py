import unittest
import index

class TestReverseMethod(unittest.TestCase):

    def test_function_exists(self):
        self.assertEqual("reverse" in dir(index), True)

    def test_reverse_string(self):
        self.assertEqual(index.reverse('abcd'), 'dcba')

    def test_reverse_reversed_string(self):
        self.assertEqual(index.reverse('dcba  '), '  abcd')

if __name__ == '__main__':
    unittest.main()
