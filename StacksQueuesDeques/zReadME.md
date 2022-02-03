## Stacks, Queues, and Deques

Note: The Jupyter files are where I like to experiment with small code fragments, methods, or ideas. These files will typically look identical to the .py files, but may be slightly different. 

- Stacks can be implemented by utilizing Python `Lists` and the *Adapter Pattern*. The Adapter Pattern applies to any context in which we modify the methods of an existing class to mirror the functinoality of a different data structure.
- 
- [This article](https://www.laurentluce.com/posts/python-list-implementation/) discusses the implementation of lists in Python, which can provide some additional context for why the `pop()` method behaves similar to `append()` in that it resizes the memory allocation in CPython that underpins the `list`. ++

Queues: [Circular Buffers | Wikipedia](https://en.wikipedia.org/wiki/Circular_buffer) ... "Circular buffering makes a good implementation strategy for a queue that has fixed maximum size. Should a maximum size be adopted for a queue, then a circular buffer is a completely ideal implementation; all queue operations are constant time. However, expanding a circular buffer requires shifting memory, which is comparatively costly. For arbitrarily expanding queues, a linked list approach may be preferred instead."

Notes from meeting w/ 

- DS have states (elements inside structure), tests need to run in any particular order.  
- Share the state of the data structures throughout the tests for more robust testing.
- The Stack is not expensive, so this approach is okay for now. But if some object (e.g., psycopg2 drivers, db conns) is expensive then sharing is more efficient.