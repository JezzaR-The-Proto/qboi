#=-=-=-=-=-=-=-= Changelog =-=-=-=-=-=-=-=
#v0.23 - removed a line that crashed the .js and added changelog
#v0.24 - added &bitrate
#v0.25 - added &neil and &christopher
#v0.26 - added &qualitybot and &qualitybotv2
#v0.27 - updated &helps
#v0.28 - removed &helps
#v0.29 - added &kurwa
#v0.30 - changed prefix to &
#v0.31 - just testing
#v0.32 - changed &ping to actual ping command and removed test
#v0.33 - fixed &ping 
#v0.34 - changed join message
#v0.35 - added real &helpme
#v0.36 - huge &helpme overhall
#v0.37 - forgot to save v36...
#v0.38 - more h
#v0.39 - less h
#v0.40 - added the classic &helpme back until i get embed perms.
#v0.41 - didnt update v40 changelog...
#v0.42 - &helpme spams every command and breaks everything. Removed.
#v0.43 - added ms to &ping and removed some unnessasary lines in &helpme.
#v0.44 - added &creeper.							aw man
#v0.45 - fixed some grammar in &creeper and added it to &helpme
#v0.46 - removed &creeper - caused too much lag
#v0.47 - enabled &helpme
#v0.48 - removed &creeper from help
#v0.49 - added needed perms for &kick
#v0.50 - added needed perms for &ban and updated needed perms for &kick
#v0.51 - added console logs to each command.
#v0.52 - bug fixes
#v0.53 - moar bug fixes
#v0.54 - meme release
#v0.55 - updated meme release
#v0.56 - mem release broke last time
#v0.58 - creeper aw man
#v0.63 - undo mem release
#v0.65 - fixing pushing to server
#v0.66 - update &helpme
#v0.67 - &creeper now embed
#v0.68 - &creeper embed working
#v0.69 - hehe 69 also creeperawman very small
#v0.72 - &creeper actually works
#v0.74 - &rawr oh god help me
#v0.75 - slight &rawr update
#v0.76 - removed one darn space from uwuSoWarm
#v0.77 - &rawr now just responds to all messages with rawr in them.
#v1.04 - Python now because fuck js


import discord, logging, time, random
from discord.ext import commands, tasks
from itertools import cycle

prefix = "&"
client = commands.Bot(command_prefix = prefix)
status = cycle(["Qualityboi","Watching for commands &helpme","Ready for action!"])
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
client.remove_command("help")

creeperAwMan = discord.Embed(title="Creeper",description="Aw man", inline=False)
creeperAwMan.add_field(name="So we back in the mine",value="got our pick axe swinging side to side \nSide-side to side", inline=False)
creeperAwMan.add_field(name="This task a grueling one \nhope to find some diamonds tonight",value="night night \ndiamonds tonight", inline=False)
creeperAwMan.add_field(name="heads up \nYou hear a sound",value="turn around and look up \ntotal shock fills your body", inline=False)
creeperAwMan.add_field(name="oh no its you again \ni can never forget those eyes eyes eyes",value="eyes eyes eyes \ncause baby tonight", inline=False)
creeperAwMan.add_field(name="the creepers tryna steal all our stuff again \ncause baby tonight",value="your grab your pick shovel and bolt again \nand run run until its done done", inline=False)
creeperAwMan.add_field(name="until the sun comes up in the morn \ncause baby tonight",value="the creepers tryna steal all our stuff again \njust when you think youre safe", inline=False)
creeperAwMan.add_field(name="overhear some hissing from right behind \nright right behind",value="thats a nice life you have \nshame its gotta end at this time time time", inline=False)
creeperAwMan.add_field(name="time ti time time \nblows up",value="then your health bar drops and you could use a one up \nget inside dont be tardy", inline=False)
creeperAwMan.add_field(name="so now youre stuck in there \nhalf a heart is left but dont die die die",value="die die die \ncause baby tonight", inline=False)
creeperAwMan.add_field(name="the creepers tryna steal all our stuff again \ncause baby tonight",value="your grab your pick shovel and bolt again \nand run run until its done done", inline=False)
creeperAwMan.add_field(name="until the sun comes up in the morn \ncause baby tonight",value="the creepers tryna steal all our stuff again \ndig up diamonds and craft those diamonds", inline=False)
creeperAwMan.add_field(name="and make some armour get it baby \ngo and forge that like you so mlg pro",value="the swords made of diamonds so come at me bro \ntraining in your room under the torchlight", inline=False)
creeperAwMan.add_field(name="hone that form to get you ready for the big fight \nevery single day and the whole night",value="creepers out prowlin alright \nlook at me look at you", inline=False)
creeperAwMan.add_field(name="take my revenge thats what im gonna do \nim a warrior baby what else is new",value="and my blades gonna tear through you bring it \ncause baby tonight", inline=False)
creeperAwMan.add_field(name="the creepers tryna steal all our stuff again \nyeah baby tonight",value="grab your sword armour and go \ntake your revenge oh-oh oh-oh", inline=False)
creeperAwMan.add_field(name="so fight fight like its the last last night \nof your life life show them your bite",value="cause baby tonight \nthe creepers tryna steal all our stuff again", inline=False)
creeperAwMan.add_field(name="cause baby tonight \nyour grab your pick shovel and bolt again",value="and run run until its done done \nuntil the sun comes up in the morn", inline=False)
creeperAwMan.add_field(name="cause baby tonight",value="the creepers tryna steal all our stuff again", inline=False)

uwuSoWarm = discord.Embed(title="~nyaa~",description=" ", inline=False)
uwuSoWarm.add_field(name="Rawr x3 nuzzles pounces on you uwu you so warm",value="couldn't help but notice your \nbulge from across the floor", inline=False)
uwuSoWarm.add_field(name="nuzzles your necky wecky ~murr~ hehe\nunzips your baggy ass",value="oof baby you so musky\ntake me and pet me and make me yours", inline=False)
uwuSoWarm.add_field(name="and don't forget to stuff me\nsee me wag my widdle baby tail",value="oh for your bulgy wulgy kissies and lickies your neck\n i hope daddy likies", inline=False)
uwuSoWarm.add_field(name="nuzzles and wuzzles your chest\ni be getting thirsty.",value="hey i got a little itch you think you could help me\nonly 7 inches long", inline=False)
uwuSoWarm.add_field(name="UwU PLZ ADOPT ME",value="paws on your bulge as i lick my lips", inline=False)
uwuSoWarm.add_field(name="bout to hit them with this furry shit",value="he don't see it coming", inline=False)

@client.event
async def on_ready():
    change_status.start()
    print(f"Bot logged in.")

@tasks.loop(seconds=15)
async def change_status():
    global prefix
    await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def ping(ctx):
    await ctx.send(f"Current ping: {round(client.latency*1000)}ms")
    print(f"{ctx.author} sent {prefix}ping")

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, *amount):
    amount = int(amount[0])
    await ctx.channel.purge(limit=amount)

@client.command()
async def helpme(ctx):
    commands={}
    commands["ping"]="Shows bot current ping."
    commands["clear [amount]"]="Clears [amount] number of posts."
    commands["helpme"]="Displays this message."
    commands["h"]="h"
    commands["help"]="no"
    commands["praise"]="YOU MUST PRAISE"
    commands["bitrate"]="uwu bitrate-san"
    commands["neil"]="neil"
    commands["christopher"]="christopher"
    commands["qualitybotv2"]="unoriginal content"
    commands["qualitybot"]="quality content"
    commands["**kurwa**"]="**FRICK**"
    commands["owo"]="owo-san"
    commands["uwu"]="uwu-chan"
    commands["creeper"]="aw man"
    commands["rawr"]="x3 nuzzles"
    msg=discord.Embed(title='QualityBotV2', description="Written by JezzaR The Protogen#6483 using Discord.py because heck js",color=0x00ff99)
    for command,description in commands.items():
        msg.add_field(name=command,value=description, inline=False)
    await ctx.send("", embed=msg)
    print(f"{ctx.author} sent {prefix}helpme")

@client.command()
async def h(ctx):
    await ctx.send("h")
    print(f"{ctx.author} sent {prefix}h")

@client.command()
async def help(ctx):
    await ctx.send("you are beyond help")
    print(f"{ctx.author} sent {prefix}help")

@client.command()
async def praise(ctx):
    await ctx.send("PRAISE LORD AND SAVIOUR QualityBot!")
    await ctx.send("PRAISE THE ORB")
    await ctx.send("PRAISE NEIL")
    await ctx.send("PRAISE CHRISTOPHER")
    print(f"{ctx.author} sent {prefix}praise")

@client.command()
async def bitrate(ctx):
    await ctx.send("GIVE ME ALL YOUR JUICY DATA")
    print(f"{ctx.author} sent {prefix}bitrate")

@client.command()
async def neil(ctx):
    await ctx.send("may neil praise you")
    print(f"{ctx.author} sent {prefix}neil")

@client.command()
async def christopher(ctx):
    await ctx.send("christopher is love christopher is life")
    print(f"{ctx.author} sent {prefix}christopher")

@client.command()
async def qualitybotv2(ctx):
    await ctx.send("yes thats me")
    print(f"{ctx.author} sent {prefix}qualitybotv2")

@client.command()
async def qualitybot(ctx):
    await ctx.send("no thats not me that the original you should know this")
    print(f"{ctx.author} sent {prefix}qualitybot")

@client.command()
async def kurwa(ctx):
    await ctx.send("**FRICK**")
    print(f"{ctx.author} sent {prefix}kurwa")

@client.command()
async def owo(ctx):
    await ctx.send("OwO")
    print(f"{ctx.author} sent {prefix}owo")

@client.command()
async def uwu(ctx):
    await ctx.send("UwU")
    print(f"{ctx.author} sent {prefix}uwu")

@client.command()
async def creeper(ctx):
    await ctx.send("aw man",embed=creeperAwMan)
    print(f"{ctx.author} sent {prefix}creeper")

@client.event
async def on_message(ctx):
    await client.process_commands(ctx)
    if ctx.content.lower() == "uwu":
        await ctx.channel.send("OwO what's this?")
    elif ctx.content.lower() == "rawr":
        await ctx.channel.send("",embed=uwuSoWarm)

client.run("NjA2OTAwMDQ5MTQxNTYzNDAy.Xn_mGQ._hQmjmZ6Duo19-sDloptdLlaO6w")
