import pymongo
from pyrogram import Client, filters
from BADMUNDA.Config import HANDLER, OWNER_ID, MONGO_DB

# MongoDB setup
mongo_client = pymongo.MongoClient(MONGO_DB)
db = mongo_client["legend_spambot_db"]
sudo_col = db["sudo_users"]

# Helper: Get sudo users from DB, fallback to OWNER_ID if empty
def get_sudo_users():
    doc = sudo_col.find_one({"_id": "sudo_list"})
    if doc and "users" in doc and doc["users"]:
        return doc["users"]
    return [str(OWNER_ID)]

# Helper: Save sudo users to DB
def save_sudo_users(sudo_list):
    sudo_col.update_one({"_id": "sudo_list"}, {"$set": {"users": sudo_list}}, upsert=True)

# Helper: Check if a user is sudo
def is_sudo(user_id):
    return str(user_id) in get_sudo_users()

# Add SUDO
@Client.on_message(filters.command("addsudo", prefixes=HANDLER) & (filters.private | filters.group))
async def addsudo(client, message):
    if message.from_user.id != OWNER_ID:
        return await message.reply("✦ ɴᴏ ᴘᴇʀᴍɪssɪᴏɴ: ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴀᴄᴄᴇss ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ.")

    if not message.reply_to_message or not message.reply_to_message.from_user:
        return await message.reply("✦ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ.")

    target_id = str(message.reply_to_message.from_user.id)
    sudo_list = get_sudo_users()

    if target_id in sudo_list:
        return await message.reply("✦ ᴛʜɪs ᴜsᴇʀ ɪs ᴀʟʀᴇᴀᴅʏ ᴀ sᴜᴅᴏ ᴜsᴇʀ !!")

    sudo_list.append(target_id)
    save_sudo_users(sudo_list)

    await message.reply(f"✦ **ɴᴇᴡ sᴜᴅᴏ ᴜsᴇʀ** ➥ `{target_id}` ᴀᴅᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ.")

# Remove SUDO
@Client.on_message(filters.command("rmsudo", prefixes=HANDLER) & (filters.private | filters.group))
async def rmsudo(client, message):
    if message.from_user.id != OWNER_ID:
        return await message.reply("✦ ɴᴏ ᴘᴇʀᴍɪssɪᴏɴ: ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴀᴄᴄᴇss ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ.")

    if not message.reply_to_message or not message.reply_to_message.from_user:
        return await message.reply("✦ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ.")

    target_id = str(message.reply_to_message.from_user.id)
    sudo_list = get_sudo_users()

    if target_id not in sudo_list:
        return await message.reply("✦ ᴛʜɪs ᴜsᴇʀ ɪs ɴᴏᴛ ᴀ sᴜᴅᴏ ᴜsᴇʀ !!")
    if target_id == str(OWNER_ID):
        return await message.reply("✦ ᴏᴡɴᴇʀ ᴋᴏ sᴜᴅᴏ sᴇ ʜᴀᴛᴀ ɴᴀʜɪ sᴀᴋᴛᴇ!")

    sudo_list.remove(target_id)
    save_sudo_users(sudo_list)

    await message.reply(f"✦ **sᴜᴅᴏ ᴜsᴇʀ** ➥ `{target_id}` ʀᴇᴍᴏᴠᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ.")

# List SUDO
@Client.on_message(filters.command("sudolist", prefixes=HANDLER) & (filters.private | filters.group))
async def sudolist(client, message):
    if not (message.from_user.id == OWNER_ID or is_sudo(message.from_user.id)):
        return await message.reply("✦ ɴᴏ ᴘᴇʀᴍɪssɪᴏɴ.")

    sudo_list = get_sudo_users()
    text = "**Sudo Users List:**\n\n"
    for idx, user_id in enumerate(sudo_list, 1):
        text += f"{idx}. `{user_id}`\n"
    await message.reply(text)
