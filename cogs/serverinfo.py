import discord
from discord.ext import commands
from datetime import datetime

class Serverinfo(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def serverInfo(self, context):
    guild = context.guild
    embed=discord.Embed(title="Server Stats", color=0xc2b280,timestamp=datetime.utcnow())
    embed.add_field(name="Server Name: ", value=guild.name, inline=False)
    embed.add_field(name="Server Size: ", value=len(guild.members), inline=False)
    embed.add_field(name="Owner Name: ", value=guild.owner.display_name, inline=False)
    await context.send(embed=embed)

def setup(client):
  client.add_cog(Serverinfo(client))