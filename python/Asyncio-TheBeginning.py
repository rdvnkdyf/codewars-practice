import asyncio

async def dreaming(n, m):
    """
    Sleeps for n seconds and then returns m ** n, without blocking.
    """
    await asyncio.sleep(n)
    return m ** n
