# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import asyncio
import concurrent.futures
import logging
import os
import random
import sys
from time import sleep

import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class BulkUser(object):
    CSV_NAME = "example_data2.csv"

    def load_csv(self):
        self.df_aux = pd.read_csv(os.path.join(BASE_DIR, self.CSV_NAME))
        self.df = self.df_aux[:10]

    def load_user(self, data):
        # the magic there
        sleep(random.randint(3, 4))
        return True, "Operaciones sobre el señor {} {}".format(data[1]["nombre"], data[1]["apellido_1"])

    async def bulk(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=90) as executor:
            loop = asyncio.get_event_loop()
            futures = [loop.run_in_executor(executor, self.load_user, row) for row in self.df.iterrows()]
            responses = [(result, messages) for result, messages in await asyncio.gather(*futures)]

        self.df["results"] = [r[0] for r in responses]
        self.df["message_error"] = [r[1] for r in responses]
        print(self.df)

    async def bulk2(self):
        loop = asyncio.get_event_loop()
        futures = [loop.run_in_executor(None, self.load_user, row) for row in self.df.iterrows()]
        for response in await asyncio.gather(*futures):
            print("Response")
            print(response)

    def bulk_sync(self):
        for row in self.df_aux.iterrows():
            response = self.load_user(row)
            print("Response")
            print(response)


if __name__ == '__main__':
    args = sys.argv[1:]
    bulk = BulkUser()
    bulk.load_csv()
    args = ["async", ]
    # args = []
    if len(args) > 0 and args[0] == "async":
        loop = asyncio.get_event_loop()
        loop.run_until_complete(bulk.bulk())
    else:
        bulk.bulk_sync()
