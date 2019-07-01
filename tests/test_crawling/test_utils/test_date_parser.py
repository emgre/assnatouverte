from unittest import TestCase

from datetime import date

from assnatouverte.crawling.utils.date_parser import parse_date


class TestDateParser(TestCase):

    def test_parse_basic_date(self):
        self.assertEqual(date(1977, 8, 16), parse_date('16 août 1977'))

    def test_parse_date_with_spaces(self):
        self.assertEqual(date(1935, 1, 8), parse_date('   8  janvier    1935    \n'))

    def test_parse_cased_date(self):
        self.assertEqual(date(1959, 11, 18), parse_date('18 Novembre 1959'))

    def test_parse_first_of_month(self):
        self.assertEqual(date(1870, 2, 1), parse_date('1er février 1870'))
