from itertools import tee

import pytest
from hypothesis import given
import hypothesis.strategies as st

from ..abasic import aiter, anext, alist
from .utils import async_generator, aapply_n_times, apply_n_times


@given(length=st.integers(min_value=0, max_value=1000))
@pytest.mark.trio
async def test_anext(length):
    ait = async_generator(length)
    for x in range(length):
        assert await anext(ait) == x
    with pytest.raises(StopAsyncIteration):
        await anext(ait)


@given(
    wrappings=st.integers(min_value=1, max_value=10),
    length=st.integers(min_value=0, max_value=1000)
)
@pytest.mark.trio
async def test_alist(wrappings, length):
    ait = async_generator(length)
    listy = await aapply_n_times(alist, ait, wrappings)
    assert listy == [x for x in range(length)]


@given(
    wrappings=st.integers(min_value=1, max_value=10),
    listish=st.one_of(
        st.binary(),
        st.lists(st.integers()),
        st.sets(st.integers()),
        st.text(),
        st.tuples(st.integers()),
    )
)
@pytest.mark.trio
async def test_aiter_anext_listish(wrappings, listish):
    ait = apply_n_times(aiter, listish, wrappings)
    for x in listish:
        assert await anext(ait) == x
    with pytest.raises(StopAsyncIteration):
        await anext(ait)


@given(
    wrappings=st.integers(min_value=1, max_value=10),
    listish=st.one_of(
        st.binary(),
        st.lists(st.integers()),
        st.sets(st.integers()),
        st.text(),
        st.tuples(st.integers()),
    )
)
@pytest.mark.trio
async def test_aiter_alist_listish(wrappings, listish):
    ait = apply_n_times(aiter, listish, wrappings)
    listy = await alist(ait)
    assert listy == list(listish)


@given(
    wrappings=st.integers(min_value=1, max_value=10),
    iterable=st.iterables(st.integers())
)
@pytest.mark.trio
async def test_aiter_anext_iterable(wrappings, iterable):
    it1, it2 = tee(iterable)
    ait = apply_n_times(aiter, it1, wrappings)
    for x in it2:
        assert await anext(ait) == x
    with pytest.raises(StopAsyncIteration):
        await anext(ait)


@given(
    wrappings=st.integers(min_value=1, max_value=10),
    iterable=st.iterables(st.integers())
)
@pytest.mark.trio
async def test_aiter_alist_iterable(wrappings, iterable):
    it1, it2 = tee(iterable)
    ait = apply_n_times(aiter, it1, wrappings)
    listy = await alist(ait)
    assert listy == list(it2)
