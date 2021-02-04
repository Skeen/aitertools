from inspect import isasyncgen


async def aiter(iterator):
    if isasyncgen(iterator):
        async for element in iterator:
            yield element
    else:
        for element in iterator:
            yield element
