import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5546335075:AAGx-LPJSnWguyEpYt9UhUC0eFwnCMQMcNU")
    API_ID = int(os.environ.get("API_ID", "17690310"))
    API_HASH = os.environ.get("API_HASH", "b665fb267cd854696948a79928a41f05")
    BOT_OWNER = os.environ.get("BOT_OWNER", "memokra")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "blacketiketbot")
    PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME", "blackmuzikbotu")
    GROUP = os.environ.get("GROUP", "blackbotdestek") 
    PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID", "-1001599632490")
    OWNER_ID = os.environ.get("OWNER_ID", "5412574484")
