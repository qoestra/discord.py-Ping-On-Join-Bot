#  ----- IMPORTS -----
import discord
from discord.ext import commands


#  ----- VARIABLES -----
prefix = "!"
TOKEN = ""
poj_channels = [11111111111111, 22222222222222]
poj_delete_time = "1"


#  ----- INTENTS -----
intents = discord.Intents.all()
client = commands.Bot(command_prefix=prefix, intents=intents, help_command=None)


#  ----- ON READY -----
@client.event
async def on_ready():
    print("Bot Started.")


#  ----- POJ -----
@client.event
async def on_member_join(member):
    channel = client.get_channel(poj_channels)
    if channel:
        await channel.send(member.mention, delete_after = poj_delete_time)


#  ----- UNKONOWN COMMAND ERROR -----
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.message.delete()
        await ctx.send("**UNKNOWN COMMAND!", delete_after=3)

#  ----- BOT START -----
client.run(TOKEN)
