class Codec:

    def encode(self, strs):
        res = []

        for string in strs:
            res.append(str(len(string)))
            res.append('#')
            res.append(string)

        return ''.join(res)

    # Find length of current string using start and end indices
    # Get the current string using previous end index and length
    # Move start index forwards
    def decode(self, s):
        res = []

        start = 0

        while start < len(s):
            end = start

            while s[end] != '#':
                end += 1

            length = int(s[start:end])
            string = s[end + 1:end + 1 + length]

            res.append(string)

            start = end + 1 + length

        return res


codec = Codec()
print(codec.decode(codec.encode(["Hello", "World"])))
