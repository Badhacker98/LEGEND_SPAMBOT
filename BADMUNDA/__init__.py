import glob
import os
import time

from .Config import *
from .core import *

from pyrogram import filters
from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli


version = "v2"
group_username = "@PBX_CHAT"
start_time = time.time()


SUDOERS = filters.user()

mongo = MongoClient(config.MONGO_URL)
mongodb = mongo.BAD

def sudo():
    global SUDOERS
    OWNER = config.OWNER_ID
    if config.MONGO_URL is None:
        SUDOERS.add(OWNER)
    else:
        sudoersdb = mongodb.sudoers
        sudoers = sudoersdb.find_one({"sudo": "sudo"})
        sudoers = [] if not sudoers else sudoers["sudoers"]
        SUDOERS.add(OWNER)
        if OWNER not in sudoers:
            sudoers.append(OWNER)
            sudoersdb.update_one(
                {"sudo": "sudo"},
                {"$set": {"sudoers": sudoers}},
                upsert=True,
            )
        if sudoers:
            for x in sudoers:
                SUDOERS.add(x)
    print("Sudoers Loaded.")

sudo()
