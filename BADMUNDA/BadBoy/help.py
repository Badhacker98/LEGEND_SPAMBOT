from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message

from Data import Data
from BADMUNDA.Config import *

if HELP_MSG:
    HELP_MSG = HELP_MSG
else:
    HELP_MSG = "[sᴘᴀᴍ ʙᴏᴛ](https://t.me/PBX_CHAT) Help Menu"


@Client.on_message(filters.command(["help"], prefixes=HANDLER))
async def _help(Legend: Client, message: Message):
    HELP_MSG = "ʜᴇʟᴘ ᴍᴇɴᴜ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @ll_THE_BAD_BOT_ll"
    if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
        await Legend.send_photo(
            message.chat.id,
            HELP_PIC,
            caption=HELP_MSG,
            reply_markup=InlineKeyboardMarkup(Data.HELP_MENU1),
        )
    elif ".mp4" in HELP_PIC.lower():
        await Legend.send_video(
            message.chat.id,
            HELP_PIC,
            caption=HELP_MSG,
            reply_markup=InlineKeyboardMarkup(Data.HELP_MENU1),
        )
    else:
        await Legend.send_message(
            message.chat.id,
            HELP_MSG,
            reply_markup=InlineKeyboardMarkup(Data.HELP_MENU1),
        )
      
