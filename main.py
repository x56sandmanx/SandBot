import discord
import os
from discord.ext import commands
#from keep_alive import keep_alive

intents = discord.Intents().all()
client = commands.Bot(intents=intents, command_prefix='-')
client.remove_command('help')


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game("-help | SandBot v1.2"))
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="welcome")
    await channel.send(
        f"Welcome to **{member.guild.name}** {member.mention}! Head over to <#797282653946642474> to be cool!"
    )
    role = discord.utils.get(member.guild.roles, name="Sandling")
    await member.add_roles(role)

with open('token.txt') as f:
    TOKEN = f.readline()

token = os.environ.get('TOKEN')
#keep_alive()
client.run(token)
