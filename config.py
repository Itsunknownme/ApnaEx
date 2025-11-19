import os
from os import getenv

# ------------------------------------------------
# Basic Bot Configuration (Environment Variables)
# ------------------------------------------------

API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
BOT_TEXT = "EXTRACTOR"

OWNER_ID = int(os.environ.get("OWNER_ID", ""))
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

# Optional Force Join Channel
# CHANNEL_ID2 = int(os.environ.get("CHANNEL_ID2", ""))

# Database
MONGO_URL = os.environ.get("MONGO_URL", "")

# Logging Channels
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", ""))

# ------------------------------------------------
# External API Keys / Other Settings
# ------------------------------------------------

UNSPLASH_ACCESS_KEY = "RabDRmuXXBobanmwwbvpP5LwoG4J8ox34y5Sstz-9jk"
UNSPLASH_QUERY = "animal baby"

# Thumbnail
THUMB_URL = os.environ.get(
    "THUMB_URL",
    "https://josephscollege.ac.in/wp-content/uploads/2022/04/1.jpg"
)
