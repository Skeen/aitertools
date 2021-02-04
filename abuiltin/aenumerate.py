async def aenumerate(ait, start=0):
    n = start
    async for elem in ait:
        yield n, elem
        n += 1
