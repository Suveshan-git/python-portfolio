import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the bot token securely
TOKEN = os.getenv("DISCORD_TOKEN")
