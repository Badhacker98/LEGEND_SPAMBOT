from random import choice

from pyLegendBS.abuse import abuse as galia
from SukhPB.get_user import user_only
from SukhPB.raid import RAID
from pyrogram import Client, filters
from pyrogram.types import Message

from BADMUNDA.Config import *

from .. import sudos
from ..core.clients import *

unlimited = False


@Client.on_message(filters.user(sudos) & filters.command(["uspam"], prefixes=HANDLER))
async def uspam(Badmunda: Client, e: Message):
    global unlimited
    unlimited = True
    msg = str(e.text[6:])
    if not msg:
        await e.reply("Gime Spam message bruh!")
        return
    if e.reply_to_message:
        lmao = e.reply_to_message
        while unlimited == True:
            for i in range(1, 26):
                lol = globals()[f"Client{i}"]
                if lol is not None:
                    await lol.send_message(e.chat.id, f"{lmao.from_user.mention} {msg}")
    else:
        while unlimited == True:
            for i in range(1, 26):
                lol = globals()[f"Client{i}"]
                if lol is not None:
                    await lol.send_message(e.chat.id, msg)
    if LOG_CHANNEL:
        try:
            await Badmunda.send_message(
                LOG_CHANNEL,
                f"started Unlimited Spam By User: {e.from_user.id} \n\n Chat: {e.chat.id} \n Spam Message: {msg}",
            )
        except Exception as a:
            print(a)


@Client.on_message(filters.user(sudos) & filters.command(["uraid"], prefixes=HANDLER))
async def uraid(Badmunda: Client, e: Message):
    global unlimited
    unlimited = True
    user = await user_only(Badmunda, e)
    mention = user.mention
    if e.reply_to_message:
        lmao = e.reply_to_message
        while unlimited == True:
            reply = choice(RAID)
            raid_msg = f"{lmao.from_user.mention} {reply}"
            for i in range(1, 26):
                lol = globals()[f"Client{i}"]
                if lol is not None:
                    await lol.send_message(e.chat.id, raid_msg)
    else:
        while unlimited == True:
            reply = choice(RAID)
            raid_msg = f"{mention} {reply}"
            for i in range(1, 26):
                lol = globals()[f"Client{i}"]
                if lol is not None:
                    await lol.send_message(e.chat.id, raid_msg)
    if LOG_CHANNEL:
        try:
            await Badmunda.send_message(
                LOG_CHANNEL,
                f"started Raid By User: {e.from_user.id} \n\n On User: {mention} \n Chat: {e.chat.id}",
            )
        except Exception as a:
            print(a)


@Client.on_message(
    filters.user(sudos) & filters.command(["abuse", "gali"], prefixes=HANDLER)
)
async def abuse(Badmunda: Client, e: Message):
    global unlimited
    unlimited = True
    if e.reply_to_message:
        lmao = e.reply_to_message
        while unlimited == True:
            msg = choice(galia)
            for i in range(1, 26):
                lol = globals()[f"Client{i}"]
                if lol is not None:
                    await lol.send_message(e.chat.id, f"{lmao.from_user.mention} {msg}")
    else:
        while unlimited == True:
            msg = choice(galia)
            for i in range(1, 26):
                lol = globals()[f"Client{i}"]
                if lol is not None:
                    await lol.send_message(e.chat.id, f"{msg}")
    if LOG_CHANNEL:
        try:
            await Badmunda.send_message(
                LOG_CHANNEL,
                f"started Raid By User: {e.from_user.id} \n\n On User: {mention} \n Chat: {e.chat.id}",
            )
        except Exception as a:
            print(a)


@Client.on_message(filters.user(sudos) & filters.command(["stop"], prefixes=HANDLER))
async def stop(_, e: Message):
    global unlimited
    unlimited = False
    await e.reply_text("Stopped Unlimited Spam/Raid/abuse -;")


@Client.on_message(
    filters.user(sudos) & filters.command(["echo", "repeat"], prefixes=HANDLER)
)
async def echo_(Badmunda: Client, message: Message):
    txt = " ".join(message.command[1:])
    if message.reply_to_message:
        msg = message.reply_to_message.text.markdown
    elif txt:
        msg = str(txt)
    else:
        await message.reply_text(
            f"**Wrong Usage!** \n\n Syntax: {HANDLER}echo (message or reply to message)"
        )
        return

    try:
        await message.delete()
        await Badmunda.send_message(message.chat.id, msg)
    except Exception as a:
        await Badmunda.send_message(message.chat.id, msg)
        print(str(a))
          
