import random
import asyncio


async def say_boo():
    i = 0
    while i < 5:
        print('...boo {0}'.format(i))
        i += 1
        await asyncio.sleep(random.randint(0, 5))


async def say_baa():
    i = 0
    while i < 5:
        print('...baa {0}'.format(i))
        i += 1
        await asyncio.sleep(random.randint(0, 2))


loop = asyncio.get_event_loop()
corrutine_boo = say_boo()
print(corrutine_boo)
asyncio.ensure_future(corrutine_boo)
asyncio.ensure_future(say_baa())
print(corrutine_boo)
loop.run_forever()