from itertools import tee

import pytest
from hypothesis import given
import hypothesis.strategies as st

from ...abuiltin import alist, aiter
from ..utils import async_generator, aapply_n_times, apply_n_times


@given(
    wrappings=st.integers(min_value=1, max_value=10),
    length=st.integers(min_value=0, max_value=1000)
)
@pytest.mark.trio
async def test_alist_generator(wrappings, length):
    ait = async_generator(length)
    listy = await aapply_n_times(alist, ait, wrappings)
    assert listy == [x for x in range(length)]


@given(
    aiter_wrappings=st.integers(min_value=1, max_value=10),
    alist_wrappings=st.integers(min_value=1, max_value=10),
    listish=st.one_of(
        st.binary(),
        st.lists(st.integers()),
        st.sets(st.integers()),
        st.text(),
        st.tuples(st.integers()),
    )
)
@pytest.mark.trio
async def test_alist_listish(aiter_wrappings, alist_wrappings, listish):
    ait = apply_n_times(aiter, listish, aiter_wrappings)
    listy = await aapply_n_times(alist, ait, alist_wrappings)
    assert listy == list(listish)

@given(
    aiter_wrappings=st.integers(min_value=1, max_value=10),
    alist_wrappings=st.integers(min_value=1, max_value=10),
    iterable=st.iterables(st.integers())
)
@pytest.mark.trio
async def test_alist_iterable(aiter_wrappings, alist_wrappings, iterable):
    it1, it2 = tee(iterable)
    ait = apply_n_times(aiter, it1, aiter_wrappings)
    listy = await aapply_n_times(alist, ait, alist_wrappings)
    assert listy == list(it2)
