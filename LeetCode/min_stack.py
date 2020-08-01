class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = []

    def push(self, x: int) -> None:
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.queue.append((x,curMin))
                

    def pop(self) -> None:
        self.queue.pop()

    def top(self) -> int:
        if self.queue:
            return self.queue[-1][0]

    def getMin(self) -> int:
        if self.queue:
            return self.queue[-1][1]
        return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
