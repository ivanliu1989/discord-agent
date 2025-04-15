import discord
import time
import asyncio
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

last_messages = 5
token = os.getenv("DISCORD_TOKEN")
print(token)

# Set up intents
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    channels = ["general"]

    if str(message.channel) in channels:
        if message.content == "!history":
            messages = await message.channel.history(limit=last_messages).flatten()
            messages.reverse()

            await message.channel.send(f"Last {last_messages} messages:")
            await message.channel.send([message.content for message in messages])

client.run(token)