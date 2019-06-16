from unittest import TestCase
from unittest.mock import patch, create_autospec

import requests

from crawling.downloader.http_downloader import HttpDownloader


class TestCrawlerRepository(TestCase):

    def setUp(self):
        self.downloader = HttpDownloader()

        self.mock_response = create_autospec(requests.Response)
        patcher = patch('crawling.downloader.http_downloader.requests', autospec=True)
        self.mock_requests = patcher.start()
        self.addCleanup(patcher.stop)

    def test_get_text(self):
        expected_response_text = "test_value"
        self.mock_response.text = expected_response_text
        self.mock_requests.get.return_value = self.mock_response
        url = "http://www.assnat.qc.ca/fr/index.html"

        text = self.downloader.get_text(url)

        self.mock_requests.get.assert_called_once_with(url)
        self.assertEqual(text, expected_response_text)

    def test_get_text(self):
        expected_response_json = { "test": 41 }
        self.mock_response.json.return_value = expected_response_json
        self.mock_requests.get.return_value = self.mock_response
        url = "http://www.assnat.qc.ca/fr/index.html"

        json = self.downloader.get_json(url)

        self.mock_requests.get.assert_called_once_with(url)
        self.assertEqual(json, expected_response_json)
