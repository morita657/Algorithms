class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mapSum = collections.defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        for k in self.mapSum.keys():
            if k==key:
                self.mapSum[key]=val
        self.mapSum[key]=val

    def sum(self, prefix: str) -> int:
        total=0
        for key in self.mapSum.keys():
            if key.startswith(prefix):
                total+=self.mapSum[key]
        return total

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

