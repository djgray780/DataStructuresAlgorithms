class MyQueue(object):
    def __init__(self):
        self.s1 = []  # Use for Enqueue
        self.s2 = []  # Use for Dequeue

    def __len__(self):
        return len(self.s1) + len(self.s2)

    def is_empty(self):
        return len(self.s1) + len(self.s2) == 0

    def put(self, value):
        self.s1.append(value)

    def pop(self):
        if len(self.s2) == 0:
            while len(self.s1) != 0:
                self.s2.append(self.s1.pop())
        self.s2.pop()

    def peek(self):
        if len(self.s2) == 0:
            while len(self.s1) != 0:
                self.s2.append(self.s1.pop())
        return self.s2[-1]
