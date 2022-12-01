import discord
import asyncio
from datetime import datetime
from discord.ext import commands

class Mute(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.has_any_role("SandKnight (Admin)", "Sandman", "SandGuard (Mod)")
  async def mute(self, ctx, member: discord.Member, *, reason=None):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
    channel = discord.utils.get(member.guild.channels, name="command-logs📚")
    embed=discord.Embed(title="Mute", color=0xc2b280,timestamp=datetime.utcnow())
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="User", value=member.mention, inline=True)
    embed.add_field(name="Moderator", value=ctx.message.author.mention, inline=True)
    embed.add_field(name="Reason", value=reason, inline=True)
    await channel.send(embed=embed)

  @commands.command()
  @commands.has_any_role("SandKnight (Admin)", "Sandman", "SandGuard (Mod)")
  async def tempmute(self, ctx, member : discord.Member, time, *, reason=None):
    guild = ctx.guild
    dayTime = time[-1]
    numTime = time[:-1]
    print(type(dayTime))
    print(type(numTime))
    for role in guild.roles:
      if role.name=="Muted":
        await member.add_roles(role)
        channel = discord.utils.get(member.guild.channels, name="command-logs📚")
        embed=discord.Embed(title="Temp Mute", color=0xc2b280,timestamp=datetime.utcnow())
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="User", value=member.mention, inline=True)
        embed.add_field(name="Moderator", value=ctx.message.author.mention, inline=True)
        embed.add_field(name="Time", value=f"{time}", inline=False)
        embed.add_field(name="Reason", value=reason, inline=True)
        await channel.send(embed=embed)

        if dayTime =="s":
          await asyncio.sleep(int(numTime))
        if dayTime == "m":
          await asyncio.sleep(int(numTime)*60)
        if dayTime == "h":
          await asyncio.sleep(int(numTime)*60*60)
        if dayTime == "d":
          await asyncio.sleep(int(numTime)*60*60*24)
      
        await member.remove_roles(role)

        embed=discord.Embed(title="Unmute", color=0xc2b280,timestamp=datetime.utcnow())
        embed.add_field(name="User", value=f"{member.mention}")
        await channel.send(embed=embed)

        return

  @commands.command()
  @commands.has_any_role("SandKnight (Admin)", "Sandman", "SandGuard (Mod)")
  async def unmute(self, ctx, member: discord.Member, *, reason=None):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(role)
    channel = discord.utils.get(member.guild.channels, name="command-logs📚")
    embed=discord.Embed(title="Unmute", color=0xc2b280,timestamp=datetime.utcnow())
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="User", value=member.mention, inline=True)
    embed.add_field(name="Moderator", value=ctx.message.author.mention, inline=True)
    embed.add_field(name="Reason", value=reason, inline=True)
    await channel.send(embed=embed)

def setup(client):
  client.add_cog(Mute(client))