from sqlalchemy.orm import Session

from assnatouverte.crawling.downloader.downloader import Downloader
from assnatouverte.database.database import Database


class Crawler:

    def get_name(self) -> str:
        raise NotImplementedError

    def crawl(self, downloader: Downloader, database: Database):
        raise NotImplementedError


class SingleSessionCrawler(Crawler):

    def get_name(self) -> str:
        raise NotImplementedError

    def crawl(self, downloader: Downloader, database: Database):
        session = database.new_session()
        try:
            self.crawl_with_session(downloader, session)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    def crawl_with_session(self, downloader: Downloader, session: Session):
        raise NotImplementedError
