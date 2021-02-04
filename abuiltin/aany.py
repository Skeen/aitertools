async def aany(ait):
    async for element in ait:
        if element:
            return True
    return False
