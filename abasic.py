import inspect


async def aiter(iterator):
    if inspect.isasyncgen(iterator):
        async for element in iterator:
            yield element
    else:
        for element in iterator:
            yield element


async def anext(ait):
    return (await ait.__anext__())


async def alist(ait):
    if inspect.isasyncgen(ait):
        return [element async for element in ait]
    return ait
