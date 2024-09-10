ULL_MAX = 0xFFFFFFFFFFFFFFFF

class H:
    def __init__(self, x=0):
        self.x = x & ULL_MAX

    def __add__(self, other):
        res = (self.x + other.x) & ULL_MAX
        carry = 1 if res < self.x else 0
        return H((res + carry) & ULL_MAX)

    def __sub__(self, other):
        return self + H(~other.x & ULL_MAX)

    def __mul__(self, other):
        m = (self.x * other.x) & ((1 << 128) - 1)
        return H(m & ULL_MAX) + H((m >> 64) & ULL_MAX)

    def get(self):
        return (self.x + (not ~self.x & ULL_MAX)) & ULL_MAX

    def __eq__(self, other):
        return self.get() == other.get()

    def __lt__(self, other):
        return self.get() < other.get()


C = H(int(1e11) + 3)

class HashInterval:
    def __init__(self, s):
        n = len(s)
        self.ha = [H()] * (n + 1)
        self.pw = [H()] * (n + 1)
        self.pw[0] = H(1)
        for i in range(n):
            self.ha[i + 1] = self.ha[i] * C + H(ord(s[i]))
            self.pw[i + 1] = self.pw[i] * C

    def hash_interval(self, a, b):
        return self.ha[b] - self.ha[a] * self.pw[b - a]

def get_hashes(s, length):
    n = len(s)
    if n < length:
        return []
    h = H(0)
    pw = H(1)
    for i in range(length):
        h = h * C + H(ord(s[i]))
        pw = pw * C
    ret = [h]
    for i in range(length, n):
        h = h * C + H(ord(s[i])) - pw * H(ord(s[i - length]))
        ret.append(h)
    return ret

def hash_string(s):
    h = H()
    for c in s:
        h = h * C + H(ord(c))
    return h