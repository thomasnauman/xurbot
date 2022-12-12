import requests
from discord.ext import commands
from bs4 import BeautifulSoup
import discord
import datetime

# Discord bot token
TOKEN = "<your-bot-token-here>"

# URL to scrape
URL = "https://www.whereisxur.com/"

client = discord.Client(intents=discord.Intents.default())
# Function to scrape data from the website
def scrape_data():
    # Make a GET request to the URL
    response = requests.get(URL)

    # Parse the HTML response
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the data we need in the HTML
    planet_location = soup.find('h2', class_='subheader').text
    location_spot = soup.find('h3', class_='subheader').text
    weapon = soup.find('p', class_='item-name').text
    weapon_type_and_slot = soup.find('p', class_='item-type').text
    hunter_armor = soup.find('div', id='Hunter').find('p', class_='item-name').text
    hunter_armor_slot = soup.find('div', id='Hunter').find('p', class_='item-type').text
    titan_armor = soup.find('div', id='Titan').find('p', class_='item-name').text
    titan_armor_slot = soup.find('div', id='Titan').find('p', class_='item-type').text
    warlock_armor = soup.find('div', id='Warlock').find('p', class_='item-name').text
    warlock_armor_slot = soup.find('div', id='Warlock').find('p', class_='item-type').text

    # Return the scraped data
    return (planet_location, location_spot,
            weapon, weapon_type_and_slot,
            hunter_armor, hunter_armor_slot,
            titan_armor, titan_armor_slot,
            warlock_armor, warlock_armor_slot)

# Send a message in the #where-is-xur channel with Xur's location and items
@bot.command()
async def whereisxur(ctx):
  # Get the current time
  now = datetime.datetime.now()

  # Check if it's Friday at noon
  if now.weekday() == 4 and now.hour == 12:
      message = (
          f"Hello, Guardians! Today, Xur is on {planet_location} in {location_spot}. "
          f"Here is what he is selling:\n"
          f"{weapon}\n"
          f"{weapon_type_and_slot}\n"
          f"{hunter_armor}\n"
          f"{hunter_armor_slot}\n"
          f"{titan_armor}\n"
          f"{titan_armor_slot}\n"
          f"{warlock_armor}\n"
          f"{warlock_armor_slot}"
      )
      await ctx.send(message)

      # Send image depending on planet location
      if planet_location == "Titan":
          with open("titan_image.png", "rb") as f:
              await ctx.send(file=discord.File(f))

      # Send message to encourage Guardians to visit Xur
      await ctx.send("GO!!")

  bot.run("YOUR_BOT_TOKEN_HERE")
