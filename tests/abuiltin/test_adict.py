from itertools import tee

import pytest
from hypothesis import given
import hypothesis.strategies as st

from ...abuiltin import adict, aiter


@given(
    listish=st.one_of(
        st.lists(st.tuples(st.text(), st.integers())),
        st.lists(st.lists(st.integers(), min_size=2, max_size=2)),
        st.sets(st.tuples(st.text(), st.integers())),
    )
)
@pytest.mark.trio
async def test_all_listish(listish):
    ait = aiter(listish)
    assert await adict(ait) == dict(listish)

@given(
    iterable=st.one_of(
        st.iterables(st.tuples(st.text(), st.integers())),
        st.iterables(st.lists(st.integers(), min_size=2, max_size=2)),
    )
)
@pytest.mark.trio
async def test_all_iterable(iterable):
    it1, it2 = tee(iterable)
    ait = aiter(it1)
    assert await adict(ait) == dict(it2)
