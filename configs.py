import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 26921911))
    API_HASH = os.environ.get("API_HASH", "d05329c36c0e4b8ffce7dacb3720d481")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "LinkSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -1001818830136))
    BOT_USERNAME = os.environ.get("mdisk_movie_searching_bot")
    BOT_OWNER = int(os.environ.get("5569871088"))
    DATABASE_URL = os.environ.get("DATABASE_URL")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", -1001824048080)
    ABOUT_BOT_TEXT = """<b>This is Link Search Bot.
    
    
    
π€ My Name: <a href='https://youtube.com/@GreyMattersBot'>Link Search Bot</a>

π Language : <a href='https://www.python.org'> Python V3</a>

π Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

π‘ Server: <a href='koyeb.com'>Koyeb</a>

π¨βπ» Created By: <a href='https://t.me/GreyMatter_Bot'>GreyMatter's Bot</a></b>
"""

    ABOUT_HELP_TEXT = """<b>π¨βπ» Creator : <a href='https://t.me/GreyMatter_Bot'>GreyMatter's Bot</a>
If You Want Your Own Bot Like This Then You Can Contact Our Creator.</b>
"""

    HOME_TEXT = """
<b>Hey! {}π,

I'm Link Search Bot.π€

I Can Search π What You Wantβ

<a>Made With β€ By @GreyMatter_Bots</a></b>
"""


    START_MSG = """
<b>Hey! {}π,

I'm Link Search Bot.π€

I Can Search π What You Wantβ

<a>Made With β€ By @GreyMatter_Bots</a></b>
"""

