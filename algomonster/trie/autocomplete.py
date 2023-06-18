class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.num_children = 0
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
            cur.num_children += 1
        cur.end = True


def autocomplete(words):
    count = 0
    trie = Trie()
    for word in words:
        trie.insert(word)
        cur = trie.root
        for char in word:
            count += 1
            char_idx = ord(char) - ord('a')
            if cur.children[char_idx].num_children == 1:
                break
            cur = cur.children[char_idx]
    return count
