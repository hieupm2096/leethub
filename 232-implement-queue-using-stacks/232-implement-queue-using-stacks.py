class MyQueue:

    def __init__(self):
        self.read = []
        self.write = []

    def push(self, x: int) -> None:
        if len(self.read) == 0:
            self.read.append(x)
        else:
            while len(self.read) != 0:
                self.write.append(self.read.pop())
            self.read.append(x)
            while len(self.write) != 0:
                self.read.append(self.write.pop())
            

    def pop(self) -> int:
        return self.read.pop()
        

    def peek(self) -> int:
        return self.read[-1]
        

    def empty(self) -> bool:
        return len(self.read) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()