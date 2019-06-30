from unittest import TestCase

from assnatouverte.crawling.crawlers.current_members_crawler import CurrentMembersCrawler
from assnatouverte.database.database import Database
from assnatouverte.database.model.member import Member
from tests.test_crawling.test_crawlers.mock_downloader import MockDownloader


class TestCurrentMembersCrawler(TestCase):

    def setUp(self):
        self.crawler = CurrentMembersCrawler()
        self.downloader = MockDownloader()
        self.database = Database.in_memory()

    def test_get_name(self):
        self.assertEqual(self.crawler.get_name(), 'current-members')

    def test_crawl(self):
        self.downloader.register_page('http://www.assnat.qc.ca/fr/deputes/index.html', 'current_members.html')

        self.crawler.crawl(self.downloader, self.database)

        session = self.database.new_session()
        self.assertEqual(session.query(Member).count(), 125)
        self.check_individual_member(session.query(Member).get('allaire-simon-17941'))
        self.check_member_without_email_address(session.query(Member).get('legault-francois-4131'))

    def check_individual_member(self, member: Member):
        self.assertEqual('allaire-simon-17941', member.id)
        self.assertEqual('Simon', member.first_name)
        self.assertEqual('Allaire', member.last_name)
        self.assertEqual('Maskinongé', member.electoral_division)
        self.assertEqual('Coalition avenir Québec', member.political_affiliation)
        self.assertEqual('Simon.Allaire.MASK@assnat.qc.ca', member.email)

    def check_member_without_email_address(self, member: Member):
        self.assertIsNone(member.email)
