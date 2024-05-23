
import unittest
from viet_badwords_filter.filter import VNBadwordsFilter

class TestVNBadwordsFilter(unittest.TestCase):

    def setUp(self):
        self.filter = VNBadwordsFilter()

    def test_is_profane(self):
        self.assertFalse(self.filter.is_profane("hello"))
        self.assertTrue(self.filter.is_profane("vcl"))

    def test_clean(self):
        self.assertEqual(self.filter.clean("hello vcl"), "hello ***")

if __name__ == '__main__':
    unittest.main()
