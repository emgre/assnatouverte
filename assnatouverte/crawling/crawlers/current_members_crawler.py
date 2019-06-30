import re

from parsel import Selector, SelectorList

from assnatouverte.crawling.crawler import Crawler
from assnatouverte.crawling.downloader.downloader import Downloader
from assnatouverte.database.database import Database
from assnatouverte.database.model.member import Member


class CurrentMembersCrawler(Crawler):
    def get_name(self) -> str:
        return 'current-members'

    def crawl(self, downloader: Downloader, database: Database):
        session = database.new_session()

        try:
            page = Selector(downloader.get_text('http://www.assnat.qc.ca/fr/deputes/index.html'))
            rows = page.xpath('//table[@id="ListeDeputes"]/tbody/tr')

            for row in rows:
                member = self.extract_single_member(row)
                session.merge(member)

            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    @staticmethod
    def extract_single_member(row: SelectorList) -> Member:
        # Extract ID
        details_url = row.xpath('./td[1]/a/@href').get()
        match = re.search(r'/([a-z0-9\-]+)/index.html', details_url)
        if match:
            member_id = match.group(1)
        else:
            raise Exception(f'Could not find member id in {details_url}')

        # Extract name
        full_name = row.xpath('./td[1]/a/text()').get()
        splitted_name = full_name.split(',', maxsplit=1)
        first_name = splitted_name[1].strip()
        last_name = splitted_name[0].strip()

        # Extract electoral division
        electoral_division = row.xpath('./td[2]/text()').get().strip()

        # Extract political affiliation
        political_affiliation = row.xpath('./td[3]/text()').get().strip()

        # Extract email
        email = None
        email_link = row.xpath('./td[4]//a/@href').get()
        match = re.search(r'mailto:(.+)', email_link)
        if match:
            email = match.group(1)

        return Member(
            id=member_id,
            first_name=first_name,
            last_name=last_name,
            electoral_division=electoral_division,
            political_affiliation=political_affiliation,
            email=email
        )
