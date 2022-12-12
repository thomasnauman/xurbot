import discord
import requests
from discord.ext import commands
from item import Item
import datetime
from on_message import on_message
from observe import observe

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
    on_message(message)

@client.command()
async def observe(message):
    obserbe(message)

# Run the Discord bot
client.run(DISCORD_BOT_TOKEN)
