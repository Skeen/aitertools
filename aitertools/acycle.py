from ..abuiltin import aiter


async def acycle(ait):
    # cycle('ABCD') --> A B C D A B C D A B C D ...
    ait = aiter(ait)

    saved = []
    async for element in ait:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
              yield element
