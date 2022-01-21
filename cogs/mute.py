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
    embed=discord.Embed(title="Mute", color=discord.Color.blue(),timestamp=datetime.utcnow())
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.add_field(name="User", value=member.mention, inline=True)
    embed.add_field(name="Moderator", value=ctx.message.author.mention, inline=True)
    embed.add_field(name="Reason", value=reason, inline=True)
    await channel.send(embed=embed)

  @commands.command()
  @commands.has_any_role("SandKnight (Admin)", "Sandman", "SandGuard (Mod)")
  async def tempmute(self, ctx, member : discord.Member, time: int, d, *, reason=None):
    guild = ctx.guild
    for role in guild.roles:
      if role.name=="Muted":
        await member.add_roles(role)
        channel = discord.utils.get(member.guild.channels, name="command-logs📚")
        embed=discord.Embed(title="Temp Mute", color=discord.Color.blue(),timestamp=datetime.utcnow())
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name="User", value=member.mention, inline=True)
        embed.add_field(name="Moderator", value=ctx.message.author.mention, inline=True)
        embed.add_field(name="Time", value=f"{time}{d}", inline=False)
        embed.add_field(name="Reason", value=reason, inline=True)
        await channel.send(embed=embed)

        if d =="s":
          await asyncio.sleep(time)
        if d == "m":
          await asyncio.sleep(time*60)
        if d == "h":
          await asyncio.sleep(time*60*60)
        if d == "d":
          await asyncio.sleep(time*60*60*24)
      
        await member.remove_roles(role)

        embed=discord.Embed(title="Unmute", color=discord.Color.blue())
        embed.add_field(name="User", value=f"{member.mention}")
        await channel.send(embed=embed)

        return

  @commands.command()
  @commands.has_any_role("SandKnight (Admin)", "Sandman", "SandGuard (Mod)")
  async def unmute(self, ctx, member: discord.Member, *, reason=None):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(role)
    channel = discord.utils.get(member.guild.channels, name="command-logs📚")
    embed=discord.Embed(title="Unmute", color=discord.Color.blue(),timestamp=datetime.utcnow())
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.add_field(name="User", value=member.mention, inline=True)
    embed.add_field(name="Moderator", value=ctx.message.author.mention, inline=True)
    embed.add_field(name="Reason", value=reason, inline=True)
    await channel.send(embed=embed)

def setup(client):
  client.add_cog(Mute(client))