class MyQueue:

    def __init__(self):
        self.tmp_s = []
        self.reversed_s = [] # this will act as the queue

    def push(self, x: int) -> None:
        while len(self.reversed_s):
            self.tmp_s.append(self.reversed_s.pop())
        self.tmp_s.append(x)
        while len(self.tmp_s):
            self.reversed_s.append(self.tmp_s.pop())


    def pop(self) -> int:
        return self.reversed_s.pop()

    def peek(self) -> int:
        return self.reversed_s[-1]

    def empty(self) -> bool:
        return len(self.reversed_s) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


