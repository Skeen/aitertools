async def aall(ait):
    async for element in ait:
        if not element:
            return False
    return True
