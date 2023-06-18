class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for char in word:
            char_idx = ord(char) - ord('a')
            if not cur.children[char_idx]:
                cur.children[char_idx] = TrieNode()
            cur = cur.children[char_idx]
        cur.end = True

    def search(self, word):
        cur = self.root
        for char in word:
            char_idx = ord(char) - ord('a')
            if not cur.children[char_idx]:
                return False
            cur = cur.children[char_idx]
        return cur.end

    def starts_with(self, prefix):
        cur = self.root
        for char in prefix:
            char_idx = ord(char) - ord('a')
            if not cur.children[char_idx]:
                return False
            cur = cur.children[char_idx]
        return True
