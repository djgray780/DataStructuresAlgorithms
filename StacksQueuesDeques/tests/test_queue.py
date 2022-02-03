import pytest
from StacksQueuesDeques.Queue import QueueArray


@pytest.fixture
def queue():
    return QueueArray()


@pytest.fixture
def nequeue():
    return []


def test_nenque(nequeue):
    assert len(nequeue) == 5
