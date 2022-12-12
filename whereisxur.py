import requests
from item import Item
import discord

DESTINY_API_KEY = "5f0c2efb72534d19a4edcba381f72e21"

XUR_URL = "https://www.bungie.net/Platform/Destiny2/Vendors/4611686018467347905/Inventory"


async def whereisxur(message):
    global full_location, image_file
    headers = {"X-API-Key": DESTINY_API_KEY}
    response = requests.get(XUR_URL, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Search data for Xur's location and assign it to a variable
        xur_location = data["Response"]["Location"]

        if xur_location == "Earth":
            full_location = "on the EDZ in Winding Cove"
        if xur_location == "Nessus":
            full_location = "on Nessus at the Watcher's Grave"
        if xur_location == "Tower":
            full_location = "in the Tower at the Hangar"

        await message.channel.send(f"Hello Guardians! Today, Xur is {full_location}. Here is what he is offering:")

        # Loop through the items in Xur's inventory and store their information in variables
        for item in data["Response"]["inventory"]["data"]["items"]:
            name = item["item"]["displayProperties"]["name"]
            slot = item["item"]["itemTypeAndTierDisplayName"]
            itemtype = item["item"]["itemTypeDisplayName"]

            # Create an Item class object with the parsed variables
            temp_item = Item(name, slot, itemtype)

            # Send a message to Discord with the item's information
            await message.channel.send(temp_item)

        # Determines which image file to send depending on what Xur's location is
        if xur_location == "Earth":
            image_file = "Locations/at_edz.jpg"
        if xur_location == "Nessus":
            image_file = "Locations/at_nessus.png"
        if xur_location == "Tower":
            image_file = "Locations/at_tower.jpg"

        # Sends the appropriate image for Xur's location
        with open(image_file, "rb") as f:
            await message.channel.send(file=discord.File(f))

        # Sends a message encouraging the reader to go to Xur, thus signifying the whereisxur operation is complete
        await message.channel.send("GO!")

    else:
        # The request failed, so send an error message to Discord
        await message.channel.send("Sorry, I couldn't retrieve Xur's inventory. Please try again later.")
