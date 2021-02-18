#!/usr/bin/env python
#bot.py
import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
#voice = discord.VoiceClient(client, "General")


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    moise = [
        'Moise är svart ngl ngl',
        'Min snorre är enorm',
        (
            'mowshe'

        ),  
    ]

    if message.content == 'moise':
        #voice.connect(True, 1000)
        response = random.choice(moise)
        await message.channel.send(response)

    if message.content == 'join':
        pass

await connect(*, timeout=60.0, reconnect=True, cls=<class 'discord.voice_client.VoiceClient'> )


#@client.command()
#async def join(ctx):
#    channel = ctx.author.voice.channel
#    await channel.connect()
#@client.command()
#async def leave(ctx):
#    await ctx.voice_client.disconnect()

#voice.

client.run(TOKEN)
