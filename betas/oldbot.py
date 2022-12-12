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
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        # The request failed, so send an error message to Discord
        await message.channel.send("Sorry, I couldn't retrieve Xur's inventory. Please try again later.")


# Create the Discord bot
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# This function runs when the bot connects to Discord
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# Command that sends Xur's inventory to the Discord channel
# noinspection PyTypeChecker
@bot.command()
async def xur(ctx):
    # Get Xur's inventory data from the API
    xur_data = get_data(XUR_API_ENDPOINT)

    # Parse the relevant information from the API response
    xur_location = xur_data["Response"]["sales"]["data"]["sales"][0]["location"]
    xur_inventory = xur_data["Response"]["sales"]["data"]["saleItems"]

    # Print the introductory message
    await ctx.send(f"Hello Guardians! Today, Xur is on {xur_location} and is offering the following:")
    await ctx.send()

    # Print the details of each item in Xur's inventory
    for item in xur_inventory:
        await ctx.send(item["item"]["displayProperties"]["name"])
        await ctx.send(item["item"]["itemTypeAndTierDisplayName"])
        await ctx.send()

    # Display an image of Xur's location
    if xur_location == "EDZ":
        with open("at_edz.jpg.png", "rb") as f:
            # noinspection PyTypeChecker
            await ctx.send(file=discord.File(f))
    elif xur_location == "Nessus":
        with open("at_nessus.jpg.png", "rb") as f:
            await ctx.send(file=discord.File(f))
    elif xur_location == "Tower":
        with open("at_tower.jpg.png", "rb") as f:
            await ctx.send(file=discord.File(f))
    # Print the final message
    await ctx.send("GO!")


# Run the bot
bot.run("MTAxMDM3ODU5MzgyMzYyMTE3MA.G7A6wk.koei7pg9jEtjiOGB2SY4kU0k3k14HzmYP4sfiE")
