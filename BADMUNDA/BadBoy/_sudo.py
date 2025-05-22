import json
from pyrogram import filters, Client
from pyrogram.types import Message
from .. import SUDO_USERS, OWNER_ID
from BADMUNDA.Config import *

SUDO_FILE = "sudo_users.json"

def save_sudo_users():
    # Save unique sudo users (avoid duplicates)
    with open(SUDO_FILE, "w") as f:
        json.dump(list(set(SUDO_USERS)), f)

def load_sudo_users():
    global SUDO_USERS
    try:
        with open(SUDO_FILE, "r") as f:
            SUDO_USERS.clear()
            SUDO_USERS.extend(json.load(f))
    except FileNotFoundError:
        # First time run: just ensure OWNER_ID is in sudo
        if OWNER_ID not in SUDO_USERS:
            SUDO_USERS.append(OWNER_ID)
        save_sudo_users()

# ==== Ensure sudo list is loaded on import ====
load_sudo_users()

@Client.on_message(filters.command(["addsudo"], prefixes=HANDLER))
async def addsudo(client: Client, message: Message):
    try:
        if not message.reply_to_message:
            if len(message.command) != 2:
                await message.reply_text("Reply to a user's message or give username/user_id.")
                return
            user = message.text.split(None, 1)[1]
            if "@" in user:
                user = user.replace("@", "")
            user = await client.get_users(user)
            if user.id in SUDO_USERS:
                await message.reply_text(f"{user.mention} is already a sudo user.")
                return
            SUDO_USERS.append(user.id)
            save_sudo_users()
            await message.reply_text(f"Added **{user.mention}** to Sudo Users.")
            return

        # If reply
        reply_user = message.reply_to_message.from_user
        if reply_user.id in SUDO_USERS:
            await message.reply_text(f"{reply_user.mention} is already a sudo user.")
            return
        SUDO_USERS.append(reply_user.id)
        save_sudo_users()
        await message.reply_text(f"Added **{reply_user.mention}** to Sudo Users.")
    except Exception as e:
        await message.reply_text(f"**ERROR:** `{e}`")
        return

@Client.on_message(filters.command(["rmsudo"], prefixes=HANDLER))
async def rmsudo(client: Client, message: Message):
    try:
        if not message.reply_to_message:
            if len(message.command) != 2:
                await message.reply_text("Reply to a user's message or give username/user_id.")
                return
            user = message.text.split(None, 1)[1]
            if "@" in user:
                user = user.replace("@", "")
            user = await client.get_users(user)
            if user.id not in SUDO_USERS:
                await message.reply_text(f"**{user.mention}** is not a part of Bot's Sudo.")
                return
            SUDO_USERS.remove(user.id)
            save_sudo_users()
            await message.reply_text(f"Removed **{user.mention}** from Bot's Sudo User")
            return

        reply_user = message.reply_to_message.from_user
        if reply_user.id not in SUDO_USERS:
            await message.reply_text(f"**{reply_user.mention}** is not a part of Bot's Sudo.")
            return
        SUDO_USERS.remove(reply_user.id)
        save_sudo_users()
        await message.reply_text(f"Removed **{reply_user.mention}** from Bot's Sudo User")
    except Exception as e:
        await message.reply_text(f"**ERROR:** `{e}`")
        return

@Client.on_message(filters.command(["sudolist"], prefixes=HANDLER))
async def sudolist(client: Client, message: Message):
    users = SUDO_USERS
    ex = await message.reply("`Processing...`")
    if not users:
        await ex.edit("No Users have been set yet")
        return
    sudo_list = "**Sudo Users:**\n"
    count = 0
    for i in users:
        count += 1
        sudo_list += f"**{count} -** `{i}`\n"
    await ex.edit(sudo_list)
    return
    
