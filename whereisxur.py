import discord
import requests
from discord.ext import commands
from item import Item

async def whereisxur(message):
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