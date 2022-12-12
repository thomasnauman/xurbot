import discord
import requests
from discord.ext import commands
from item import Item
import datetime
from on_message import receive
from observe import observe

# Replace with your Discord bot token
DISCORD_BOT_TOKEN = "MTAxMDM3ODU5MzgyMzYyMTE3MA.GFxY8v.sKe13cxpWwB0VZ8gspumDR7fveB9-RmfsE4XrM"

# Replace with your Destiny 2 API key
DESTINY_API_KEY = "5f0c2efb72534d19a4edcba381f72e21"

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
    if message.author == client.user:
        return

    # Check if the message is "!xur"
    if message.content.lower() == "!xur":
        headers = {"X-API-Key": DESTINY_API_KEY}
        response = requests.get(XUR_URL, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()

            # Loop through the items in Xur's inventory and store their information in variables
            for item in data["Response"]["inventory"]["data"]["items"]:
                name = item["item"]["displayProperties"]["name"]
                slot = item["item"]["itemTypeAndTierDisplayName"]
                itemtype = item["item"]["itemTypeDisplayName"]

                # Create an Item class object with the parsed variables
                temp_item = Item(name, slot, itemtype)

                # Send a message to Discord with the item's information
                await message.channel.send(temp_item)


        else:
            # The request failed, so send an error message to Discord
            await message.channel.send("Sorry, I couldn't retrieve Xur's inventory. Please try again later.")

@client.command()
async def observe(message):
    # Get the current time
    now = datetime.datetime.now()

    # Check if it's Friday at Noon
    if now.weekday() == 4 and now.hour == 12:
        headers = {"X-API-Key": DESTINY_API_KEY}
        response = requests.get(XUR_URL, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()

            # Loop through the items in Xur's inventory and store their information in variables
            for item in data["Response"]["inventory"]["data"]["items"]:
                name = item["item"]["displayProperties"]["name"]
                slot = item["item"]["itemTypeAndTierDisplayName"]
                itemtype = item["item"]["itemTypeDisplayName"]

                # Create an Item class object with the parsed variables
                temp_item = Item(name, slot, itemtype)

                # Send a message to Discord with the item's information
                await message.channel.send(temp_item)


        else:
            # The request failed, so send an error message to Discord
            await message.channel.send("Sorry, I couldn't retrieve Xur's inventory. Please try again later.")

# Run the Discord bot
client.run(DISCORD_BOT_TOKEN)
