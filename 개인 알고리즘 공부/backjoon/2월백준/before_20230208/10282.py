class Stack:
    def __init__(self, numb):
        self.stack = []
        self.numb = numb

    def push(self):
        self.stack.append(self.numb)

    def top(self):
        if len(self.stack) != 0:
            return self.stack[-1]
        else:
            return -1

    def pop(self):
        if len(self.stack) == 0:
            return -1
        else:
            return self.stack.pop()

    def size(self):
        return len(self.stack)

    def empty(self):
        if len(self.stack) == 0:
            return 1
        else:
            return 0



