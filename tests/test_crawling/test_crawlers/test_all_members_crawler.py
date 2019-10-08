from unittest import TestCase

from assnatouverte.crawling.crawlers.all_members_crawler import AllMembersCrawler
from assnatouverte.database.database import Database
from assnatouverte.database.model.member import Member
from tests.test_crawling.test_crawlers.mock_downloader import MockDownloader


class TestAllMembersCrawler(TestCase):

    def setUp(self):
        self.crawler = AllMembersCrawler()
        self.downloader = MockDownloader()
        self.downloader.register_page('http://www.assnat.qc.ca/fr/membres/notices/index.html', 'all_members_1.html')
        self.database = Database.in_memory()

    def test_get_name(self):
        self.assertEqual(self.crawler.get_name(), 'all-members')

    def test_find_pages(self):
        pages = list(self.crawler.find_pages(self.downloader))

        self.assertEqual(16, len(pages))
        self.assertEqual('http://www.assnat.qc.ca/fr/membres/notices/index.html', pages[0])
        self.assertEqual('http://www.assnat.qc.ca/fr/membres/notices/index-vz.html', pages[15])

    def test_extract_members(self):
        members = list(self.crawler.extract_members('http://www.assnat.qc.ca/fr/membres/notices/index.html',
                                                    self.downloader))

        self.assertEqual(64, len(members))

    def test_extract_members_with_id_with_parantheses(self):
        self.downloader.register_page('http://www.assnat.qc.ca/fr/membres/notices/index-b.html', 'all_members_2.html')

        session = self.database.new_session()
        session.add_all(list(self.crawler.extract_members('http://www.assnat.qc.ca/fr/membres/notices/index-b.html',
                                                          self.downloader)))
        session.commit()

        member = session.query(Member).get('bryson-(fils)-george-75')
        self.assertEqual('George', member.first_name)
        self.assertEqual('Bryson', member.last_name)
        self.assertEqual('fils', member.name_details)
