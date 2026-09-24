class Codec:

    def __init__(self):
        self.url_map = {}
        self.counter = 0

    def encode(self, longUrl: str) -> str:
        self.counter += 1

        shortUrl = str(self.counter)
        self.url_map[shortUrl] = longUrl

        return shortUrl

    def decode(self, shortUrl: str) -> str:
        return self.url_map[shortUrl]
