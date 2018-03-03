import asyncio
import json

import aiohttp

results = []


async def fetch(future, url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            future.set_result(await resp.text())


def got_result(future):
    result = (future.result())
    results.append(json.loads(result))


loop = asyncio.get_event_loop()
future1 = asyncio.Future()
future2 = asyncio.Future()

asyncio.ensure_future(fetch(future1, "https://ghibliapi.herokuapp.com/films/2baf70d1-42bb-4437-b551-e5fed5a87abe"))
future1.add_done_callback(got_result)
asyncio.ensure_future(fetch(future2, "https://ghibliapi.herokuapp.com/people/ba924631-068e-4436-b6de-f3283fa848f0"))
future2.add_done_callback(got_result)

# RESULTS?
print(len(results))  # -> 0
# FUTURE 1
print(future1.done())  # -> False
result = asyncio.ensure_future(future1)
print(result.done())  # -> False
try:
    print(future1.result())
except asyncio.base_futures.InvalidStateError:
    print("Sin resultados")  # -> Print this line

# FUTURE 2
try:
    print(future2.result())
except asyncio.base_futures.InvalidStateError:
    print("Sin resultados")  # -> Print this line

# RUN LOOP
loop.run_until_complete(future1)
loop.run_until_complete(future2)

# RESULTS?
print(len(results))  # -> 2
# FUTURE 1
print(future1.done())   # -> True
result = asyncio.ensure_future(future1)
print(result.done())  # -> True
print(future1.result())  # -> [{'id': '2baf70d1-42bb-4437-b551-e5fed5a87abe', 'title': ....
# FUTURE 2
print(future2.done())   # -> True
result = asyncio.ensure_future(future2)
print(result.done())  # -> True
print(future2.result())  # -> [{'id': 'ba924631-068e-4436-b6de-f3283fa848f0', 'title': ....
