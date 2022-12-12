import discord
import requests
from discord.ext import commands
from item import Item
import datetime
from whereisxur import whereisxur

async def on_message(message):
    if message.author == client.user:
        return

    # Check if the message is "!xur"
    if message.content.lower() == "!xur":
        whereisxur(message)