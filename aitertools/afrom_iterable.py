async def afrom_iterable(aiters):
    # chain.from_iterable(['ABC', 'DEF']) --> A B C D E F
    async for aiter in aiters:
        async for element in aiter:
            yield element
