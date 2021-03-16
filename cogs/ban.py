import discord
from discord.ext import commands

class Ban(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    channel = discord.utils.get(member.guild.channels, name="logs")
    embed=discord.Embed(title="Ban", color=discord.Color.blue())
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.add_field(name="User", value=member.mention, inline=True)
    embed.add_field(name="Moderator", value=ctx.message.author.mention, inline=True)
    embed.add_field(name="Reason", value=reason, inline=True)
    await channel.send(embed=embed)

def setup(client):
  client.add_cog(Ban(client))