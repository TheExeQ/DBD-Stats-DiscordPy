import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '-', case_insensitive=True)
BOTTOKEN = "";

client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f"!help | Currently Serving: {str(len(client.guilds))} Servers"))
    print("Bot is ready!")
    print(f"Logged in as {client.user.name}")
    print(f"Currently on {str(len(client.guilds))} servers!")
    print("--------------------------------")

@client.event
async def on_guild_join(guild):
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f"!help | Currently Serving: {str(len(client.guilds))} Servers"))

@client.event
async def on_guild_remove(guild):
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f"!help | Currently Serving: {str(len(client.guilds))} Servers"))

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong!\nyour ping is {round(client.latency * 1000)}ms")

@client.command()
async def load(ctx, extension):
    if str(ctx.author.id) == '155034937739837440':
        client.load_extension(f"cogs.{extension}")
        print(f"loaded: {extension}")

@client.command()
async def unload(ctx, extension):
    if str(ctx.author.id) == '155034937739837440':
        client.unload_extension(f"cogs.{extension}")
        print(f"unloaded: {extension}")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(BOTTOKEN)
