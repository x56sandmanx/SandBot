import discord
from discord.ext import commands
from datetime import datetime

class Reaction(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_raw_reaction_add(self, payload):
    guild = discord.utils.find(lambda g : g.id == payload.guild_id, self.client.guilds)
    if payload.emoji.name == '🔞':
      role = discord.utils.get(guild.roles, name='NSFW')
    elif payload.emoji.name =='👶':
      role = discord.utils.get(guild.roles, name='13-16')
    elif payload.emoji.name=='👦':
      role = discord.utils.get(guild.roles, name='17-20')
    elif payload.emoji.name=='🧓':
      role = discord.utils.get(guild.roles, name='21+')
    elif payload.emoji.name=='👨':
      role = discord.utils.get(guild.roles, name='Male')
    elif payload.emoji.name=='👩':
      role = discord.utils.get(guild.roles, name='Female')
    elif payload.emoji.name=='⚫':
      role = discord.utils.get(guild.roles, name='black')
    elif payload.emoji.name=='🔵':
      role = discord.utils.get(guild.roles, name='blue')
    elif payload.emoji.name=='🔴':
      role = discord.utils.get(guild.roles, name='red')
    elif payload.emoji.name=='🟡':
      role = discord.utils.get(guild.roles, name='yellow')
    elif payload.emoji.name=='🟢':
      role = discord.utils.get(guild.roles, name='green')
    elif payload.emoji.name=='🟣':
      role = discord.utils.get(guild.roles, name='purple')
    else:
      role = discord.utils.get(guild.roles, name=payload.emoji.name)

    if role is not None:
      member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
      if member is not None:
        await member.add_roles(role)

  @commands.Cog.listener()
  async def on_raw_reaction_remove(self, payload):
    guild = discord.utils.find(lambda g : g.id == payload.guild_id, self.client.guilds)
    if payload.emoji.name == '🔞':
      role = discord.utils.get(guild.roles, name='NSFW')
    elif payload.emoji.name =='👶':
      role = discord.utils.get(guild.roles, name='13-16')
    elif payload.emoji.name=='👦':
      role = discord.utils.get(guild.roles, name='17-20')
    elif payload.emoji.name=='🧓':
      role = discord.utils.get(guild.roles, name='21+')
    elif payload.emoji.name=='👨':
      role = discord.utils.get(guild.roles, name='Male')
    elif payload.emoji.name=='👩':
      role = discord.utils.get(guild.roles, name='Female')
    elif payload.emoji.name=='⚫':
      role = discord.utils.get(guild.roles, name='black')
    elif payload.emoji.name=='🔵':
      role = discord.utils.get(guild.roles, name='blue')
    elif payload.emoji.name=='🔴':
      role = discord.utils.get(guild.roles, name='red')
    elif payload.emoji.name=='🟡':
      role = discord.utils.get(guild.roles, name='yellow')
    elif payload.emoji.name=='🟢':
      role = discord.utils.get(guild.roles, name='green')
    elif payload.emoji.name=='🟣':
      role = discord.utils.get(guild.roles, name='purple')
    else:
      role = discord.utils.get(guild.roles, name=payload.emoji.name)

    if role is not None:
      member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
      if member is not None:
        await member.remove_roles(role)
  
  # Sends message with reaction
  @commands.command() 
  async def react(self, ctx):
    embed=discord.Embed(title="Reaction Roles!", color=0xc2b280,timestamp=datetime.utcnow())
    embed.add_field(name="NSFW", value="🔞", inline=False)
    embed.add_field(name="Age", value="🧓: 21+\n👦: 17-20\n👶: 13-16", inline=False)
    embed.add_field(name="Gender", value="👨: Male\n👩: Female", inline=False)
    react_message = await ctx.send(embed=embed)
    await react_message.add_reaction("🔞")
    await react_message.add_reaction("🧓")
    await react_message.add_reaction("👦")
    await react_message.add_reaction("👶")
    await react_message.add_reaction("👨")
    await react_message.add_reaction("👩")

  @commands.command() 
  async def colorreact(self, ctx):
    embed=discord.Embed(title="Color Reaction Roles!", color=0xc2b280,timestamp=datetime.utcnow())
    embed.add_field(name="Colors", value="⚫: Black\n🔵: Blue\n🔴: Red\n🟡: Yellow\n🟢: Green\n🟣: Purple", inline=False)
    react_message = await ctx.send(embed=embed)
    await react_message.add_reaction("⚫")
    await react_message.add_reaction("🔵")
    await react_message.add_reaction("🔴")
    await react_message.add_reaction("🟡")
    await react_message.add_reaction("🟢")
    await react_message.add_reaction("🟣")
    
async def setup(client):
  await client.add_cog(Reaction(client))