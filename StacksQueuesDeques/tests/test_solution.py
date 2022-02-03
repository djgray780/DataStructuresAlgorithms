import pytest
from StacksQueuesDeques.Problems.TwoStackQueue.solution import MyQueue


@pytest.fixture()
def queue():
    return MyQueue().s1


@pytest.fixture()
def e_queue():
    return MyQueue()


@pytest.fixture()
def d_queue():
    return MyQueue()


def test_queue_primitives(queue):
    queue.put(1)
    assert len(queue) == 1
    queue.put(2)
    assert len(queue) == 2
    assert queue.peek() == 2
    queue.pop()
    queue.pop()
    assert len(queue) == 0
