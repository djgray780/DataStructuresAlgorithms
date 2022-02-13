
## Initial Thoughts

- Inputs that are given initially are symmetrical, but other inputs may not be. 
- We might also want to consider an edge case in which the input string is the empty string
- At first a `Dequeue` seemed like a natural choice because the provided inputs were symmetrical. If the inputs were restricted to being symmetrical then we would only need to pop the left and right elements of the dequeue and do a membership check in a matching pair of brackets. After some thought, the `Dequeue` did not seem like the best tool for the job here. 


## Solution
This is what the initial `solution.py` file should look like.

```python
import pytest

##########################################################################
### SOLUTION
##########################################################################
def isBalanced(input: str) -> str:
	pass

##########################################################################
### TEST CASES
##########################################################################

##########################################################################
if __name__ == "__main__":
	raise SystemExit(pytest.main([__file__])
```

Before getting into the actual solution, I think it's a helpful practice to think of different test cases and try to build up from there. This approach to writing code is called [Test Driven Development](https://en.wikipedia.org/wiki/Test-driven_development).  Let's think of a few test cases that we can come up with on our own, and then when we input our solution into HackerRank we'll probably get many more that we might not have considered. In the code below, I have included the first four on my own, the last three are sample inputs. If we run these on our `isBalanced()` function, we should *expect* them all to fail, but now we can build our code around these test cases. 

```python
##########################################################################
### TEST CASES
##########################################################################
@pytest.mark.parametrize
("input_brackets", "output"),
	(
		("", "NO"),
		("[]", "YES"),
		("()", "YES"),
		("{}", "YES"),
		("{[(]}", "NO"),
		("{[()]}", "YES"),
		("{[(])}", "NO"),
		("{{[[(())]]}}", "YES")
	),
)
def test_isBalanced(input_brackets, output):
	assert  isBalanced(input_brackets) ==  output
```
Given that this problem is in the "Stacks and Queues" area the obvious guess for a solution should be to use a `Stack`, `Queue`, or `Dequeue` data structure. My initial approach was to utilize a `Dequeue` because I assumed the inputs would always be symmetrical, but this is not necessarily the case when we interrogate the sample inputs. Thinking back to the implementation of a [Queue using two Stacks](https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem?h_r=profile), the `Stack` seemed like a better choice.  

The idea behind the solution is as follows. Our function should only return "YES" when a sequence of brackets *contains no unmatched brackets* and *the subset of brackets within a pair of matched brackets is also a matched pair*. The most atomic unit we can expect to see within even the most complicated sequence of brackets must be one of three pairs: `(), [], {}`. This means that we can utilize the properties of a `Stack` to help determine if a pair of brackets is atomic, and thus, matching. 

```python
from typing import Dict, List, Union

def isBalanced(input: str) -> str:
    left_right_pairs: Dict[str, str] = {"(": ")", "[": "]", "{": "}"}
    left_brackets = left_right_pairs.keys()
    stack: List[Union[None, str]] = []

	for bracket in input:
		if len(stack) == 0:	# Empty stack
			stack.append(bracket)
		elif bracket in left_brackets:
			stack.append(bracket)
		elif bracket not in left_brackets:
			try:
				if left_right_pairs[stack[-1]] == bracket:
					stack.pop()
				else:
					stack.append(bracket)
			except KeyError:	# Trying to access an undefined key
				stack.append(bracket)
			
	if (input == "") or (len(stack) != 0):
		return "NO"
	else:
		return "YES"
```