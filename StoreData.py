import discord
from range_key_dict import RangeKeyDict

def getStatNames(gamestats_json, selectList):

    pipsToRank_dict = RangeKeyDict({
    #Pips To Rank
    (85, 85) : 1,
    (80, 85) : 2,
    (75, 80) : 3,
    (70, 75) : 4,
    (65 ,70) : 5,
    (60, 65) : 6,
    (55, 60) : 7,
    (50, 55) : 8,
    (45, 50) : 9,
    (40, 45) : 10,
    (35, 40) : 11,
    (30, 35) : 12,
    (26, 30) : 13,
    (22, 26) : 14,
    (18, 22) : 15,
    (14, 18) : 16,
    (10, 14) : 17,
    (6, 10) : 18,
    (3, 6) : 19,
    (0, 3) : 20,
    })

    rankToPips_dict = {
    #Rank To Pips
    1 : 85,
    2 : 80,
    3 : 75,
    4 : 70,
    5 : 65,
    6 : 60,
    7 : 55,
    8 : 50,
    9 : 45,
    10 : 40,
    11 : 35,
    12 : 30,
    13 : 26,
    14 : 22,
    15 : 18,
    16 : 14,
    17 : 10,
    18 : 6,
    19 : 3,
    20 : 0,
    }

    statNames_dict = {
    'DBD_BloodwebPoints' : 'Bloodpoints Earned',
    # Survivor Stats
    'DBD_CamperSkulls' : 'Survivor Rank',
    'DBD_Escape' : 'Escapes (healthy/injured)',
    'DBD_EscapeKO' : 'Escapes (crawling)',
    'DBD_Camper9_Stat2' : 'Escapes (injured for half of the trial)',
    'DBD_DLC8_Camper_Stat1' : 'Escapes (downed once)',
    'DBD_EscapeThroughHatch' : 'Hatch Escapes (healthy/injured)',
    'DBD_Chapter12_Camper_Stat2' : 'Hatch Escapes (crawling)',
    'DBD_AllEscapeThroughHatch' : 'Hatch Escapes (with everyone)',
    'DBD_CamperNewItem' : 'Escaped (with new item)',
    'DBD_CamperEscapeWithItemFrom' : "Escaped (with someone else's item)",
    'DBD_CamperFullLoadout' : "Played with full loadout",
    'DBD_CamperMaxScoreByCategory' : "Perfect games (max in all categories)",
    'DBD_GeneratorPct_float' : "Equivalent generators repaired",
    'DBD_SkillCheckSuccess' : "Successful skill checks",
    'DBD_HealPct_float' : "Equivalent survivors healed",
    'DBD_Chapter14_Camper_Stat1' : "Protection hits",
    'DBD_Chapter15_Camper_Stat1' : "Survivors healed from dying to injured state",
    'DBD_Chapter17_Camper_Stat1' : "Items depleted",
    'DBD_Camper8_Stat2' : "Vaults while in chase",
    'DBD_Chapter12_Camper_Stat1' : "Wiggled from the killers grasp",
    'DBD_DLC3_Camper_Stat1' : "Hex totems cleansed",
    'DBD_DLC7_Camper_Stat2' : "Exit gates opened",
    'DBD_Chapter9_Camper_Stat1' : "Unhooked yourself",
    'DBD_Chapter10_Camper_Stat1' : "Hooks broken",
    'DBD_HitNearHook' : "Hit near a hook",
    'DBD_DLC7_Camper_Stat1' : "Chests searched",
    #Killer Stats
    'DBD_KillerSkulls' : 'Killer Rank',
    'DBD_KilledCampers' : 'Survivors Killed',
    'DBD_SacrificedCampers' : 'Sacrificed Survivors',
    'DBD_Chapter11_Slasher_Stat1' : 'Sacrificed all survivors before last generator',
    'DBD_DLC8_Slasher_Stat2' : 'Killed/Sacrificed after last generator',
    'DBD_SlasherFullLoadout' : 'Played with full loadout',
    'DBD_TrapPickup' : 'Bear trap catches',
    'DBD_UncloakAttack' : 'Uncloak attacks',
    'DBD_ChainsawHit' : 'Chainsaw hits',
    'DBD_SlasherChainAttack' : 'Blink attacks',
    'DBD_DLC3_Slasher_Stat1' : 'Phantasms triggered',
    'DBD_SlasherTierIncrement' : 'Evil Within tier ups',
    'DBD_DLC4_Slasher_Stat1' : 'Shocks',
    'DBD_DLC5_Slasher_Stat1' : 'Hatchets thrown',
    'DBD_DLC7_Slasher_Stat1' : 'Dream state',
    'DBD_DLC8_Slasher_Stat1' : 'Reverse bear traps placed',
    'DBD_Chapter16_Slasher_Stat1' : 'Cages of atonement',
    'DBD_Chapter17_Slasher_Stat1' : 'Lethal Rush hits',
    'DBD_DLC7_Slasher_Stat2' : 'Obsessions sacrificed',
    'DBD_Chapter12_Slasher_Stat1' : 'Survivors grabbed while repairing a gen',
    'DBD_Chapter15_Slasher_Stat2' : 'Survivors interrupted while cleansing a totem',
    'DBD_Chapter9_Slasher_Stat1' : 'Hit a survivor who dropped a pallet within a chase',
    'DBD_Chapter10_Slasher_Stat1' : 'Hit a survivor while carrying another',
    'DBD_Event1_Stat1' : 'Had 3 survivors hooked in the basement at same time',
    'DBD_Chapter14_Slasher_Stat1' : 'Hooked a survivor while 3 other survivors were injured'
    }

    statValues_dict = {
    'DBD_BloodwebPoints' : int(next(filter(lambda x: x['name'] == 'DBD_BloodwebPoints', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    }

    survivorRank = pipsToRank_dict[int(next(filter(lambda x: x['name'] == 'DBD_CamperSkulls', gamestats_json['playerstats']['stats']), dict()).get('value', '0'))]
    survivorTotalPips = int(next(filter(lambda x: x['name'] == 'DBD_CamperSkulls', gamestats_json['playerstats']['stats']), dict()).get('value', '0'))

    killerRank = pipsToRank_dict[int(next(filter(lambda x: x['name'] == 'DBD_KillerSkulls', gamestats_json['playerstats']['stats']), dict()).get('value', '0'))]
    killerTotalPips = int(next(filter(lambda x: x['name'] == 'DBD_KillerSkulls', gamestats_json['playerstats']['stats']), dict()).get('value', '0'))

    statRankValues_dict = {
    'DBD_CamperSkulls' : f"{survivorRank} (with {survivorTotalPips- rankToPips_dict.get(survivorRank)} pips)",
    'DBD_KillerSkulls' : f"{killerRank} (with {killerTotalPips - rankToPips_dict.get(killerRank)} pips)",
    }

    statSurvValues_dict = {
    # Survivor Stats
    'DBD_Escape' : int(next(filter(lambda x: x['name'] == 'DBD_Escape', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_EscapeKO' : int(next(filter(lambda x: x['name'] == 'DBD_EscapeKO', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_Camper9_Stat2' : int(next(filter(lambda x: x['name'] == 'DBD_Camper9_Stat2', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_DLC8_Camper_Stat1' : int(next(filter(lambda x: x['name'] == 'DBD_DLC8_Camper_Stat1', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_EscapeThroughHatch' : int(next(filter(lambda x: x['name'] == 'DBD_EscapeThroughHatch', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_Chapter12_Camper_Stat2' : int(next(filter(lambda x: x['name'] == 'DBD_Chapter12_Camper_Stat2', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_AllEscapeThroughHatch' : int(next(filter(lambda x: x['name'] == 'DBD_AllEscapeThroughHatch', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_CamperNewItem' : int(next(filter(lambda x: x['name'] == 'DBD_CamperNewItem', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_CamperEscapeWithItemFrom' : int(next(filter(lambda x: x['name'] == 'DBD_CamperEscapeWithItemFrom', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_CamperFullLoadout' : int(next(filter(lambda x: x['name'] == 'DBD_CamperFullLoadout', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_CamperMaxScoreByCategory' : int(next(filter(lambda x: x['name'] == 'DBD_CamperMaxScoreByCategory', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_GeneratorPct_float' : int(next(filter(lambda x: x['name'] == 'DBD_GeneratorPct_float', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_SkillCheckSuccess' : int(next(filter(lambda x: x['name'] == 'DBD_SkillCheckSuccess', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_HealPct_float' : int(next(filter(lambda x: x['name'] == 'DBD_HealPct_float', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_Chapter14_Camper_Stat1' : int(next(filter(lambda x: x['name'] == 'DBD_Chapter14_Camper_Stat1', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_Chapter15_Camper_Stat1' : int(next(filter(lambda x: x['name'] == 'DBD_Chapter15_Camper_Stat1', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_Chapter17_Camper_Stat1' : int(next(filter(lambda x: x['name'] == 'DBD_Chapter17_Camper_Stat1', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_Camper8_Stat2' : int(next(filter(lambda x: x['name'] == 'DBD_Camper8_Stat2', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_Chapter12_Camper_Stat1' : int(next(filter(lambda x: x['name'] == 'DBD_Chapter12_Camper_Stat1', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_DLC3_Camper_Stat1' : int(next(filter(lambda x: x['name'] == 'DBD_DLC3_Camper_Stat1', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_DLC7_Camper_Stat2' : int(next(filter(lambda x: x['name'] == 'DBD_DLC7_Camper_Stat2', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_Chapter9_Camper_Stat1' : int(next(filter(lambda x: x['name'] == 'DBD_Chapter9_Camper_Stat1', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_Chapter10_Camper_Stat1' : int(next(filter(lambda x: x['name'] == 'DBD_Chapter10_Camper_Stat1', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_HitNearHook' : int(next(filter(lambda x: x['name'] == 'DBD_HitNearHook', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_DLC7_Camper_Stat1' : int(next(filter(lambda x: x['name'] == 'DBD_DLC7_Camper_Stat1', gamestats_json['playerstats']['stats']), dict()).get('value', '0'))
    }

    statKillerValues_dict = {
    #Killer Stats
    'DBD_SacrificedCampers' : int(next(filter(lambda x: x['name'] == 'DBD_SacrificedCampers', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_KilledCampers' : int(next(filter(lambda x: x['name'] == 'DBD_KilledCampers', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_Chapter11_Slasher_Stat1' : int(next(filter(lambda x: x['name'] == 'DBD_Chapter11_Slasher_Stat1', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_DLC8_Slasher_Stat2' : int(next(filter(lambda x: x['name'] == 'DBD_DLC8_Slasher_Stat2', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_SlasherFullLoadout' : int(next(filter(lambda x: x['name'] == 'DBD_SlasherFullLoadout', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_DLC7_Slasher_Stat2' : int(next(filter(lambda x: x['name'] == 'DBD_DLC7_Slasher_Stat2', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_Chapter12_Slasher_Stat1' : int(next(filter(lambda x: x['name'] == 'DBD_Chapter12_Slasher_Stat1', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_Chapter15_Slasher_Stat2' : int(next(filter(lambda x: x['name'] == 'DBD_Chapter15_Slasher_Stat2', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_Chapter9_Slasher_Stat1' : int(next(filter(lambda x: x['name'] == 'DBD_Chapter9_Slasher_Stat1', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_Chapter10_Slasher_Stat1' : int(next(filter(lambda x: x['name'] == 'DBD_Chapter10_Slasher_Stat1', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_Event1_Stat1' : int(next(filter(lambda x: x['name'] == 'DBD_Event1_Stat1', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_Chapter14_Slasher_Stat1' : int(next(filter(lambda x: x['name'] == 'DBD_Chapter14_Slasher_Stat1', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_TrapPickup' : int(next(filter(lambda x: x['name'] == 'DBD_TrapPickup', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_UncloakAttack' : int(next(filter(lambda x: x['name'] == 'DBD_UncloakAttack', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_ChainsawHit' : int(next(filter(lambda x: x['name'] == 'DBD_ChainsawHit', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_SlasherChainAttack' : int(next(filter(lambda x: x['name'] == 'DBD_SlasherChainAttack', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_DLC3_Slasher_Stat1' : int(next(filter(lambda x: x['name'] == 'DBD_DLC3_Slasher_Stat1', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_SlasherTierIncrement' : int(next(filter(lambda x: x['name'] == 'DBD_SlasherTierIncrement', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_DLC4_Slasher_Stat1' : int(next(filter(lambda x: x['name'] == 'DBD_DLC4_Slasher_Stat1', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_DLC5_Slasher_Stat1' : int(next(filter(lambda x: x['name'] == 'DBD_DLC5_Slasher_Stat1', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_DLC7_Slasher_Stat1' : int(next(filter(lambda x: x['name'] == 'DBD_DLC7_Slasher_Stat1', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_DLC8_Slasher_Stat1' : int(next(filter(lambda x: x['name'] == 'DBD_DLC8_Slasher_Stat1', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_Chapter16_Slasher_Stat1' : int(next(filter(lambda x: x['name'] == 'DBD_Chapter16_Slasher_Stat1', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    'DBD_Chapter17_Slasher_Stat1' : int(next(filter(lambda x: x['name'] == 'DBD_Chapter17_Slasher_Stat1', gamestats_json['playerstats']['stats']), dict()).get('value', '0')),
    }

    if selectList == 'names':
        return statNames_dict
    elif selectList == 'values':
        return statValues_dict
    elif selectList == 'ranks':
        return statRankValues_dict
    elif selectList == 'survivor':
        return statSurvValues_dict
    elif selectList == 'killer':
        return statKillerValues_dict
    elif selectList == 'survivor_rank':
        return survivorRank
    elif selectList == 'killer_rank':
        return killerRank

def GetRankColor():
    rankColor_dict = RangeKeyDict({
    (1, 5) : discord.Colour.from_rgb(255, 0, 0),
    (5, 9) : discord.Colour.from_rgb(128, 0, 255),
    (9, 13) : discord.Colour.from_rgb(0, 153, 51),
    (13, 17) : discord.Colour.from_rgb(204, 204, 0),
    (17, 21) : discord.Colour.from_rgb(255, 153, 0)
    })
    return rankColor_dict
