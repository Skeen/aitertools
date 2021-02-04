# Needs testing
async def afilter(function, ait):
    # TODO: Handle awaitable function
    async for element in ait:
        if function(element):
            yield element
