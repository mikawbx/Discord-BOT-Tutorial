import discord
from discord import member
from discord.ext import commands
import random

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
async def sprech(ctx, *, arg):
    await ctx.send(f"Deine Nachricht: {arg}")


@client.command()
async def ping(ctx):
    await ctx.send(f"{round(client.latency * 100)}ms")

#-----------------------------------------------------------------

@client.event
async def on_member_join(member):
    guild = client.get_guild(id=768520545951678534)
    await member.send("Herzlich willkommen bei uns!")
    channel = await client.fetch_channel(850151389493461002)
    await channel.send(f"Willkommen {member.mention}! Hab hier viel Spaß!")
    role = discord.utils.get(guild.roles, name="Benutzer")
    await member.add_roles(role)


@client.event
async def on_member_remove(member):
    channel = await client.fetch_channel(850151417301303316)
    await channel.send(f"Schönes Leben {member.name}#{member.discriminator} wünschen wir dir noch!")


#-----------------------------------------------------------------

client.run('ODQ4ODE5MDE2NjI5MjIzNDY0.YLSKTw.eE3XDrL69KbLiuaRVdvWu6C516Q')
