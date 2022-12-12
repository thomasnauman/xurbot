import discord
from discord.ext import commands
from datetime import datetime
import asyncio

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='!', intents =intents)

async def xur_task():
    await bot.wait_until_ready()

    # Get the #where-is-xur channel
    channel = discord.utils.get(bot.get_all_channels(), name="where-is-xur")

    while not bot.is_closed():
        # Get the current time
        now = datetime.utcnow()

        # Check if it's Friday at 12:05 PM
        if now.weekday() == 4 and now.hour == 12 and now.minute == 5:
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
            await channel.send(message)

            # Send image depending on planet location
            if planet_location == "Titan":
                with open("titan_image.png", "rb") as f:
                    await channel.send(file=discord.File(f))

            # Send message to encourage Guardians to visit Xur
            await channel.send("GO!!")

        # Sleep for 1 minute
        await asyncio.sleep(60)