import pytest
from StacksQueuesDeques.Dequeue import Dequeue

# TODO: Test peek elements
# TODO: Test resizing method

@pytest.fixture
def empty_Dequeue():
    return Dequeue()


@pytest.fixture
def almost_full_Dequeue(empty_Dequeue):
    for i in range(empty_Dequeue.DEFAULT_CAPACITY - 1):
        empty_Dequeue.add_to_front(i + 1)
    return empty_Dequeue  # [None, 8, 7, 6, ... , 0]


@pytest.fixture
def two_on_each_end_Dequeue(empty_Dequeue):
    empty_Dequeue.add_to_front(1)
    empty_Dequeue.add_to_front(2)
    empty_Dequeue.add_to_back(3)
    empty_Dequeue.add_to_back(4)
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

class TestRemoving:
    def test_remove_from_front(self, almost_full_Dequeue):
        almost_full_Dequeue.add_to_front(9)
        assert almost_full_Dequeue._num_elements == almost_full_Dequeue.DEFAULT_CAPACITY
        assert almost_full_Dequeue.remove_from_front() == 9
        assert almost_full_Dequeue._num_elements == 9


    def test_remove_from_back(self, almost_full_Dequeue):
        almost_full_Dequeue.add_to_back(9)
        assert almost_full_Dequeue._num_elements == almost_full_Dequeue.DEFAULT_CAPACITY
        removed_element = almost_full_Dequeue.remove_from_back()
        assert removed_element == 9

    def test_remove_from_back_2(self, two_on_each_end_Dequeue):
        dequeue = two_on_each_end_Dequeue
        dequeue.remove_from_back()
        assert dequeue._num_elements == 3

# class TestUtilities:

class TestUtilities:
    def test_is_empty(self, empty_Dequeue):
        assert empty_Dequeue.is_empty() == True

    def test_dequeue_is_full(self, almost_full_Dequeue):
        almost_full_Dequeue.add_to_front(99)
        assert almost_full_Dequeue._num_elements == almost_full_Dequeue.DEFAULT_CAPACITY


    def test_decrement_head(self, almost_full_Dequeue):
        assert almost_full_Dequeue._head_idx == 1
        updated_head_idx = almost_full_Dequeue._decrement_head_idx()
        assert updated_head_idx == 0


    def test_increment_head(self, almost_full_Dequeue):
        assert almost_full_Dequeue._head_idx == 1
        updated_head_idx = almost_full_Dequeue._increment_head_idx()
        assert updated_head_idx == 2


    def test_increment_tail(self, two_on_each_end_Dequeue):
        dequeue = two_on_each_end_Dequeue
        assert dequeue._tail_idx == 1
        assert dequeue._head_idx == 8
        new_idx = dequeue._increment_tail_idx()
        assert new_idx == 2


    def test_decrement_tail(self, two_on_each_end_Dequeue):
        dequeue = two_on_each_end_Dequeue
        assert dequeue._tail_idx == 1
        dequeue._storage[1] = None
        dequeue._num_elements -= 1
        assert dequeue._num_elements == 3
        new_idx = dequeue._decrement_tail_idx()
        assert new_idx == 0


# class TestPeeks:
def test_peek_first():
    assert False

def test_peek_last():
    assert False