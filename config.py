import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5446861802:AAFmJ5pYhzjmsqTDXLLn1axv6MbZraA8lxk")
    API_ID = int(os.environ.get("API_ID", "19785832"))
    API_HASH = os.environ.get("API_HASH", "5a894d5786057b269caf4ae788d5ecc2")
    BOT_OWNER = os.environ.get("BOT_OWNER", "DeepKraL")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "youtubeVcproBot")
    PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "youtubevcmuzik")
    GROUP = os.environ.get("GROUP", "SohbetMiss") 
    PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1001259764610"))
