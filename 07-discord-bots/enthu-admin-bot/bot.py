import discord
from discord.ext import commands
from utils.config import TOKEN
import asyncio

# Enable necessary Discord intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

# Disable default help command to use your custom one
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

# Bot ready event
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")

# Async function to load cogs and start bot
async def main():
    async with bot:
        await bot.load_extension("cogs.help")  # Load help command
        await bot.start(TOKEN)

# Run the main bot function
if __name__ == "__main__":
    asyncio.run(main())
