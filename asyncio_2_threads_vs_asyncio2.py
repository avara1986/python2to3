import threading
from multiprocessing.pool import ThreadPool

from urllib.request import urlopen
import time
import json

urls = [
    'https://ghibliapi.herokuapp.com/films/2baf70d1-42bb-4437-b551-e5fed5a87abe',
    'https://ghibliapi.herokuapp.com/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49',
    'https://ghibliapi.herokuapp.com/films/ebbb6b7c-945c-41ee-a792-de0e43191bd8',
    'https://ghibliapi.herokuapp.com/films/0440483e-ca0e-4120-8c50-4c8cd9b965d6',
    'https://ghibliapi.herokuapp.com/films/dc2e6bd1-8156-4886-adff-b39e6043af0c',
]


def fetch_url(url):
    urlHandler = urlopen(url)
    json_data = urlHandler.read()
    film = json.loads(json_data)
    print("Film: {}".format(film["title"]))
    print("Director: {}".format(film["director"]))
    print("'%s\' fetched in %ss" % (url, (time.time() - start)))
    print("'%s\' fetched in %ss" % (url, (time.time() - start)))
    return film["title"]


results = []
start = time.time()

threads = [threading.Thread(target=fetch_url, args=(url,)) for url in urls]
for thread in threads:
    thread.start()
for thread in threads:
    results.append(thread.join())

print(results)
print("Elapsed Time: %s" % (time.time() - start))


start = time.time()

pool = ThreadPool(processes=9)
async_result = [pool.apply_async(fetch_url, (url,)) for url in urls]

print([res.get(timeout=1) for res in async_result])
print("Elapsed Time: %s" % (time.time() - start))
