import asyncio
import operator

from abasic import aiter, alist, anext

from aitertools import aaccumulate, achain, acount, acycle, afrom_iterable, arepeat


async def main():
    # cycle
    async_iter = acycle("ABCD")
    assert await anext(async_iter) == "A"
    assert await anext(async_iter) == "B"
    assert await anext(async_iter) == "C"
    assert await anext(async_iter) == "D"
    assert await anext(async_iter) == "A"
    assert await anext(async_iter) == "B"

    async_iter = acycle(aiter("ABCD"))
    assert await anext(async_iter) == "A"
    assert await anext(async_iter) == "B"
    assert await anext(async_iter) == "C"
    assert await anext(async_iter) == "D"
    assert await anext(async_iter) == "A"
    assert await anext(async_iter) == "B"

    # repeat
    async_iter = arepeat(10, 3)
    assert await anext(async_iter) == 10
    assert await anext(async_iter) == 10
    assert await anext(async_iter) == 10
    exception = False
    try:
        await anext(async_iter)
    except StopAsyncIteration:
        exception = True
    assert exception == True

    # accumulate
    async_iter = aaccumulate(aiter([1, 2, 3, 4, 5]))
    assert await anext(async_iter) == 1
    assert await anext(async_iter) == 3
    assert await anext(async_iter) == 6
    assert await anext(async_iter) == 10
    assert await anext(async_iter) == 15
    exception = False
    try:
        await anext(async_iter)
    except StopAsyncIteration:
        exception = True
    assert exception == True

    async_iter = aaccumulate(aiter([1, 2, 3, 4, 5]), initial=100)
    assert await anext(async_iter) == 100
    assert await anext(async_iter) == 101
    assert await anext(async_iter) == 103
    assert await anext(async_iter) == 106
    assert await anext(async_iter) == 110
    assert await anext(async_iter) == 115
    exception = False
    try:
        await anext(async_iter)
    except StopAsyncIteration:
        exception = True
    assert exception == True

    async_iter = aaccumulate(aiter([1, 2, 3, 4, 5]), operator.mul)
    assert await anext(async_iter) == 1
    assert await anext(async_iter) == 2
    assert await anext(async_iter) == 6
    assert await anext(async_iter) == 24
    assert await anext(async_iter) == 120
    exception = False
    try:
        await anext(async_iter)
    except StopAsyncIteration:
        exception = True
    assert exception == True

    async_iter_1 = aiter("ABC")
    async_iter_2 = aiter("DEF")
    async_iter = achain(async_iter_1, async_iter_2)
    assert await anext(async_iter) == "A"
    assert await anext(async_iter) == "B"
    assert await anext(async_iter) == "C"
    assert await anext(async_iter) == "D"
    assert await anext(async_iter) == "E"
    assert await anext(async_iter) == "F"
    exception = False
    try:
        await anext(async_iter)
    except StopAsyncIteration:
        exception = True
    assert exception == True

    async_iter_1 = aiter("ABC")
    async_iter_2 = aiter("DEF")
    async_iter = afrom_iterable(aiter([async_iter_1, async_iter_2]))
    assert await anext(async_iter) == "A"
    assert await anext(async_iter) == "B"
    assert await anext(async_iter) == "C"
    assert await anext(async_iter) == "D"
    assert await anext(async_iter) == "E"
    assert await anext(async_iter) == "F"
    exception = False
    try:
        await anext(async_iter)
    except StopAsyncIteration:
        exception = True
    assert exception == True

    async_iter = aiter("ABCDEFG")
    assert await anext(async_iter) == "A"
    assert await anext(async_iter) == "B"
    assert await anext(async_iter) == "C"

    async_iter = aiter("ABCDEFG")
    async_list = await alist(async_iter)
    assert async_list == ["A", "B", "C", "D", "E", "F", "G"]

    print("HI")

    # async_iter = iters('ABCDEFG')
    # async_iter = islice(async_iter, 2)
    # async_list = await alist(async_iter)
    # assert async_list == ['A', 'B']


asyncio.run(main())
