class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.elems = []
        for i in range(len(v)):
            self.elems += v[i]
        self.index = 0

    def next(self) -> int:
        if self.index < len(self.elems):
            self.index += 1
            return self.elems[self.index - 1]
        else:
            return None

    def hasNext(self) -> bool:
        return self.index < len(self.elems)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
