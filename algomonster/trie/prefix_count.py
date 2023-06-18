class TrieNode():
    def __init__(self):
        self.children = [None] * 26
        self.num_children = 0
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        cur.num_children += 1
        for char in word:
            char_idx = ord(char) - ord('a')
            if not cur.children[char_idx]:
                cur.children[char_idx] = TrieNode()
            cur = cur.children[char_idx]
            cur.num_children += 1
        cur.end = True

    def get_prefix_count(self, prefix):
        cur = self.root
        for char in prefix:
            char_idx = ord(char) - ord('a')
            if not cur.children[char_idx]:
                return 0
            cur = cur.children[char_idx]
        return cur.num_children


def prefix_count(words, prefixes):
    trie = Trie()
    for word in words:
        trie.insert(word)
    return [trie.get_prefix_count(prefix) for prefix in prefixes]
