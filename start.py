import os

from SukhPB.startup import *

os.system("clear")


vars = """
APP_ID=
API_HASH=
SUDO_USERS=
START_PIC=
START_MESSAGE=
HELP_PIC=
PING_PIC=
LOG_CHANNEL=
HANDLER=
BOT_TOKEN=
BOT_TOKEN2=
BOT_TOKEN3=
BOT_TOKEN4=
BOT_TOKEN5=
BOT_TOKEN6=
BOT_TOKEN7=
BOT_TOKEN8=
BOT_TOKEN9=
BOT_TOKEN10=
BOT_TOKEN11=
BOT_TOKEN12=
BOT_TOKEN13=
BOT_TOKEN14=
BOT_TOKEN10=
BOT_TOKEN11=
BOT_TOKEN12=
BOT_TOKEN13=
BOT_TOKEN14=
BOT_TOKEN15=
BOT_TOKEN16=
BOT_TOKEN17=
BOT_TOKEN18=
BOT_TOKEN19=
BOT_TOKEN20=
BOT_TOKEN21=
BOT_TOKEN22=
BOT_TOKEN23=
BOT_TOKEN24=
BOT_TOKEN25=
"""


botspam = input(f"Want to fill vars ? if yes type Y/yes else press enter: ")
if botspam.lower() in ["y", "yes"]:
    if not os.path.exists(".env"):
        y = open(".env", "w")
        y.write(vars)
        y.close()
        os.system("clear")
        BadmundaStartUP()
    elif os.path.exists(".env"):
        f = open(".env")
        check = f.read()
        print(check)
        f.close()
        check_again()
        if not len(lines) == 35:
            os.system("rm -rf .env")
            y = open(".env", "w")
            y.write(vars)
            y.close()
            os.system("clear")
            BadmundaStartUP()
        else:
            os.system("clear")
            BadmundaStartUP()
else:
    os.system("clear")
    os.system("python3 -m BADMUNDA")
  
