from crawling.crawler import Crawler
from crawling.downloader.downloader import Downloader
from database.database import Database


class CurrentMembersCrawler(Crawler):
    name = "current-members"

    def crawl(self, downloader: Downloader, db: Database):
        print('Hello')
