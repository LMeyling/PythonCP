def op(a,b):
    return (min(a,b),)
class iter_seg:
    def __init__(self, arr,e=(0xFFFFFFFF,),op=min):
        sz = len(e)
        self.n = len(arr) // sz
        self.bits = (self.n-1).bit_length() + 1
        self.e = e
        self.op = op
        self.arr = [i for i in e for _ in range(1<<self.bits)]
        self.ll = [0]
        base = 0
        le = 1 << self.bits
        for bit in range(self.bits):
            idx = 0
            for i in range(0,self.n,1<<bit):
                if bit:
                    self.arr[(base + idx)*sz:(base + idx+1)*sz] = self.op(*self.arr[sz*(base+2*idx-le):sz*(base+2*idx-le+1)],*self.arr[sz*(base+2*idx-le+1):sz*(base+2*idx-le+2)])
                else:
                    self.arr[sz*i:sz*i+sz] = arr[i*sz:(i+1)*sz]
                idx += 1
            le >>= 1
            base += le
            self.ll.append(base)
        self.sz = sz
    def query(self,l,r):
        assert(l < r <= self.n)
        val = self.e
        while l < r:
            lsb = min(r & - r, r - l)
            x = lsb.bit_length() - 1
            rr = r - (1 << x)
            num = rr >> x
            val = self.op(*self.arr[(self.ll[x] + num)*self.sz:(self.ll[x] + num+1)*self.sz],*val)
            r = rr
        return val
    def upd(self,x,y):
        for i in range(self.bits):
            if i:
                self.arr[(x+self.ll[i])*self.sz:(x+self.ll[i]+1)*self.sz] = self.op(*self.arr[(2*x+self.ll[i-1])*self.sz:(2*x+self.ll[i-1]+1)*self.sz],*self.arr[(2*x+self.ll[i-1]+1)*self.sz:(2*x+self.ll[i-1]+2)*self.sz])
            else:
                self.arr[x*self.sz:self.sz*x+self.sz] = y
            x >>= 1