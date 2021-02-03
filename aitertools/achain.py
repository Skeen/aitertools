async def achain(*aiters):
    # chain('ABC', 'DEF') --> A B C D E F
    for aiter in aiters:
        async for element in aiter:
            yield element
