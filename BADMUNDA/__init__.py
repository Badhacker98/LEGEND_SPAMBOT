import glob
import os
import time

from BADMUNDA.Config import SUDOERS, OWNER_ID, MONGO_URL
from .core import *

from pyrogram import filters
from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli


version = "v2"
group_username = "@PBX_CHAT"
start_time = time.time()


SUDOERS = filters.user()

mongo = MongoClient(MONGO_URL)
mongodb = mongo.BAD

def sudo():
    global SUDOERS
    OWNER = OWNER_ID
    if MONGO_URL is None:
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
