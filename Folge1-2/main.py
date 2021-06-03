import discord
from discord.ext import commands
import random
import asyncio

#------------------------------------------------------------------

intents = discord.Intents.default()
intents.members = True
intents.presences = True

client = commands.Bot(command_prefix = '!', intents=discord.Intents.all())

client.remove_command('help')

#-----------------------------------------------------------------

@client.event
async def on_ready():
    print(f'{client.user.name} wurde hochgefahren!')
    await client.change_presence(activity=discord.Game('mir mir'), status=discord.Status.online)


@client.command()
async def test(ctx):
    await ctx.send("Ich bin ein Test luuul")

@client.command()
async def sprech(ctx, *, arg):
    await ctx.send(f"Deine Nachricht: {arg}")

@client.command()
async def jaodernein(ctx):
    jaodernein = ["Ja", "Nein", "ddjkh"]
    rndm = random.choice(jaodernein)
    await ctx.send(f'Meine Antwort: {rndm}')


@client.command(aliases=["zahl", "zzahl"])
async def randomnumber(ctx):
    zahl = random.randint(1, 100)
    await ctx.send(f"Deine Zahl: {zahl}")


@client.command()
async def embed(ctx):
    embed=discord.Embed(title='lol', description="Ich bin cool yeah", color=discord.Color.dark_blue())
    embed.add_field(name='Überschriiift', value='Ich bin hier unten :c', inline=False)
    embed.add_field(name='2 Feld', value='loool', inline=False)
    embed.set_author(name='heisserhund', icon_url=ctx.author.avatar_url)
    embed.set_footer(text='unten bin ich lol', icon_url=ctx.guild.icon_url)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/848704536830148650/850113446862913556/40f189daa5c0279718484ca5f5569f78-bitcoin-icon-by-vexels.png")
    embed.set_image(url="https://cdn.discordapp.com/attachments/848704536830148650/850114390783033347/587113586279710742.png")
    await ctx.send(embed=embed)


@client.command()
async def ping(ctx):
    await ctx.send(f"{round(client.latency * 100)}ms")



#-----------------------------------------------------------------

client.run("DEIN TOKEN")
