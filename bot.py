import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print('Bot is ready!')

@client.command()
async def hello(ctx):
    await ctx.send(f"hello there, {ctx.author.mention}")

@client.command()
async def riddle(ctx):
    random = ["What has to be broken before you can use it?",
            "I’m tall when I’m young, and I’m short when I’m old. What am I?",
            "What month of the year has 28 days?",
            "What is full of holes but still holds water?",
            "What gets wet while drying?",
            " I shave every day, but my beard stays the same. What am I?",
            "The more of this there is, the less you see. What is it?"]
    await ctx.send(f"{random.choice(random)}")

client.run('OTEzNDk1NzgzODI1ODk5NTUx.YZ_VPg.zy8drq4O_UQeGKY9bxBSSJCtvd4')





