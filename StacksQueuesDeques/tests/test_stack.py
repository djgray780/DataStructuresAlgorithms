import pytest
from StacksQueuesDeques.Stack import Empty, StackArray

# Assertions about expected exceptions: https://docs.pytest.org/en/6.2.x/assert.html
# pytest.raises(): [anthonywritescode #176](https://www.youtube.com/watch?v=6nRxZyQwwlE)

# DS have states (elements inside structure), tests need to run in any particular order.  
# Share the state of the data structures throughout the tests for more robust testing.
# The Stack is not expensive, so this approach is okay for now. But if some object (e.g., psycopg2 drivers, db conns) is expensive then sharing is more efficient.

@pytest.fixture
def stack():
    return StackArray()


def test_push(stack):
    stack.push(1)
    assert len(stack) == 1
    stack.push(2)
    assert len(stack) == 2


def test_is_empty(stack):
    assert stack.is_empty() == True


def test_pop(stack):
    stack.push(1)
    assert len(stack) == 1
    stack.pop()
    assert len(stack) == 0


def test_pop_is_empty(stack):  # ref: anthonywritescode #176
    with pytest.raises(Empty) as execinfo:
        stack.pop()
    (msg,) = execinfo.value.args
    assert msg == "Stack is empty"
    # assert pytest.raises(Empty, stack.pop, category_id)


def test_peak(stack):
    stack.push(1)
    stack.push(2)
    assert stack.peak() == 2


