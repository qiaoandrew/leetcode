def restore_ip_addresses(s):
    res = []
    cur = []

    def dfs(start):
        if start == len(s):
            if len(cur) == 4:
                res.append('.'.join(cur))
            return

        for end in range(start, min(len(s), start + 3)):
            part = s[start:end + 1]

            if int(part) <= 255 and not (len(part) > 1 and part[0] == '0'):
                cur.append(part)
                dfs(end + 1)
                cur.pop()

    dfs(0)

    return res


print(restore_ip_addresses('25525511135'))
print(restore_ip_addresses('0000'))
print(restore_ip_addresses('101023'))