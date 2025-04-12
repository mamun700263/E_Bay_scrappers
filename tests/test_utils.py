import unittest
from ebay_scraper.utils.common import file_formate_checker

class TestUtilCommon(unittest.TestCase):

    def test_file_format_checker_valid(self):
        self.assertEqual(file_formate_checker("data.csv"), "csv")
        self.assertEqual(file_formate_checker("data.json"), "json")
        self.assertEqual(file_formate_checker("data.xlsx"), "xlsx")

    def test_file_format_checker_invalid(self):
        with self.assertRaises(ValueError):
            file_formate_checker("data.txt")
