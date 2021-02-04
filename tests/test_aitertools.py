from itertools import count

import hypothesis.strategies as st
import pytest
from hypothesis import given

from ..abuiltin import anext
from ..aitertools import acount


@given(start=st.integers(), step=st.integers())
@pytest.mark.trio
async def test_anext(start, step):
    it = count(start, step)
    ait = acount(start, step)
    for x in range(10):
        avalue = await anext(ait)
        value = next(it)
        assert avalue == value
