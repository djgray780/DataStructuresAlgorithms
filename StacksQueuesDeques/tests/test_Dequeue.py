import pytest
from StacksQueuesDeques.Dequeue import Dequeue


@pytest.fixture
def empty_Dequeue():
    return Dequeue()


@pytest.fixture
def almost_full_Dequeue(empty_Dequeue):
    for i in range(empty_Dequeue.DEFAULT_CAPACITY - 1):
        empty_Dequeue.add_to_front(i + 1)
    return empty_Dequeue


class TestInstantiatedValues:
    def test_default_capacity(self, empty_Dequeue):
        assert empty_Dequeue.DEFAULT_CAPACITY == 10

    def test_initial_instantiated_storage(self, empty_Dequeue):
        assert empty_Dequeue._storage == [None] * 10

    def test_initial_instantiated_head_idx(self, empty_Dequeue):
        assert empty_Dequeue._head_idx == 0

    def test_initial_instantiated_num_elements(self, empty_Dequeue):
        assert empty_Dequeue._num_elements == 0


def test_almost_full_Dequeue(almost_full_Dequeue):
    assert almost_full_Dequeue._num_elements == 9
    assert almost_full_Dequeue._num_elements < len(almost_full_Dequeue._storage)


# class TestAdding:


class TestAddingVals:
    def test_add_to_front(self, empty_Dequeue):
        empty_Dequeue.add_to_front(1)
        assert empty_Dequeue._num_elements != 0
        assert empty_Dequeue._head_idx == 9  # Modular Arithmetic: -1 % 10 = 9
        assert empty_Dequeue._num_elements == 1

    def test_add_to_back(self, empty_Dequeue):
        empty_Dequeue.add_to_back(1)
        assert empty_Dequeue._num_elements != 0
        assert empty_Dequeue._tail_idx == 0
        assert empty_Dequeue._num_elements == 1

    def test_add_last_element_from_front(self, almost_full_Dequeue):
        almost_full_Dequeue.add_to_front(9)
        assert almost_full_Dequeue._num_elements != 0
        assert almost_full_Dequeue._num_elements == 10
        assert almost_full_Dequeue._head_idx == 0


# class TestRemoving:


def test_remove_from_front(almost_full_Dequeue):
    almost_full_Dequeue.add_to_front(9)
    assert almost_full_Dequeue._num_elements == almost_full_Dequeue.DEFAULT_CAPACITY
    assert almost_full_Dequeue.remove_from_front() == 9
    assert almost_full_Dequeue._num_elements == 9


# class TestUtilities:


def test_is_empty(empty_Dequeue):
    assert empty_Dequeue.is_empty() == True


# class TestPeeks:
