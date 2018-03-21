import asyncio
import random


async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(random.randint(1, 2))
    return x + y


async def print_sum(x, y):
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))


loop = asyncio.get_event_loop()
coroutine = [print_sum(i, i + 1) for i in range(10)]
print(coroutine)
result = loop.run_until_complete(asyncio.wait(coroutine))
print(result)
loop.close()
