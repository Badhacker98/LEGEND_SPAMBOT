import asyncio
from random import choice

from Sukh.craid import CRAID
from pyrogram import Client, filters
from pyrogram.types import Message

from BADMUNDA.Config import *

from .. import sudos
from ..core.clients import *


@Client.on_message(filters.user(sudos) & filters.command(["craid"], prefixes=HANDLER))
async def craid(Badmunda: Client, e: Message):
    usage = f"Command :- {HANDLER}craid (count) (reply to anyone)\nUsage :- `{HANDLER}craid 3 <reply to anyone>`\n\nCommand :- {HANDLER}craid <count> <username>\nUsage :- `{HANDLER}craid 3 @Hekeke`"
    lol = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
    chat = e.chat
    try:
        counts = int(lol[0])
    except ValueError:
        return await e.reply_text(usage)
    if len(lol) == 2:
        if not counts:
            await e.reply_text(
                f"Gib craid Counts or use `{HANDLER}.ucraid` for Unlimited craid!"
            )
            return
        owo = lol[1]
        if not owo:
            await e.reply_text(
                "you need to specify an user! Reply to any user or gime id/username"
            )
            return
        try:
            user = await Badmunda.get_users(lol[1])
        except:
            await e.reply_text("**Error:** User not found!")
            return
    elif e.reply_to_message:
        try:
            user = await Badmunda.get_users(e.reply_to_message.from_user.id)
        except:
            user = e.reply_to_message.from_user
    else:
        await e.reply_text(usage)
        return
    for _ in range(counts):
        craid = choice(CRAID)
        for i in range(1, 26):
            lol = globals()[f"Client{i}"]
            if lol is not None:
                await lol.send_message(chat.id, f"{user.mention} {craid}")
                await asyncio.sleep(0.3)
    if LOG_CHANNEL:
        try:
            await Badmunda.send_message(
                LOG_CHANNEL,
                f"started craid By User: {e.from_user.id} \n\n On User: {mention} \n Chat: {e.chat.id} \n Counts: {counts}",
            )
        except Exception as a:
            print(a)


USERS = []


@Client.on_message(filters.all)
async def checkraid(Badmunda: Client, msg: Message):
    global USERS
    if int(msg.from_user.id) in USERS:
        await msg.reply_text(choice(CRAID))
          
