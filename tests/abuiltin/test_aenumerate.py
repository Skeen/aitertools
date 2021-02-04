from itertools import tee

import pytest
from hypothesis import given
import hypothesis.strategies as st

from ...abuiltin import aenumerate, aiter, alist


@given(
    listish=st.one_of(
        st.binary(),
        st.lists(st.integers()),
        st.sets(st.integers()),
        st.text(),
        st.tuples(st.integers()),
    ),
    start=st.integers()
)
@pytest.mark.trio
async def test_all_listish(listish, start):
    ait = aiter(listish)
    assert await alist(aenumerate(ait, start)) == list(enumerate(listish, start))

@given(
    iterable=st.iterables(st.integers()),
    start=st.integers()
)
@pytest.mark.trio
async def test_all_iterable(iterable, start):
    it1, it2 = tee(iterable)
    ait = aiter(it1)
    assert await alist(aenumerate(ait, start)) == list(enumerate(it2, start))
