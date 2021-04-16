import StoreData
import discord
import requests
import asyncio
import traceback
from discord.ext import commands

class SteamAPI(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Cog loaded")

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Help", color=0x00ebff)
        embed.description = f"""
        **__ General Commands:__**\n
        **!ping** - See latency to the discord bot.\n
        **!servers** - See how many servers has this bot.\n
        **__Dead by Daylight Commands:__**\n
        **!stats [steam link]** - Note: Private steam profiles will not be visable.
        """
        embed.set_footer(text='Bot developed by ExeQ#0001')
        await ctx.send(embed=embed)

    @commands.command()
    async def servers(self, ctx):
        await ctx.send("Bot is in: " + str(len(self.client.guilds)) + " servers currently.")

def setup(client):
    client.add_cog(SteamAPI(client))
