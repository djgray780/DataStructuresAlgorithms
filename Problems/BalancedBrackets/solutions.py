from typing import Dict, KeysView, List, Optional, Set, Tuple, Union

import pytest

# TODO: Add typing to solutions.

##########################################################################
# SOLUTIONS
##########################################################################


def isBalanced(input: str) -> str:
    left_right_pairs: Dict[str, str] = {"(": ")", "[": "]", "{": "}"}
    left_brackets: KeysView = left_right_pairs.keys()
    stack: List[str] = []

    for bracket in input:
        if len(stack) == 0:  # Empty
            stack.append(bracket)
        elif bracket in left_brackets:
            stack.append(bracket)
        elif bracket not in left_brackets:
            try:
                if left_right_pairs[stack[-1]] == bracket:
                    stack.pop()
                else:
                    stack.append(bracket)
            except KeyError:
                stack.append(bracket)

    if (input == "") or len(stack) != 0:
        return "NO"
    else:
        return "YES"


def isBalanced2(input: str) -> str:
    left_brackets: str = "([{"
    right_brackets: str = ")]}"
    matching_pairs: Set[Tuple[str, str]] = {("(", ")"), ("[", "]"), ("{", "}")}
    stack: List[str] = []

    for bracket in input:
        if len(stack) == 0:
            stack.append(bracket)
        elif bracket in left_brackets:
            stack.append(bracket)
        elif bracket in right_brackets:
            if (stack[-1], bracket) in matching_pairs:
                stack.pop()
            else:
                stack.append(bracket)

    if (input == "") or len(stack) != 0:
        return "NO"
    else:
        return "YES"


def isBalanced3(input: str) -> str:
    left_brackets: str = "([{"
    right_brackets: str = ")]}"
    stack: List[str] = []

    if input == "" or len(input) == 1:  # Handle edge cases
        return "NO"
    else:
        for bracket in input:
            if bracket in left_brackets:
                stack.append(bracket)
            elif bracket in right_brackets:
                if len(stack) == 0:
                    return "NO"  # Cannot have the first element be a closing bracket.
                if left_brackets.index(stack.pop()) != right_brackets.index(bracket):
                    return "NO"  # Brackets aren't matching, done.

    if len(stack) == 0:
        return "YES"
    else:
        return "NO"


##########################################################################
### TEST CASES
##########################################################################


@pytest.mark.parametrize(
    ("input_brackets", "output"),
    (
        ("", "NO"),
        ("[", "NO"),
        ("]", "NO"),
        ("[]", "YES"),
        ("()", "YES"),
        ("{}", "YES"),
        ("{[(]}", "NO"),
        ("{[()]}", "YES"),
        ("{[(])}", "NO"),
        ("{(([])[])[]}", "YES"),
        ("{(([])[])[]]}", "NO"),
        ("{(([])[])[]}[]", "YES"),
        ("{(([])[])[]}", "YES"),
        ("{{[[(())]]}}", "YES"),
    ),
)
def test_isBalanced(input_brackets, output):
    assert isBalanced(input_brackets) == output


@pytest.mark.parametrize(
    ("input_brackets", "output"),
    (
        ("", "NO"),
        ("[", "NO"),
        ("]", "NO"),
        ("[]", "YES"),
        ("()", "YES"),
        ("{}", "YES"),
        ("{[(]}", "NO"),
        ("{[()]}", "YES"),
        ("{[(])}", "NO"),
        ("{(([])[])[]}", "YES"),
        ("{(([])[])[]]}", "NO"),
        ("{(([])[])[]}[]", "YES"),
        ("{(([])[])[]}", "YES"),
        ("{{[[(())]]}}", "YES"),
    ),
)
def test_isBalanced2(input_brackets, output):
    assert isBalanced2(input_brackets) == output


@pytest.mark.parametrize(
    ("input_brackets", "output"),
    (
        ("", "NO"),
        ("[", "NO"),
        ("]", "NO"),
        ("[]", "YES"),
        ("()", "YES"),
        ("{}", "YES"),
        ("{[(]}", "NO"),
        ("{[()]}", "YES"),
        ("{[(])}", "NO"),
        ("{(([])[])[]}", "YES"),
        ("{(([])[])[]]}", "NO"),
        ("{(([])[])[]}[]", "YES"),
        ("{(([])[])[]}", "YES"),
        ("{{[[(())]]}}", "YES"),
    ),
)
def test_isBalanced3(input_brackets, output):
    assert isBalanced3(input_brackets) == output


##########################################################################

if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))
