class MyHashMap:

    def __init__(self):
        self.key_space = 2069
        self.hash_table = [Bucket() for _ in range(self.key_space)]

    def put(self, key, val):
        hash_key = key % self.key_space
        self.hash_table[hash_key].update(key, val)

    def get(self, key):
        hash_key = key % self.key_space
        return self.hash_table[hash_key].get(key)

    def remove(self, key):
        hash_key = key % self.key_space
        return self.hash_table[hash_key].remove(key)


class Bucket:

    def __init__(self):
        self.bucket = []

    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v

        return -1

    def update(self, key, value):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                return

        self.bucket.append((key, value))

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]
                return