import glob
import os
import time

from .Config import *
from .core import *

version = "v2"
group_username = "@PBX_CHAT"
start_time = time.time()

# Sudo Users
SUDO_USERS = SUDO_USER
SUDO_USER.append(OWNER_ID)

# Load sudo users from file on startup
from BADMUNDA.BadBoy._sudo import load_sudo_users
load_sudo_users()
