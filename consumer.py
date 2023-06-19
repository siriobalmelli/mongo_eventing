#!/usr/bin/env python3
from db import db
from time import sleep
from random import randrange

bcs = db["broadcasts"]

print("Listening:")
while True:
    try:
        with bcs.watch(full_document="updateLookup") as stream:
            for change in stream:
                doc = change["fullDocument"]
                sleep(randrange(10) / 1000000)  # sleep 0-9µSec
                doc = bcs.find_one_and_update(
                    # find the desired broadcast
                    {"_id": doc["_id"]},
                    # update it
                    {"$set": {"handled": True}},
                )
                # only print if we are the handler
                if not doc["handled"]:
                    print(
                        {k: v for k, v in doc.items() if k in {"broadcast", "alarms"}}
                    )
    except KeyboardInterrupt:
        break
    except Exception as e:  # e.g. when db_reset() drops the collection
        raise e
