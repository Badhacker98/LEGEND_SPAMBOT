from BADMUNDA.Config import *
from ..core.clients import *
from .. import sudos

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.user(sudos) & filters.command(["gcast"], prefixes=HANDLER))
async def broadcast(Badmunda: Client, message: Message):
    if await Badmunda.sudo.sudoFilter(message, 1):
        return

    await Badmunda.functions.broadcast(Badmunda, message)

@Client.on_message(filters.user(sudos) & filters.command(["join"], prefixes=HANDLER))
async def join(Badmunda: Client, message: Message):
    try:
        group = str(message.command[1])
    except:
        await message.reply("__Please give valid join link or username of group to join.__")
        return

    wait = await message.reply("__joining.....__")
    try:
        await Badmunda.join_chat(group)
        await message.reply("**✅ Joined successfully**")
    except Exception as er:
        await message.reply(f"**Error while join:** {str(er)} \n\n__Report in @{Badmunda.supportGroup}__")
    await wait.delete()

@Client.on_message(filters.user(sudos) & filters.command(["left"], prefixes=HANDLER))
async def leave(Badmunda: Client, message: Message):
    if len(message.command) == 1:
        group = message.chat.id
    else:
        try:
            group = message.command[1]
        except:
            await message.reply("__Please give valid join link or username of group to join.__")
            return

    if group in [Badmunda.restrict.res, f"@{Badmunda.supportGroup}", f"@{Badmunda.updateChannel}", Badmunda.supportGroup, Badmunda.updateChannel]:
        return

    wait = await message.reply("__leaving.....__")
    try:
        await Badmunda.join_chat(group)
        await message.reply("**✅ Left successfully**")
    except Exception as er:
        await message.reply(f"**Error while Leave:** {str(er)} \n\n__Report in @{Badmunda.supportGroup}__")
    await wait.delete() 
