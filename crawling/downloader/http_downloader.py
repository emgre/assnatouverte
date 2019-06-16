import requests
from crawling.downloader.downloader import Downloader


class HttpDownloader(Downloader):
    def get_text(self, url: str) -> str:
        return requests.get(url).text

    def get_json(self, url: str) -> dict:
        return requests.get(url).json()
