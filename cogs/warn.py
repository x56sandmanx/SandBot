import discord
from discord.ext import commands

class Warn(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.has_any_role("Mod", "SandKnight (Admin)", "Sandman")
  async def warn(self, ctx, member : discord.Member, *, reason=None):
    channel = discord.utils.get(member.guild.channels, name="logs")
    embed=discord.Embed(title="Warn", color=discord.Color.blue())
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.add_field(name="User", value=member.mention, inline=True)
    embed.add_field(name="Moderator", value=ctx.message.author.mention, inline=True)
    embed.add_field(name="Reason", value=reason, inline=True)
    await channel.send(embed=embed)

def setup(client):
  client.add_cog(Warn(client))