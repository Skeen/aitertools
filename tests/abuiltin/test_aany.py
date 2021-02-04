from itertools import tee

import pytest
from hypothesis import given
import hypothesis.strategies as st

from ...abuiltin import aany, aiter


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
async def test_any_listish(listish):
    ait = aiter(listish)
    assert await aany(ait) == any(listish)

@given(
    iterable=st.iterables(st.booleans())
)
@pytest.mark.trio
async def test_any_iterable(iterable):
    it1, it2 = tee(iterable)
    ait = aiter(it1)
    assert await aany(ait) == any(it2)
