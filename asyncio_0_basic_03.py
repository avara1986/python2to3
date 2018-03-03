import asyncio
import concurrent.futures
from concurrent.futures import ProcessPoolExecutor
from time import sleep
import random

from past.builtins import di
loop = asyncio.get_event_loop()


def say_boo(i):
    sleep(random.randint(1, 5))
    return '...boo {0}'.format(i)

# async def thread_results():
#     executor = ProcessPoolExecutor(8)
#     futures = [loop.run_in_executor(executor, say_boo, value) for value in range(10)]
#     for result in await asyncio.gather(*futures):
#         print("Result", end=": ")
#         print(result)


async def thread_results():
    with concurrent.futures.ThreadPoolExecutor(max_workers=90) as executor:
        futures = [loop.run_in_executor(executor, say_boo, value) for value in range(10)]
        for result in await asyncio.gather(*futures):
            print("Result", end=": ")
            print(result)


loop.run_until_complete(thread_results())
