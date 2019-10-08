import re

from parsel import Selector, SelectorList
from sqlalchemy.orm import Session

from assnatouverte.crawling.crawler import SingleSessionCrawler
from assnatouverte.crawling.downloader.downloader import Downloader
from assnatouverte.crawling.utils.string_utils import extract_member_id
from assnatouverte.database.model.member import Member


class CurrentMembersCrawler(SingleSessionCrawler):
    def get_name(self) -> str:
        return 'current-members'

    def crawl_with_session(self, downloader: Downloader, session: Session):
        page = Selector(downloader.get_text('http://www.assnat.qc.ca/fr/deputes/index.html'))
        rows = page.xpath('//table[@id="ListeDeputes"]/tbody/tr')

        for row in rows:
            member = self.extract_single_member(row)
            session.merge(member)

    @staticmethod
    def extract_single_member(row: SelectorList) -> Member:
        # Extract ID
        details_url = row.xpath('./td[1]/a/@href').get()
        member_id = extract_member_id(details_url)
        if not member_id:
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
