import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='!',intents=discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run("ODkwNjI1MDg0ODI0MzU5MDY0.YUyhPw.tTw3gmENQsZ7_8UhN6xg3oGvufM")