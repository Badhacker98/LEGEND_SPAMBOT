import glob
import os
import time

from .Config import *
from .core import *

version = "v2"
group_username = "@PBX_CHAT"
start_time = time.time()

# Sudo Users
SUDO_USERS = []
# full debugging
if SUDO_USERS_CONFIG:  # <-- dhyan rahe, agar aapka Config me SUDO_USERS_CONFIG naam ka variable hai
    try:
        sudouser = SUDO_USERS_CONFIG
        print(sudouser)
        _list = []
        for x in sudouser:
            _list.append(int(x))
        SUDO_USERS = _list
    except Exception as e:
        SUDO_USERS = SUDO_USERS_CONFIG
        print(e)
else:
    print("sudo user")
