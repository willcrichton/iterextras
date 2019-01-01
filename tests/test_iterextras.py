from iterextras import *


def test_unzip_basic():
    l = [(1, 2), (3, 4)]
    assert unzip(l) == ([1, 3], [2, 4])


def test_unzip_empty():
    assert unzip([]) == ([], [])


def test_unzip_three():
    l = [(1, 2, 3), (4, 5, 6)]
    assert unzip(l) == ([1, 4], [2, 5], [3, 6])


def test_par_for_basic():
    l = par_for(lambda x: x + 1, [1, 2, 3])
    assert l == [2, 3, 4]


def test_par_filter():
    l = par_filter(lambda x: x % 2 == 0, [1, 2, 3])
    assert l == [2]


def test_flatten():
    l = [[1, 2], [], [3, 4]]
    assert flatten(l) == [1, 2, 3, 4]


def test_collect():
    l = [('a', 1), ('b', 2), ('a', 3)]
    d = collect(l, lambda t: t[0])
    assert d == {'a': [('a', 1), ('a', 3)], 'b': [('b', 2)]}


def test_batch():
    l = [1, 2, 3, 4, 5]
    assert list(batch(l, 2)) == [[1, 2], [3, 4], [5]]
