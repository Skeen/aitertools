# TODO: Implemement default parameter
async def anext(ait, default=None):
    return (await ait.__anext__())
