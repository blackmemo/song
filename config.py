import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    BOT_OWNER = os.environ.get("BOT_OWNER")
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME")
    GROUP = os.environ.get("GROUP")
    DURATION_LIMIT = int(os.environ.get("DURATION_LIMIT", "7"))
    PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID"))
