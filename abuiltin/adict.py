from .alist import alist


async def adict(ait):
    listy = await alist(ait)
    return dict(listy)
