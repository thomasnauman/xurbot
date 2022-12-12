import requests
from discord.ext import commands
import discord

# API endpoint for Xur's inventory
XUR_API_ENDPOINT = "https://www.bungie.net/Platform/Destiny2/Vendors/?components=402"


# Helper function to make API requests
BUNGIE_API_KEY = "5f0c2efb72534d19a4edcba381f72e21"

def get_data(endpoint):
    headers = {"X-API-Key": BUNGIE_API_KEY}
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()



# Create the Discord bot
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


# Command that sends Xur's inventory to the Discord channel
@bot.command()
async def xurfinder(ctx):
    await ctx.send("Hello World!")


# Run the bot
bot.run("MTAxMDM3ODU5MzgyMzYyMTE3MA.G7A6wk.koei7pg9jEtjiOGB2SY4kU0k3k14HzmYP4sfiE")