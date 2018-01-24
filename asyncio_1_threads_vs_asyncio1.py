import asyncio
import aiohttp
import async_timeout
import time
import json

start = time.time()
urls = [
    'https://ghibliapi.herokuapp.com/films/2baf70d1-42bb-4437-b551-e5fed5a87abe',
    'https://ghibliapi.herokuapp.com/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49',
    'https://ghibliapi.herokuapp.com/films/ebbb6b7c-945c-41ee-a792-de0e43191bd8',
    'https://ghibliapi.herokuapp.com/films/0440483e-ca0e-4120-8c50-4c8cd9b965d6',
    'https://ghibliapi.herokuapp.com/films/dc2e6bd1-8156-4886-adff-b39e6043af0c',
]

async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()

async def call_url(url):
    print('Starting {}'.format(url))
    async with aiohttp.ClientSession() as session:
        json_data = await fetch(session, url)
        film = json.loads(json_data)
        print("Film: {}".format(film["title"]))
        print("Director: {}".format(film["director"]))
        print("'%s\' fetched in %ss" % (url, (time.time() - start)))

futures = [call_url(url) for url in urls]



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(futures))
    print("Elapsed Time: %s" % (time.time() - start))