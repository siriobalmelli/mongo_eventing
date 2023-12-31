#!/usr/bin/env python3
from db import db
from random import randrange
from datetime import datetime

bcs = db["broadcasts"]

new_event = {
    "timestamp": datetime.utcnow().isoformat(),
    "random": randrange(2000),
}

obj = bcs.find_one_and_update(
    # find the desired broadcast
    {"broadcast": randrange(10)},
    # update it
    {"$push": {"alarms": new_event}, "$set": {"handled": False}},
    # create it if not existing
    upsert=True,
    return_document=True,
)
print(f"updated: {obj}")
