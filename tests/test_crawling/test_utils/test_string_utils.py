from unittest import TestCase

from assnatouverte.crawling.utils.string_utils import extract_member_id, extract_parentheses


class TestStringUtils(TestCase):

    def test_extract_member_id(self):
        self.assertEqual('baril-(pq)-gilles-1845', extract_member_id('/fr/deputes/baril-(pq)-gilles-1845/index.html'))

    def test_extract_member_id_no_index(self):
        self.assertEqual('burton-francis-nathaniel-83',
                         extract_member_id('/fr/patrimoine/anciens-parlementaires/burton-francis-nathaniel-83.html'))

    def test_extract_parentheses(self):
        self.assertEqual(('Bryson', 'Cité Limoilou'), extract_parentheses('Bryson (Cité Limoilou)'))

    def test_extract_parentheses_without_parenthese(self):
        self.assertEqual(('test', None), extract_parentheses('test'))
