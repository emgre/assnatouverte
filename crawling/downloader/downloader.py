class Downloader:
    def get_text(self, url: str) -> str:
        raise NotImplementedError

    def get_json(self, url: str) -> dict:
        raise NotImplementedError
