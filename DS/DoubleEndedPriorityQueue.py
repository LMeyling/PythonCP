import sys
from heapq import heappush, heappop


class DoubleEndedPriorityQueue:
    def __init__(self, arr: List[int] = None) -> None:
        self.hq1 = []
        self.hq2 = []
        if arr:
            self.used = bytearray(len(S))
            self.idx = len(S)
            for i, x in enumerate(S):
                tmp = x << 20 | i
                heappush(self.hq1, tmp)
                heappush(self.hq2, ~tmp)
        else:
            self.used = bytearray()
            self.idx = 0

    def pop_min(self) -> int:
        while 1:
            tmp = heappop(self.hq1)
            x, i = tmp >> 20, tmp & 0xfffff
            if self.used[i]: continue
            self.used[i] = 1
            return x

    def pop_max(self) -> int:
        while 1:
            tmp = heappop(self.hq2)
            tmp = ~tmp
            x, i = tmp >> 20, tmp & 0xfffff
            if self.used[i]: continue
            self.used[i] = 1
            return x

    def push(self, x: int) -> None:
        tmp = x << 20 | self.idx
        heappush(self.hq1, tmp)
        heappush(self.hq2, ~tmp)
        self.used.append(0)
        self.idx += 1