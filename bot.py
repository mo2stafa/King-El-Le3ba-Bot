from discord.ext import commands
from dotenv import load_dotenv
import discord
import os
import firebase_admin
from firebase_admin import credentials, db


intents = discord.Intents.all()
load_dotenv()
TOKEN = os.environ.get('TOKEN', 3)


DBLINK = os.environ.get('DBLINK', 3)


cred = credentials.Certificate(
    "king-el-le3ba-bot-firebase-adminsdk.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': DBLINK
})


bot = commands.Bot(command_prefix="m-", intents=intents)


# get the data
data = db.reference("/")


# node for each server you are in
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    # loop through every guild and create a new key for it
    # only run once if necessary
    # for guild in bot.guilds:
    #     # loop through every member and create a new key for them
    #     member_object = {}
    #     for member in guild.members:
    #       member_object[member.id] = 0
    #     data.child(str(guild.id)).set(member_object)


# on guild join, create a new key for it
@bot.event
async def on_guild_join(guild):
    # loop through every member and create a new key for it
    member_object = {}
    for member in guild.members:
        # Skip the bot itself
        if member.bot:
            continue

        member_object[member.id] = 0
    data.child(str(guild.id)).set(member_object)


# change score
@bot.command(name="cs")
async def cs(ctx, amount: int):
    # Get the guild id and member id
    guild_id = str(ctx.guild.id)
    member_id = str(ctx.author.id)

    # Check if the member object exists
    if data.child(guild_id).child(member_id).get() is None:
        # Create a new member object with an initial score of 0
        data.child(guild_id).child(member_id).set(0)

    # Get the member's current score
    member_object = data.child(guild_id).child(member_id).get()

    # Modify the score by the specified amount
    member_object += amount

    # Update the member's score in the database
    data.child(guild_id).child(member_id).set(member_object)

    # Provide feedback to the user
    await ctx.send(f"{ctx.author.mention}, your score has been changed to {member_object}.")


# create a leaderboard command
@bot.command()
async def leaderboard(ctx):
    # get leaderboard data
    leaderboard_data = data.child(str(ctx.guild.id)).get()
    # sort the leaderboard data
    leaderboard_data = dict(
        sorted(leaderboard_data.items(), key=lambda item: item[1], reverse=True))

    embed = discord.Embed(title="Leaderboard", color=discord.Color.blue())
    embed.set_thumbnail(
        url="https://cdn-icons-png.flaticon.com/512/5987/5987898.png")

    # limit the leaderboard to 10 entries
    count = 0
    # Add fields to the embed for each leaderboard entry
    for index, entry in enumerate(leaderboard_data, start=1):
        count += 1
        # get the name of the member
        name = bot.get_user(int(entry)).name
        # get the score of the member
        score = leaderboard_data[entry]
        # add the field to the embed
        embed.add_field(name=f"#{index} - {name}",
                        value=f"Score: {score}", inline=False)
        if count == 10:
            break

    await ctx.send(embed=embed)


# create a command that shows the user's score in the leaderboard
@bot.command()
async def me(ctx):
    # get the guild id
    guild_id = str(ctx.guild.id)
    # get the member id
    member_id = str(ctx.author.id)
    # check if member object exists
    if data.child(guild_id).child(member_id).get() == None:
        # create a new member object
        data.child(guild_id).child(member_id).set(0)
    # get the member object
    member_object = data.child(guild_id).child(member_id).get()
    # get members name
    name = bot.get_user(int(member_id)).name
    # create the embed
    embed = discord.Embed(title=name, color=discord.Color.blue())
    # embed icon
    embed.set_thumbnail(url=ctx.author.avatar)
    # embed score
    embed.add_field(name=member_object, value="", inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def reset(ctx):
    guild_id = str(ctx.guild.id)

    # Get a list of all members in the guild
    for member in ctx.guild.members:
        member_id = str(member.id)
        # Skip the bot itself
        if member.bot:
            continue

        # Reset each member's score to 0
        data.child(guild_id).child(member_id).set(0)

    # Provide feedback to the user
    await ctx.send("All scores have been reset to 0.")


@bot.command()
async def ping(ctx):
    await ctx.send("pong")

bot.run(TOKEN)
