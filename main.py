import discord
from discord.ext import commands
from on_message import scan
from timecheck import observe

# Replace with your Discord bot token
DISCORD_BOT_TOKEN = ""

# Replace with your Destiny 2 API key
DESTINY_API_KEY = ""

# URL for Xur's inventory on Bungie's API
XUR_URL = "https://www.bungie.net/Platform/Destiny2/Vendors/4611686018467347905/Inventory"

# Create a new Discord client
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())


# This function runs when the bot connects to Discord
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


# This function runs when the bot receives a message on Discord
@client.event
async def on_message(message):
    await scan(message)

@client.command()
async def observe(message):
    await observe(message)

# Run the Discord bot
client.run(DISCORD_BOT_TOKEN)
