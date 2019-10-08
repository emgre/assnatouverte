import logging
from typing import Iterable

from parsel import Selector
from sqlalchemy.orm import Session

from assnatouverte.crawling.crawler import SingleSessionCrawler
from assnatouverte.crawling.downloader.downloader import Downloader
from assnatouverte.crawling.utils.string_utils import extract_member_id, extract_parentheses
from assnatouverte.database.model.member import Member


class AllMembersCrawler(SingleSessionCrawler):
    def __init__(self):
        self._logger = logging.getLogger(__name__)

    def get_name(self) -> str:
        return 'all-members'

    def crawl_with_session(self, downloader: Downloader, session: Session):
        pages = self.find_pages(downloader)
        for page in pages:
            members = self.extract_members(page, downloader)

            for member in members:
                session.merge(member)

    @staticmethod
    def find_pages(downloader: Downloader) -> Iterable[str]:
        index = Selector(downloader.get_text('http://www.assnat.qc.ca/fr/membres/notices/index.html'))
        links = index.xpath('//div[contains(@class, colonneImbriquee)]/p[3]/a/@href')

        for link in links:
            yield f'http://www.assnat.qc.ca{link.get()}'

    def extract_members(self, url: str, downloader: Downloader) -> Iterable[Member]:
        self._logger.info(f'Crawling {url}')
        page = Selector(downloader.get_text(url))
        links = page.xpath('//div[contains(@class, colonneImbriquee)]/div[position()=4 or position()=5]/div/a')
        for link in links:
            # Extract ID
            details_url = link.attrib['href']
            member_id = extract_member_id(details_url)
            if not member_id:
                raise Exception(f'Could not find member id in {details_url}')

            # Extract name
            full_name = link.xpath('./text()').get()
            splitted_name = full_name.split(',', maxsplit=1)
            first_name = splitted_name[1].strip()
            last_name = splitted_name[0].strip()
            # If there is text in parentheses, then it's details
            # to help distinguish members
            last_name, name_details = extract_parentheses(last_name)

            self._logger.debug(f'Found {first_name} {last_name}')
            yield Member(
                id=member_id,
                first_name=first_name,
                last_name=last_name,
                name_details=name_details,
            )
