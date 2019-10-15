class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.window = []
        self.size = size

    def next(self, val: int) -> float:
        if len(self.window) < self.size:
            self.window.append(val)
            return sum(self.window) / len(self.window)
        else:
            self.window.pop(0)
            self.window.append(val)
            return sum(self.window) / len(self.window)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
