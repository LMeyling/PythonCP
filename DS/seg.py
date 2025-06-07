class iter_seg:
    def __init__(self, arr,e=0xFFFFFFFF,op=min):
        self.n = len(arr)
        self.bits = (self.n-1).bit_length() + 1
        self.max = 1 << self.bits
        self.e = e
        self.op = op
        self.arr = [self.e for _ in range(1<<self.bits)]
        self.ll = [0]
        base = 0
        le = 1 << self.bits
        for bit in range(self.bits):
            idx = 0
            for i in range(0,self.n,1<<bit):
                if bit:
                    self.arr[base + idx] = self.op(self.arr[base+2*idx-le],self.arr[base+2*idx-le+1])
                else:
                    self.arr[i] = arr[i]
                idx += 1
            le >>= 1
            base += le
            self.ll.append(base)
    def query(self,l,r):
        assert(l < r <= self.n)
        val = self.e
        while l < r:
            lsb = min(r & - r, r - l)
            x = lsb.bit_length() - 1
            rr = r - (1 << x)
            num = rr >> x
            val = self.op(self.arr[self.ll[x] + num],val)
            r = rr
        return val
    def upd(self,x,y):
        for i in range(self.bits):
            if i:
                self.arr[x+self.ll[i]] = self.op(self.arr[2*x+self.ll[i-1]],self.arr[2*x+self.ll[i-1]+1])
            else:
                self.arr[x] = y

            x >>= 1
    def min_right(self, start, comp):
        val = 1 << self.bits
        v = self.e
        cur = start
        san = start
        biggest = 0
        for bit in range(self.bits):
            if san + (1 << bit) >= self.max: break
            if cur % 2:
                nv = self.op(v, self.arr[cur + self.ll[bit]])
                if not comp(nv):
                    v = nv
                    cur += 1
                    san += 1 << bit
                else:
                    break
            biggest = bit + 1
            cur >>= 1
        smallest = self.n + 1
        if san >= smallest: return smallest
        for bit in range(biggest, -1,-1):
            if san + (1 << bit) >= self.max: continue
            nv = self.op(v, self.arr[cur + self.ll[bit]])
            if not comp(nv):
                san += 1 << bit
                v = nv
                cur += 1
            else:
                smallest = min(smallest,san + (1 << bit), self.n)
            cur <<= 1
        return smallest

    def max_left(self, start, comp):
        v = self.e
        cur = start
        san = start + 1
        biggest = 1
        pl = 0
        for bit in range(self.bits):
            if san - (1 << bit) < 0: break
            if 1 ^ (cur & 1):
                nv = self.op(v, self.arr[cur + self.ll[bit]])
                if not comp(nv):
                    v = nv
                    cur -= 1
                    san -= 1 << bit
                else:
                    pl = 1
                    break
            biggest = bit + 1
            cur >>= 1
        bigs = -1
        for bit in range(biggest, -1, -1):
            cur += 1 - pl
            pl = 0
            if san - (1 << bit) < 0: continue
            nv = self.op(v, self.arr[cur + self.ll[bit]])
            if not comp(nv):
                san -= 1 << bit
                v = nv
                cur -= 1
            else:
                bigs = max(bigs, san - (1 << bit), 0)
            cur <<= 1
        return bigs