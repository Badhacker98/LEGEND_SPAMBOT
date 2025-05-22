import asyncio
import os
import subprocess

from pyrogram import Client, filters
from pyrogram.types import Message

from BADMUNDA.Config import *

from BADMUNDA import SUDOERS


@Client.on_message(filters.user(SUDOERS) & filters.command(["eval"], prefixes=HANDLER))
async def eval(Badmunda: Client, message: Message):
    cmd = message.text[6:]
    if message.reply_to_message:
        code = message.reply_to_message.text.markdown
    elif cmd:
        try:
            code = message.text.split(" ", maxsplit=1)[1]
            if not code:
                message.reply_text("Gib me code")
        except IndexError:
            code = message.text.split(" \n", maxsplit=1)[1]
            if not code:
                return await message.reply_text("Gib me code!")
    else:
        return await message.reply("Gib me execute code")
    output = subprocess.getoutput(f"python -c {code}")
    await message.reply_text(f"Output: {output}")


@Client.on_message(filters.user(SUDOERS) & filters.command(["exec"], prefixes=HANDLER))
async def exec(Badmunda: Client, message: Message):
    cmd = message.text[6:]
    if message.reply_to_message:
        code = message.reply_to_message.text.markdown
    elif cmd:
        try:
            code = message.text.split(" ", maxsplit=1)[1]
            if not code:
                message.reply_text("Gib me code")
        except IndexError:
            code = message.text.split(" \n", maxsplit=1)[1]
            if not code:
                return await message.reply_text("Gib me code!")
    else:
        return await message.reply("Gib me execute code")
    process = await asyncio.create_subprocess_shell(
        code, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    result = str(stdout.decode().strip()) + str(stderr.decode().strip())
    uid = os.geteuid()
    if uid == 0:
        await message.reply_text(
            f"<b>Code:</b>\n"
            f"<code>{code}</code>\n\n"
            f"<b>Result</b>:\n"
            f"<code>{result}</code>"
        )
    else:
        await message.reply_text(
            f"<b>Code:</b>\n"
            f"<code>{code}</code>\n\n"
            f"<b>Result</b>:\n"
            f"<code>{result}</code>"
        )
      
      
