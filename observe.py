import discord
import requests
from discord.ext import commands
from item import Item
import datetime
from whereisxur import whereisxur

async def observe(message):
  # Get the current time
  now = datetime.datetime.now()

  # Check if it's Friday at Noon
  if now.weekday() == 4 and now.hour == 12:
      whereisxur(message)