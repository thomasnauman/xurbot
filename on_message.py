import discord
from discord.ext import commands
from whereisxur import whereisxur

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

async def scan(message):
    if message.author == client.user:
        return

    # Check if the message is "!xur"
    if message.content.lower() == "!xur":
        await whereisxur(message)
