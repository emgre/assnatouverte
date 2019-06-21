import inspect
import importlib.util
from pathlib import Path
import pkgutil
from typing import List

from assnatouverte.crawling.crawler import Crawler


class CrawlerNotFoundException(Exception):
    pass


class CrawlerWithSameIdAlreadyExistsException(Exception):
    pass


class CrawlerRepository:

    def __init__(self):
        self._crawlers = {}

    def add_crawler(self, crawler: Crawler) -> None:
        if crawler.get_name() in self._crawlers:
            raise CrawlerWithSameIdAlreadyExistsException

        self._crawlers[crawler.get_name()] = crawler

    def get_crawler(self, crawler_name: str) -> Crawler:
        crawler = self._crawlers.get(crawler_name)
        if not crawler:
            raise CrawlerNotFoundException

        return crawler

    def get_all_crawlers(self) -> List[Crawler]:
        return list(self._crawlers.values())

    def discover_crawlers(self, path: Path = Path(__file__).parent / 'crawlers') -> None:
        for loader, module_name, is_pkg in pkgutil.walk_packages([path.as_posix()]):
            if not is_pkg:
                spec = loader.find_spec(module_name)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                for _, obj in inspect.getmembers(module, inspect.isclass):
                    if obj.__module__ == module_name and issubclass(obj, Crawler):
                        self.add_crawler(obj())
