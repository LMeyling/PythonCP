class DSF:
    def __init__(self, n:int) -> None:
        self.par = [i for i in range(n)]
        self.siz =  [0]*n
    def root(self, x: int) -> int:
        while self.par[x] != x:
            self.par[x] = self.par[self.par[x]] 
            x = self.par[x]
        return x

    def union(self, x: int, y: int) -> bool:
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.siz[x] < self.siz[y]:
            x, y = y, x
        self.siz[x] += self.siz[y]
        self.par[y] = x
        return True
    def same(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)
    def size(self, x: int) -> int:
        return self.siz[self.root(x)]
