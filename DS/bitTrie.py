# 2 per bit
class Trie:
    # n = number of expected elements
    # bits = number of max bits
    def __init__(self,n,bits=30):
        self.R = [-1] * (n * bits)
        self.R[0] = 2
        self.R[1] = 0
        self.idx = 6
        self.bits = bits
    def rev(self,at):
        if self.idx + 8 > len(self.R):
            self.R += [-1 for _ in range(100)]
        self.R[at] = self.idx
        self.idx += 4
        self.R[at+1] = 0
    def insert(self,word):
        bit = self.bits
        at = 0
        while bit >= 0:
            self.R[at+1] += 1
            if bit == 0:
                break
            if word.bit_length() >= bit:
                if self.R[self.R[at]+2] == -1:
                    self.rev(self.R[at]+2)
                word -= 1 << (bit - 1)
                at = self.R[at] + 2
            else:
                if self.R[self.R[at]] == -1:
                    self.rev(self.R[at])
                at = self.R[at]
            bit-=1

    def delete(self,word):
        bit = self.bits
        at = 0
        while bit >= 0:
            self.R[at+1] -= 1
            if bit == 0:break
            if word.bit_length() >= bit:
                at = self.R[at]+2
                word -= 1 << (bit - 1)
            else:
                at = self.R[at]
            bit -=1
    def search_max(self,word):
        bit = self.bits
        xox = 0
        at = 0
        while bit > 0:
            if word.bit_length() >= bit:
                if self.R[self.R[at]+3] > 0:
                    xox += 1 << (bit - 1)
                    at = self.R[at] + 2
                else:
                    at = self.R[at]
                word -= 1 << (bit - 1)
            else:
                if self.R[self.R[at]+1] > 0:
                    at = self.R[at]
                else:
                    at = self.R[at] + 2
                    xox += 1 << (bit - 1)
            bit-=1
        return xox

# 1 per bit, a little faster and twice as memory efficient
class Trie:
    # n = number of expected elements
    # bits = number of max bits
    def __init__(self,n,bits=30):
        self.R = [-1] * (n * bits + 10)
        self.R[0] = 2
        self.idx = 4
        self.bits = bits
    def rev(self,at,bit):
        if self.R[at] != -1:
            self.R[at] = abs(self.R[at]);return
        if self.idx + 8 > len(self.R):
            self.R += [-1 for _ in range(100)]
        if bit==1:
            self.R[at] = self.idx
            self.idx += 4
        elif bit:
            self.R[at] = self.idx
            self.idx += 2
        else:
            self.R[at] = 2
            self.R[at+1]=0
    def insert(self,word):
        bit = self.bits
        at = 0
        while bit >= 0:
            if bit == 0:
                self.R[at+1] += 1
                break
            if word.bit_length() >= bit:
                if self.R[self.R[at]+1+int(bit==1)] < 0:
                    self.rev(self.R[at]+1+int(bit==1),bit-1)
                word -= 1 << (bit - 1)
                at = self.R[at] + 1 + int(bit==1)
            else:
                if self.R[self.R[at]] < 0:
                    self.rev(self.R[at],bit-1)
                at = self.R[at]
            bit-=1

    def delete(self,word):
        bit = self.bits
        tword = word
        at = 0
        IDX=[]
        while bit >= 0:
            if bit == 0:self.R[at+1] -= 1;break
            if word.bit_length() >= bit:
                at = self.R[at]+1+int(bit==1)
                word -= 1 << (bit - 1)
            else:
                at = self.R[at]
            bit-=1;IDX.append(at)
        if self.R[at+1]==0:
            self.R[IDX[-1]] *= -1
            for i in range(len(IDX)-2,-1,-1):
                if self.R[self.R[IDX[i]]] < 0 and self.R[self.R[IDX[i]]+1+int(i==len(IDX)-2)] < 0:
                    self.R[IDX[i]] *= -1
                else:
                    break
    def search_max(self,word):
        bit = self.bits
        xox = 0
        at = 0
        while bit > 0:
            if word.bit_length() >= bit:
                if self.R[self.R[at]+1+int(bit==1)] > 0:
                    xox += 1 << (bit - 1)
                    at = self.R[at] + 1
                else:
                    at = self.R[at]
                word -= 1 << (bit - 1)
            else:
                if self.R[self.R[at]] > 0:
                    at = self.R[at]
                else:
                    at = self.R[at] + 1
                    xox += 1 << (bit - 1)
            bit-=1
        return xox