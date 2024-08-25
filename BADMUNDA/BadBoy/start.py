import platform

from SukhPB.start import start_cmd
from pyrogram import Client
from pyrogram import __version__ as py_version
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, Message

from BADMUNDA.Config import *

from ..core.clients import *

if START_PIC:
    START_PIC = START_PIC
else:
    START_PIC = ""


@Client.on_message(filters.command(["start"], prefixes=HANDLER))
async def _start(Badmunda: Client, message: Message):
    global START_MESSAGE
    my_detail = await Badmunda.get_me()
    my_mention = my_detail.mention
    if START_MESSAGE:
        START_MESSAGE = START_MESSAGE
    else:
        START_MESSAGE = f"ʜᴇʏ💫 {message.from_user.mention}🌸\n✥ ɪ ᴀᴍ {my_mention}\n\n❖━━━━•❅•°•❈•°•❅•━━━━❖\n\n✥ **__ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ__** = {py_version}\n✥ **__ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ__** = {platform.python_version()}\n✥ **__ʙᴏᴛsᴘᴀᴍ ᴠᴇʀsɪᴏɴ__** = {version}\n\n❖━━━━•❅•°•❈•°•❅•━━━━❖"
    if ".jpg" in START_PIC or ".png" in START_PIC:
        for i in range(1, 26):
            lol = globals()[f"Client{i}"]
            if lol is not None:
                await lol.send_photo(
                    message.chat.id,
                    START_PIC,
                    caption=START_MESSAGE,
                    reply_markup=InlineKeyboardMarkup(await start_cmd(Badmunda)),
                )
    elif ".mp4" in START_PIC.lower():
        for i in range(1, 26):
            lol = globals()[f"Client{i}"]
            if lol is not None:
                await lol.send_video(
                    message.chat.id,
                    START_PIC,
                    caption=START_MESSAGE,
                    reply_markup=InlineKeyboardMarkup(await start_cmd(Badmunda)),
                )
    else:
        for i in range(1, 26):
            lol = globals()[f"Client{i}"]
            if lol is not None:
                await lol.send_message(
                    message.chat.id,
                    START_MESSAGE,
                    reply_markup=InlineKeyboardMarkup(await start_cmd(Badmunda)),
                )
