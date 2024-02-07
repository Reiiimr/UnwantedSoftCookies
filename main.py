import discord
import os

from keep_alive import keep_alive
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

keep_alive()
token = os.environ.get("TOKEN")
client.run(os.getenv("TOKEN"))


@client.event
async def on_ready():
    print('Hello, I am {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'hi':
        await message.channel.send('hello')

client.run(os.getenv("TOKEN"))
