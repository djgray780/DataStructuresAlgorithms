class Empty(Exception):
    """Error when trying to access element from an empty container"""

    pass


class StackArray:
    # Constructor
    def __init__(self):
        """Define the empty container"""
        self._container = []

    # Return length of the stack
    def __len__(self):
        """Return length of the Stack"""
        return len(self._container)

    # Push onto the stack
    def push(self, e):
        """Add element to top of the stack"""
        self._container.append(e)

    # Pop off of the stack
    def pop(self):
        """Remove top element from the stack"""
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._container.pop()

    # Peak at the top of the stack
    def peak(self):
        # if self.is_empty():
        #     raise Empty("Stack is empty")
        return self._container[-1]

    # Check if stack is empty
    def is_empty(self):
        """Returns True if empty, False otherwise"""
        return len(self._container) == 0
