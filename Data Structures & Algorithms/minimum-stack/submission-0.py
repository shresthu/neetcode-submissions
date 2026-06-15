class MinStack:

    def __init__(self):
        self.stack = []
        self.m = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.m[-1] if self.m else val)
        self.m.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.m.pop()
        else:
            return null

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return null
    def getMin(self) -> int:
        if self.m:
            return self.m[-1]
        else:
            return null