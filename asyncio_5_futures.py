import asyncio
import json

import aiohttp

urls = [
    'https://ghibliapi.herokuapp.com/films/2baf70d1-42bb-4437-b551-e5fed5a87abe',
    'https://ghibliapi.herokuapp.com/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49',
    'https://ghibliapi.herokuapp.com/films/ebbb6b7c-945c-41ee-a792-de0e43191bd8',
    'https://ghibliapi.herokuapp.com/films/0440483e-ca0e-4120-8c50-4c8cd9b965d6',
    'https://ghibliapi.herokuapp.com/films/dc2e6bd1-8156-4886-adff-b39e6043af0c',
]

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
# [asyncio.ensure_future(fetch(future, url)) for url in urls]
asyncio.ensure_future(fetch(future1, "https://ghibliapi.herokuapp.com/films/2baf70d1-42bb-4437-b551-e5fed5a87abe"))
future1.add_done_callback(got_result)
asyncio.ensure_future(fetch(future2, "https://ghibliapi.herokuapp.com/people/ba924631-068e-4436-b6de-f3283fa848f0"))
future2.add_done_callback(got_result)

# RESULTS?
print(len(results))
print(results)
# FUTURE 1
print(future1.done())
result = asyncio.ensure_future(future1)
print(result.done())
try:
    print(future1.result())
except asyncio.base_futures.InvalidStateError:
    print("Sin resultados")
# FUTURE 2
print(future2.done())
result = asyncio.ensure_future(future2)
print(result.done())
try:
    print(future2.result())
except asyncio.base_futures.InvalidStateError:
    print("Sin resultados")


# RUN LOOP
loop.run_until_complete(future1)
loop.run_until_complete(future2)

# RESULTS?
print(len(results))
print(results)
# FUTURE 1
print(future1.done())
result = asyncio.ensure_future(future1)
print(result.done())
print(future1.result())
# FUTURE 2
print(future2.done())
result = asyncio.ensure_future(future2)
print(result.done())
print(future2.result())
