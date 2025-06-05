class iter_seg:
    def __init__(self, arr,e=0xFFFFFFFF,op=min):
        self.n = len(arr)
        self.bits = (self.n-1).bit_length() + 1
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