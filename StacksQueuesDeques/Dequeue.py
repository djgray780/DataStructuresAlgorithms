from typing import Generic, List, TypeVar, Union

# See https://mypy.readthedocs.io/en/stable/generics.html for how to implement TypeVar and Generic
# on self._storage for better typing.
# TODO: Add array downsizing for element removal methods.


class Empty:
    pass


class Dequeue:

    DEFAULT_CAPACITY: int = 10

    def __init__(self) -> None:
        """Dequeue ADT maintains three instance variables"""
        self._storage: List[Union[None, int]] = [None] * Dequeue.DEFAULT_CAPACITY
        self._head_idx: int = 0
        self._tail_idx: Union[None, int] = None
        self._num_elements: int = 0

    def __len__(self) -> int:
        return self._num_elements

    def add_to_front(self, object) -> None:
        if self._dequeue_is_full():
            self._resize_storage(2 * len(self._storage))
        self._head_idx = self._decrement_head_idx()
        self._storage[self._head_idx] = object
        self._num_elements += 1

    def add_to_back(self, object) -> None:
        if self._dequeue_is_full():
            self._resize_storage(2 * len(self._storage))
        self._tail_idx = self._update_tail_idx()
        self._storage[self._tail_idx] = object
        self._num_elements += 1

    def remove_from_front(self):
        to_remove = self._storage[self._head_idx]
        self._storage[self._head_idx] = None
        self._head_idx = self._increment_head_idx()
        self._num_elements -= 1
        return to_remove

    def is_empty(self):
        return self._num_elements == 0

    # Utility Methods:
    def _resize_storage(self, new_capacity):
        return

    def _decrement_head_idx(self) -> int:
        return (self._head_idx - 1) % len(self._storage)

    def _increment_head_idx(self) -> int:
        return (self._head_idx + 1) % len(self._storage)

    def _update_tail_idx(self) -> int:
        return (self._head_idx + self._num_elements) % len(self._storage)

    def _dequeue_is_full(self) -> bool:
        return self._num_elements == len(self._storage)
