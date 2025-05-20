import asyncio
from random import choice

from SukhPB.raidd import PBRAID
from pyrogram import Client, filters
from pyrogram.types import Message

from BADMUNDA.Config import *

from .. import sudos
from ..core.clients import *


@Client.on_message(filters.user(sudos) & filters.command(["Pbiraid"], prefixes=HANDLER))
async def Pbiraid(Badmunda: Client, e: Message):
    usage = f"Command :- {HANDLER}Pbiraid (count) (reply to anyone)\nUsage :- `{HANDLER}Pbiraid 3 <reply to anyone>`\n\nCommand :- {HANDLER}Pbiraid <count> <username>\nUsage :- `{HANDLER}Pbiraid 3 @Hekeke`"
    lol = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
    chat = e.chat
    try:
        counts = int(lol[0])
    except ValueError:
        return await e.reply_text(usage)
    if len(lol) == 2:
        if not counts:
            await e.reply_text(
                f"Gib Pbiraid Counts or use `{HANDLER}.upbiraid` for Unlimited Pbiraid!"
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
        Pbiraid = choice(PBRAID)
        for i in range(1, 26):
            lol = globals()[f"Client{i}"]
            if lol is not None:
                await lol.send_message(chat.id, f"{user.mention} {raid}")
                await asyncio.sleep(0.3)
    if LOG_CHANNEL:
        try:
            await Badmunda.send_message(
                LOG_CHANNEL,
                f"started Raid By User: {e.from_user.id} \n\n On User: {mention} \n Chat: {e.chat.id} \n Counts: {counts}",
            )
        except Exception as a:
            print(a)
