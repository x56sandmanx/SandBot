import discord
from discord.ext import commands

class Kiss(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def kiss(self, ctx, member : discord.Member):
    await ctx.send(f'**{ctx.message.author.mention}** kissed {member.mention}')

def setup(client):
  client.add_cog(Kiss(client))