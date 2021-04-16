import StoreData
import discord
import aiohttp
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
    async def stats(self, ctx, vanityURL):

        api_key = ""

        if vanityURL[-1] == '/':
            vanityURL = vanityURL[:-1]
        vanityURL = vanityURL.split('/')[-1]

        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.steampowered.com/ISteamUser/ResolveVanityURL/v1/?key={api_key}&vanityurl={vanityURL}&url_type=1") as r:
                if r.status == 200:
                    steamid_json = await r.json()
                else:
                    await ctx.send("Response Error on fetching steamid, Code: " + r.status)

        successcode = str(steamid_json['response']['success'])
        if successcode == '1':
            steamid = str(steamid_json['response']['steamid'])
        elif successcode == '42':
            steamid = vanityURL

        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={api_key}&steamids={steamid}") as r:
                if r.status == 200:
                    playersummaries_json = await r.json()
                else:
                    await ctx.send("Response Error on fetching player summaries, Code: " + r.status)

        if playersummaries_json['response']['players']:
            username = str(playersummaries_json['response']['players'][0]['personaname'])
            avatar = str(playersummaries_json['response']['players'][0]['avatarmedium'])
        else:
            await ctx.send("Could not find profile")
            return

        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v2/?key={api_key}&steamid={steamid}&appid=381210") as r:
                if r.status == 200:
                    gamestats_json = await r.json()
                else:
                    await ctx.send("Response Error on fetching gamedata, Code: " + r.status)

        statNames_dict = StoreData.getStatNames(gamestats_json, 'names')
        statValues_dict = StoreData.getStatNames(gamestats_json, 'values')

        survivorRank = StoreData.getStatNames(gamestats_json, 'survivor_rank')
        killerRank = StoreData.getStatNames(gamestats_json, 'killer_rank')
        statRankValues_dict = StoreData.getStatNames(gamestats_json, 'ranks')
        rankColor_dict = StoreData.GetRankColor()

        statSurvValues_dict = StoreData.getStatNames(gamestats_json, 'survivor')
        statKillerValues_dict = StoreData.getStatNames(gamestats_json, 'killer')

        embed = discord.Embed(title=f"{username} - General Stats", description="Please select Survivor or Killer to get more information.")
        embed.colour = discord.Colour.from_rgb(255, 0, 0)
        embed.set_image(url=avatar)
        embed.add_field(name=statNames_dict.get('DBD_BloodwebPoints'), value=str(f"{statValues_dict.get('DBD_BloodwebPoints'):,}"))

        msg = await ctx.send(embed=embed)
        await msg.add_reaction('<:DBD_Survivor:757030524932849726>')
        await msg.add_reaction('<:DBD_Killer:757030525927030844>')

        def check(reaction, user):
            return user == ctx.author and reaction.message.id == msg.id

        try:
            reaction, user = await self.client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('Request Timeout.')
        else:
            if str(reaction.emoji) == '<:DBD_Survivor:757030524932849726>':
                survivorEmbed = discord.Embed(title=f"{username} - Survivor Stats", description="----------------")
                survivorEmbed.add_field(name=statNames_dict.get('DBD_CamperSkulls'), value=statRankValues_dict.get('DBD_CamperSkulls'))
                survivorEmbed.colour = rankColor_dict.get(survivorRank)
                for i in statSurvValues_dict:
                    if statSurvValues_dict.get(i) != '0':
                        survivorEmbed.add_field(name=statNames_dict.get(i), value=str(f"{statSurvValues_dict.get(i):,}"))
                await ctx.send(embed=survivorEmbed)
            elif str(reaction.emoji) == '<:DBD_Killer:757030525927030844>':
                killerEmbed = discord.Embed(title=f"{username} - Killer Stats", description="----------------")
                killerEmbed.add_field(name=statNames_dict.get('DBD_KillerSkulls'), value=statRankValues_dict.get('DBD_KillerSkulls'))
                killerEmbed.colour = rankColor_dict.get(killerRank)
                for i in statKillerValues_dict:
                    if statKillerValues_dict.get(i) != '0':
                        killerEmbed.add_field(name=statNames_dict.get(i), value=str(f"{statKillerValues_dict.get(i):,}"))
                await ctx.send(embed=killerEmbed)

    @stats.error
    async def stats_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Steam profile link is needed to fetch player statistics.")
        else:
            traceback.print_exception(type(error), error, error.__traceback__)

def setup(client):
    client.add_cog(SteamAPI(client))
