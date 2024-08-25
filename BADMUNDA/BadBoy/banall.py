from SukhPB.banall import start_banall
from pyrogram import Client, filters
from pyrogram.types import Message

from BADMUNDA.Config import *

from .. import sudos


@Client.on_message(filters.user(sudos) & filters.command(["banall"], prefixes=HANDLER))
async def banall(Badmunda: Client, message: Message):
    if message.chat.id == message.from_user.id:
        await message.reply_text("Use this cmd in group;")
        return
    await start_banall(Badmunda, message)
