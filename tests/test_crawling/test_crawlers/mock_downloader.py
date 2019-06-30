from pathlib import Path

from assnatouverte.crawling.downloader.downloader import Downloader


class MockDownloader(Downloader):

    def __init__(self):
        self._pages = {}

    def register_page(self, url: str, filename: str):
        self._pages[url] = Path(__file__).parent / Path('pages') / Path(filename)

    def get_json(self, url: str) -> dict:
        pass

    def get_text(self, url: str) -> str:
        return self._pages[url].read_text(encoding='utf8')
