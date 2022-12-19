import discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime


class Kick(commands.Cog):

  def __init__(self, client):
    self.client = client

  @app_commands.command(name="kick", description="Kick a certain user")
  @app_commands.describe(user="User to kick")
  async def kick(self, interaction: discord.Interaction, user: discord.Member,
                 reason: str):
    if not reason:
      await interaction.response.send_message("Please provide a reason")
      return
    channel = discord.utils.get(user.guild.channels, name="command-logs📚")
    embed = discord.Embed(title="Kick",
                          color=0xc2b280,
                          timestamp=datetime.utcnow())
    embed.set_thumbnail(url=user.avatar)
    embed.add_field(name="User", value=user.mention, inline=True)
    embed.add_field(name="Moderator",
                    value=interaction.user.mention,
                    inline=True)
    embed.add_field(name="Reason", value=reason, inline=True)
    await interaction.response.send_message(embed=embed)
    await channel.send(embed=embed)
    await user.send(embed=embed)
    await user.kick(reason=reason)


async def setup(client):
  await client.add_cog(Kick(client))
