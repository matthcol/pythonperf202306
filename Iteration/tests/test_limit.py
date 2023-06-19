import pytest
from collections.abc import Iterator
import limit

@pytest.mark.parametrize("n", list(range(3)))
def test_limit_empty_iterable(n):
    iterable = []
    g = limit.limit(iterable, n)
    assert isinstance(g, Iterator)
    l = list(g)
    assert len(l) == 0

@pytest.mark.parametrize("n", [3, 4, 5])
def test_limit_all_elements(n):
    iterable = [7, 9, 8]
    g = limit.limit(iterable, n)
    assert isinstance(g, Iterator)
    l = list(g)
    assert len(l) == 3
    assert l == iterable

@pytest.mark.parametrize("n", list(range(4)))
def test_limit_zero_to_all_elements(n):
    iterable = [7, 9, 8]
    g = limit.limit(iterable, n)
    assert isinstance(g, Iterator)
    l = list(g)
    assert len(l) == n
    assert l == iterable[:n]

@pytest.mark.parametrize("n", list(range(4)))
def test_limit_on_iterator(n):
    iterable = [7, 9, 8]
    it = iter(iterable)
    g = limit.limit(iterable, n)
    assert isinstance(g, Iterator)
    l = list(g)
    assert len(l) == n
    assert l == iterable[:n]


