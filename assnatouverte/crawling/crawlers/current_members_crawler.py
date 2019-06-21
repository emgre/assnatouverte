from assnatouverte.crawling.crawler import Crawler
from assnatouverte.crawling.downloader.downloader import Downloader
from assnatouverte.database.database import Database


class CurrentMembersCrawler(Crawler):
    def get_name(self) -> str:
        return 'current-members'

    def crawl(self, downloader: Downloader, database: Database):
        print('Hello')
