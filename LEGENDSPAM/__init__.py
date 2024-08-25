import glob
import os
import time

from .Config import *
from .core import *

version = "v2"
group_username = "@PBX_CHAT"
start_time = time.time()


# Sudo Users
sudos = []
# full debugging
if SUDO_USERS:
    try:
        sudouser = SUDO_USERS
        print(sudouser)
        _list = []
        for x in sudouser:
            _list.append(int(x))
        sudos = _list
    except Exception as e:
        sudos = SUDO_USERS
        print(e)
else:
    print("sudo user")
