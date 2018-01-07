import asyncio
import aiohttp
import async_timeout
import time

start = time.time()
urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']

async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()

async def call_url(url):
    print('Starting {}'.format(url))
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        print("'%s\' fetched in %ss" % (url, (time.time() - start)))

futures = [call_url(url) for url in urls]



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(futures))
    print("Elapsed Time: %s" % (time.time() - start))