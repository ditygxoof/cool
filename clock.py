import discord

TOKEN = "OTU4OTA3MjcyNTk0MDc5Nzg0.YkUJ_Q.aAcchQNT9FgCv4Nid-jV1YMGy74"

client = discord.Client()

@client.event
async def on_ready():
    print("{0.user} is online!".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith("hi") or message.contentstartswith("hello"):
        await message.channel.send("YOOOOOOO")