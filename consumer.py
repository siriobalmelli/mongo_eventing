#!/usr/bin/env python3
from db import db

bcs = db["broadcasts"]

print("Listening:")
while True:
    try:
        with bcs.watch(full_document="updateLookup") as stream:
            for change in stream:
                print(change["fullDocument"])
    except KeyboardInterrupt:
        break
    except Exception:  # e.g. when db_reset() drops the collection
        pass
