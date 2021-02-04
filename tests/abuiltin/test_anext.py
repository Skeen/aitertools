import hypothesis.strategies as st
import pytest
from hypothesis import given

from ...abuiltin import anext
from ..utils import async_generator


@given(length=st.integers(min_value=0, max_value=1000))
@pytest.mark.trio
async def test_anext(length):
    ait = async_generator(length)
    for x in range(length):
        assert await anext(ait) == x
    with pytest.raises(StopAsyncIteration):
        await anext(ait)
