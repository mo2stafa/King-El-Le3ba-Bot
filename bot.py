from discord.ext import commands
from dotenv import load_dotenv
import discord
import os


intents = discord.Intents.all()
load_dotenv()
TOKEN = os.environ.get('TOKEN', 3)
print(TOKEN)
bot = commands.Bot(command_prefix="m", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def ping(ctx):
    await ctx.send("pong")
    
bot.run(TOKEN)
