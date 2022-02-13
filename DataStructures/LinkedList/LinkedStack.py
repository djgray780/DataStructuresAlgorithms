# The SLL has a Node class that contains a reference to the data of the node, and also a pointer for the node.


class LinkedStack:
    class _Node:
        __slots__ = "_element", "_next"  # Memory preservation

        def __init__(self, element, next):
            self._element = element
            self._next = next

    """
    ## Methods
        # pop(), remove and return the first element of the LIFO stack
        # peek(), return, but do not remove, the first element of the stack
            # For both pop(), and peek(), raise an empty error if empty.
        # is_empty() will return True if the stack is empty
        # len() funciton to tell us how long our Linked Stack is.
        # push(), add element to the top of the stack
        # __repr__ method would be nice, but not necessary here, we'll add it though at the end for fun.
    """

    def __init__(self):
        self._head_ref = None
        self._size: int = 0

    def __len__(self):
        return self._size

    def pop(self):
        if self._size == 0:
            raise Exception("LinkedStack is empty")
        stored_element = self._head_ref._element
        self._head_ref = self._head_ref._next
        self._size -= 1
        return stored_element

    def push(self, e):
        # Create the new node first
        new_node = self._Node(e, self._head_ref)
        self._head_ref = new_node
        self._size += 1

    def peek(self):
        if self._size == 0:
            raise Exception("LinkedStack is empty")
        return self._head_ref._element  # Accessing the nodes element.

    def is_empty(self) -> bool:
        return self._size == 0
