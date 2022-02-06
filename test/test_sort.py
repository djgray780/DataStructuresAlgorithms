from sort import selection_sort

def test_myselsort():
    assert selection_sort([1,2,0,3,4], ascend=True) == [0,1,2,3,4]
    assert selection_sort([1,2,0,3,4], ascend=False) == [4,3,2,1,0]
    assert selection_sort([-1,0,1,0,-1,1], ascend=True) == [-1,-1,0,0,1,1]
    assert selection_sort([-1,0,1,0,-1,1], ascend=False) == [1,1,0,0,-1,-1]