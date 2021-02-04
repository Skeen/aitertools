async def async_generator(to=3):
    for x in range(to):
        yield x


async def aapply_n_times(func, ait, times):
    for x in range(times):
        ait = await func(ait)
    return ait


def apply_n_times(func, ait, times):
    for x in range(times):
        ait = func(ait)
    return ait
