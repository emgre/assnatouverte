from datetime import date
from unittest import TestCase

from assnatouverte.crawling.crawlers.legislatures_crawler import LegislaturesCrawler
from assnatouverte.database.database import Database
from assnatouverte.database.model.legislature import Legislature, Session
from tests.test_crawling.test_crawlers.mock_downloader import MockDownloader


class TestSessionsCrawler(TestCase):

    def setUp(self):
        self.crawler = LegislaturesCrawler()
        self.downloader = MockDownloader()
        self.database = Database.in_memory()

    def test_get_name(self):
        self.assertEqual(self.crawler.get_name(), 'legislatures')

    def test_crawl(self):
        self.downloader.register_page(
            'http://www.assnat.qc.ca/fr/patrimoine/datesessions.html', 'sessions.html')

        self.crawler.crawl(self.downloader, self.database)

        session = self.database.new_session()
        self.assertEqual(42, session.query(Legislature).count())
        self.assertEqual(145, session.query(Session).count())
        self.check_first_legislature(session.query(Legislature).get(1))

    def check_first_legislature(self, legislature: Legislature):
        self.assertEqual(1, legislature.id)
        self.assertEqual(4, len(legislature.sessions))

        first_session = legislature.sessions[0]
        self.assertEqual(1, first_session.legislature_id)
        self.assertEqual(1, first_session.session_id)
        self.assertEqual(date(1867, 12, 27), first_session.start_date)
        self.assertEqual(date(1868, 2, 24), first_session.prorogation_date)
        self.assertIsNone(first_session.dissolution_date)
        self.assertEqual(39, first_session.num_sittings)

        second_session = legislature.sessions[1]
        self.assertEqual(1, second_session.legislature_id)
        self.assertEqual(2, second_session.session_id)
        self.assertEqual(date(1869, 1, 20), second_session.start_date)
        self.assertEqual(date(1869, 4, 5), second_session.prorogation_date)
        self.assertIsNone(second_session.dissolution_date)
        self.assertEqual(48, second_session.num_sittings)

        third_session = legislature.sessions[2]
        self.assertEqual(1, third_session.legislature_id)
        self.assertEqual(3, third_session.session_id)
        self.assertEqual(date(1869, 11, 23), third_session.start_date)
        self.assertEqual(date(1870, 2, 1), third_session.prorogation_date)
        self.assertIsNone(third_session.dissolution_date)
        self.assertEqual(38, third_session.num_sittings)

        fourth_session = legislature.sessions[3]
        self.assertEqual(1, fourth_session.legislature_id)
        self.assertEqual(4, fourth_session.session_id)
        self.assertEqual(date(1870, 11, 3), fourth_session.start_date)
        self.assertEqual(date(1870, 12, 24), fourth_session.prorogation_date)
        self.assertEqual(date(1871, 5, 27), fourth_session.dissolution_date)
        self.assertEqual(38, fourth_session.num_sittings)
