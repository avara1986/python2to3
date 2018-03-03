import asyncio
import random


async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(random.randint(1,20))
    return x + y

async def print_sum(x, y):
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([print_sum(i, i+1) for i in range(10)]))
loop.close()