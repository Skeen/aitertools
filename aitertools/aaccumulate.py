import operator

from ..abuiltin import aiter, anext


async def aaccumulate(aiter, func=operator.add, *, initial=None):
    "Return running totals"
    # accumulate([1,2,3,4,5]) --> 1 3 6 10 15
    # accumulate([1,2,3,4,5], initial=100) --> 100 101 103 106 110 115
    # accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120
    total = initial
    if initial is None:
        try:
            total = await anext(aiter)
        except StopAsyncIteration:
            return
    yield total
    async for element in aiter:
        total = func(total, element)
        yield total
