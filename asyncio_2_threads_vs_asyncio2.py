import threading
from urllib.request import urlopen
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

def fetch_url(url):
    urlHandler = urlopen(url)
    json_data = urlHandler.read()
    film = json.loads(json_data)
    print("Film: {}".format(film["title"]))
    print("Director: {}".format(film["director"]))
    print("'%s\' fetched in %ss" % (url, (time.time() - start)))
    print("'%s\' fetched in %ss" % (url, (time.time() - start)))

threads = [threading.Thread(target=fetch_url, args=(url,)) for url in urls]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print("Elapsed Time: %s" % (time.time() - start))