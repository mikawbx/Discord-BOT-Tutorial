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
    pingmsg = await ctx.send(f"{round(client.latency * 100)}ms")
    await pingmsg.add_reaction("😣")

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

@client.command()
async def reactionmsg(ctx):
    msg = await ctx.send("KLICK = ROLLE")
    await msg.add_reaction("<:bitcoin:851166458489602078>")
    await msg.add_reaction("😀")


@client.event
async def on_raw_reaction_add(payload):
    guild = client.get_guild(id=768520545951678534)
    channel = client.get_channel(850706562385051658)
    message = await channel.fetch_message(852164311413030942)

    if payload.channel_id == 850706562385051658:
        if payload.message_id == 852164311413030942:

            if str(payload.emoji) == "😀":
                await message.remove_reaction(payload.emoji, payload.member)
                await guild.create_text_channel(name=f"{payload.member.name}-ticket", topic=f"Channel für {payload.member.name}")
            
            if str(payload.emoji) == "<:bitcoin:851166458489602078>":
                toastbrot = discord.utils.get(guild.roles, name="VIP")
                await payload.member.add_roles(toastbrot)


@client.event
async def on_raw_reaction_remove(payload):
    guild = client.get_guild(id=768520545951678534)

    if payload.channel_id == 850706562385051658:
        if payload.message_id == 852164311413030942:

            if str(payload.emoji) == "<:bitcoin:851166458489602078>":
                rr = discord.utils.get(guild.roles, name="VIP")
                member = guild.get_member(payload.user_id)
                await member.remove_roles(rr)




#-----------------------------------------------------------------

client.run("DEIN TOKEN")