import sys
from BADMUNDA.Config import *
import heroku3
from .. import sudos
from pyrogram import Client, filters, enums
from os import execl, getenv
from telethon import events
from datetime import datetime
from pyrogram.types import InlineKeyboardMarkup, Message


@Client.on_message(filters.command(["addsudo"], prefixes=HANDLER))
async def _sudo(Badmunda: Client, message: Message):
    if message.from_user.id == OWNER_ID:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        sudousers = getenv("SUDO_USERS", default=None)

        ok = await message.reply(f"✦ ᴀᴅᴅɪɴɢ ᴜꜱᴇʀ ᴀꜱ ꜱᴜᴅᴏ...")
        target = ""
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("✦ `[HEROKU] ➥" "\n✦ Please Setup Your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        try:
            reply_msg = message.reply_to_message
            if reply_msg is None:
                await ok.edit("✦ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ.")
                return
            target = reply_msg.from_user.id
        except Exception as e:
            await ok.edit("✦ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ.")
            return

        if str(target) in sudousers:
            await ok.edit(f"✦ ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ !!")
        else:
            if len(sudousers) > 0:
                newsudo = f"{sudousers} {target}"
            else:
                newsudo = f"{target}"
            await ok.edit(f"✦ **ɴᴇᴡ ꜱᴜᴅᴏ ᴜꜱᴇʀ** ➥ `{target}`")
            heroku_var["SUDO_USERS"] = newsudo    
    
    elif message.from_user.id in SUDO_USERS:
        await message.reply("✦ ꜱᴏʀʀʏ, ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.")
