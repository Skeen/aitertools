from inspect import isasyncgen


async def alist(ait):
    if isasyncgen(ait):
        return [element async for element in ait]
    return ait
