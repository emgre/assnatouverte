from parsel import Selector

from assnatouverte.crawling.crawler import SingleSessionCrawler
from assnatouverte.crawling.downloader.downloader import Downloader
from assnatouverte.crawling.utils.date_parser import parse_date
from assnatouverte.database.model.legislature import Legislature, Session


class LegislaturesCrawler(SingleSessionCrawler):
    def get_name(self) -> str:
        return 'legislatures'

    def crawl_with_session(self, downloader: Downloader, session: Session):
        page = Selector(downloader.get_text('http://www.assnat.qc.ca/fr/patrimoine/datesessions.html'))
        rows = page.xpath('//table[contains(@class, "tableauLegisSessionsDepuis1867")]/tbody/tr[position()>3]')

        current_legislature = Legislature()
        for row in rows:
            # Extract legislature
            try:
                current_legislature_id = int(row.xpath('./td[1]/text()').get())
                if current_legislature_id != current_legislature.id:
                    current_legislature = Legislature(id=current_legislature_id)
            except:
                pass

            # Extract session
            try:
                session_id = int(row.xpath('./td[2]/text()').get())
            except:
                continue

            # Extract dates
            start_date_str = row.xpath('string(./td[3])').get()
            if start_date_str:
                start_date = parse_date(start_date_str)

            prorogation_date_str = row.xpath('string(./td[4])').get()
            if prorogation_date_str:
                prorogation_date = parse_date(prorogation_date_str)

            dissolution_date_str = row.xpath('string(./td[5])').get()
            if dissolution_date_str:
                dissolution_date = parse_date(dissolution_date_str)

            # Extract number of sittings
            try:
                num_sittings = int(row.xpath('./td[6]/text()').get())
            except:
                pass

            legislature_session = Session(
                legislature=current_legislature,
                session_id=session_id,
                start_date=start_date,
                prorogation_date=prorogation_date,
                dissolution_date=dissolution_date,
                num_sittings=num_sittings,
            )

            session.merge(legislature_session)
