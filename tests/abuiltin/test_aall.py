from itertools import tee

import hypothesis.strategies as st
import pytest
from hypothesis import given

from ...abuiltin import aall, aiter


@given(
    listish=st.one_of(
        st.binary(),
        st.lists(st.booleans()),
        st.sets(st.booleans()),
        st.text(),
        st.tuples(st.booleans()),
    )
)
@pytest.mark.trio
async def test_all_listish(listish):
    ait = aiter(listish)
    assert await aall(ait) == all(listish)


@given(iterable=st.iterables(st.booleans()))
@pytest.mark.trio
async def test_all_iterable(iterable):
    it1, it2 = tee(iterable)
    ait = aiter(it1)
    assert await aall(ait) == all(it2)
