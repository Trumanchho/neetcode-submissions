class MinStack:

    def __init__(self):
        self.stack = []
        self.current_min = None
        self.min_map = {}
        self.size = 0


    def push(self, val: int) -> None:
        if not len(self.stack):
            self.current_min  = val
        else:
            self.current_min = min(self.current_min, val)
        self.stack.append(val)
        self.size += 1
        self.min_map[self.size] = self.current_min
        
    def pop(self) -> None:
        del self.min_map[self.size]
        self.size -= 1
        if self.size:
            self.current_min = self.min_map[self.size]
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[self.size-1]

    def getMin(self) -> int:
        return self.current_min
        

"""
1 2 0

1: 1
2: 1
0: 0

1: 1
2: 1
2: 1

"""

