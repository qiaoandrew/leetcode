def is_isomorphic(s, t):
    s_to_t = {}
    t_to_s = {}

    for i in range(len(s)):
        cur_s = s[i]
        cur_t = t[i]

        if cur_s in s_to_t and cur_t != s_to_t[cur_s]:
            return False

        if cur_t in t_to_s and cur_s != t_to_s[cur_t]:
            return False

        s_to_t[cur_s] = cur_t
        t_to_s[cur_t] = cur_s

    return True


print(is_isomorphic('egg', 'add'))
print(is_isomorphic('foo', 'bar'))
print(is_isomorphic('paper', 'title'))