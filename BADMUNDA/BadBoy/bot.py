import datetime
import os
import sys
import time

from SukhPB.get_time import get_time
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from BADMUNDA import start_time
from BADMUNDA.Config import *

from .. import SUDO_USERS as sudos
from ..core.clients import *

SUPPORT_CHAT_URL = "https://t.me/PBX_CHAT"
UPDATE_CHANNEL_URL = "https://t.me/HEROKUBIN_01"

if PING_PIC:
    PING_PIC = PING_PIC
else:
    PING_PIC = "https://telegra.ph/file/c26f985c3f59004bc9927.jpg"


@Client.on_message(filters.user(sudos) & filters.command(["ping"], prefixes=HANDLER))
async def ping(_, e: Message):
    start = datetime.datetime.now()
    uptime = get_time((time.time() - start_time))
    user_mention = f"[{e.from_user.first_name}](tg://user?id={e.from_user.id})" if e.from_user else "User"
    a = await e.reply_text("ᴘᴏɴɢ 👻")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000

    ping_temp = (
        f"📌 ᴘɪɴɢ ᴘᴏɴɢ \n\n"
        f"🧪 ᴘɪɴɢ: {ms} ms\n"
        f"🌡️ ᴜᴘᴛɪᴍᴇ: {uptime}\n"
        f"👻 ᴏᴡɴᴇʀ: {user_mention}"
    )

    # Inline Buttons
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("✯ sᴜᴘᴘᴏʀᴛ ✯", url=SUPPORT_CHAT_URL),
                InlineKeyboardButton("✯ ᴜᴘᴅᴀᴛᴇ ✯", url=UPDATE_CHANNEL_URL)
            ]
        ]
    )

    await a.delete()
    for i in range(1, 26):
        lol = globals().get(f"Client{i}")
        if lol is not None:
            if ".jpg" in PING_PIC or ".png" in PING_PIC:
                await lol.send_photo(
                    e.chat.id,
                    PING_PIC,
                    caption=ping_temp,
                    reply_markup=buttons,
                )
            elif ".mp4" in PING_PIC.lower():
                await lol.send_video(
                    e.chat.id,
                    PING_PIC,
                    caption=ping_temp,
                    reply_markup=buttons,
                )
            else:
                await lol.send_message(
                    e.chat.id,
                    ping_temp,
                    reply_markup=buttons,
                )


@Client.on_message(
    filters.user(sudos) & filters.command(["restart", "reboot"], prefixes=HANDLER)
)
async def restarter(Badmunda: Client, message: Message):
    await message.reply_text(
        f"**Bot Is Restarting**\n\n Please Wait 5 min till bot is restart.\nAfter 5 Min Type {HANDLER}ping"
    )
    try:
        await Badmunda.stop()
    except Exception as error:
        print(str(error))

    args = [sys.executable, "-m", "BADMUNDA"]
    os.execl(sys.executable, *args)
    quit()
