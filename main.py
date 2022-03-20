import discord

import commands
import config


client = discord.Client()


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!hello":
        await commands.hello(message)

    if message.content == "!ooh":
        await commands.ooh(message)

    if message.content == "!breadline":
        await commands.breadline(message)

    if message.content == "!breadfact":
        await commands.breadfact(message)

    if message.content == "!list":
        await commands.list(message)

    if message.content.startswith("!accuse"):
        await commands.accuse(message)

    if message.content.startswith("!conspiracy"):
        await commands.conspiracy(message)

    if message.content.startswith("!flee"):
        await commands.flee(message)

    if message.content == "!athensss":
        await commands.athensss(message)

client.run(config.discord["token"])
