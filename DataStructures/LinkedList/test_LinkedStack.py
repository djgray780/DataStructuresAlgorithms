import pytest

from LinkedStack import LinkedStack


# class TestLinkedStack
@pytest.fixture
def stack():
    return LinkedStack()


@pytest.fixture
def three_element_stack(stack):
    for i in range(3):
        stack.push(i)
    return stack


def test_empty_LS():
    linked_stack = LinkedStack()
    assert linked_stack._head_ref == None
    assert linked_stack._size == 0


class TestPush:
    def test_push_size(self, stack):
        # TODO Not sure how to test the stack._head_ref attribute
        stack.push(1)
        assert stack._size == 1

    def test_push_head(self, stack):
        stack.push(1)
        stack._head_ref != None
        stack._head_ref == LinkedStack._Node(1, stack._head_ref)  # This feels gross.


class TestPeek:
    def test_peek_on_empty_stack(self, stack):
        with pytest.raises(Exception) as e_info:
            stack.peek()

    def test_peek_on_nonempty_stack(self, three_element_stack):
        assert three_element_stack.peek() == 2


class TestEmptyCheck:
    def test_is_empty_on_empty_stack(self, stack):
        assert stack.is_empty() == True

    def test_is_empty_on_nonempty_stack(self, three_element_stack):
        assert three_element_stack.is_empty() == False


# class TestPop:
class TestPop:
    def test_pop_on_empty_stack(self, stack):
        with pytest.raises(Exception) as e_info:
            stack.pop()

    def test_pop_on_non_empty_stack(self, three_element_stack):
        assert three_element_stack.pop() == 2
