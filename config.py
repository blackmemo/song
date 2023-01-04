import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5446861802:AAFV76i5ds4ewapkU7pGzWrA0aytHbyyPlw")
    API_ID = int(os.environ.get("API_ID", "10555778"))
    API_HASH = os.environ.get("API_HASH", "f3c3b702ebc181753d4b559b9b91d3f9")
    BOT_OWNER = os.environ.get("BOT_OWNER", "Youtube")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "youtubeVcproBot")
    PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "youtubemucis")
    GROUP = os.environ.get("GROUP", "yangazlargrup") 
    PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1001711522921"))
