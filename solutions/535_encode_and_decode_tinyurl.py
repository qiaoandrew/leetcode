class Codec:

    def __init__(self):
        self.encode_map = {}
        self.decode_map = {}

    def encode(self, long_url):
        if long_url not in self.encode_map:
            encoded = 'http://tinyurl.com/' + str(len(self.encode_map))
            self.encode_map[long_url] = encoded
            self.decode_map[encoded] = long_url

        return self.encode_map[long_url]

    def decode(self, short_url):
        return self.decode_map[short_url]


codec = Codec()
print(
    codec.decode(codec.encode('https://leetcode.com/problems/design-tinyurl')))
