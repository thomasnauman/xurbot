import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import datetime

# Discord bot token
TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# Discord bot prefix
PREFIX = "!xur"

# URL of "whereisxur.com"
XUR_URL = "https://whereisxur.com/"

# Create a new Discord bot
bot = commands.Bot(command_prefix=PREFIX)

# Send a message in the #where-is-xur channel with Xur's location and items
@bot.command()
async def whereisxur(ctx):
  # Get the current time
  now = datetime.datetime.now()

  # Check if it's Friday at noon
  if now.weekday() == 4 and now.hour == 12:
    # Scrape data from "whereisxur.com"
    page = requests.get(XUR_URL)
    soup = BeautifulSoup(page.text, "html.parser")

    # Parse data from the page
    planet_location = soup.find("h1", class_="subtitle").text
    location_spot = soup.find("h2", class_="subtitle").text
    items = soup.find_all("div", class_="item")

    # Create the message
    message = "Hello, Guardians! Today, Xur is on {} in {}. Here is what he is selling.\n\n".format(planet_location, location_spot)
    for item in items:
      name = item.find("h3").text
      type_and_slot = item.find("h4").text
      message += "{}\n{}\n\n".format(name, type_and_slot)

    # Send the message
    await ctx.send(message)

    # Send the picture depending on the planet location
    if planet_location == "Tower":


