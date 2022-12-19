import discord
from discord.ext import commands
from discord import app_commands

class Ban(commands.Cog):
  def __init__(self, client):
    self.client = client

  @app_commands.command(name="ban",
                        description="Ban a certain user")
  @app_commands.describe(user="User being banned", reason="Reason for ban")
  async def ban(self, interaction: discord.Interaction, user : discord.Member, reason: str):
    channel = discord.utils.get(user.guild.channels, name="command-logs📚")
    embed=discord.Embed(title="Ban", color=0xc2b280)
    embed.set_thumbnail(url=user.avatar)
    embed.add_field(name="User", value=user.mention, inline=True)
    embed.add_field(name="Moderator", value=interaction.user.mention, inline=True)
    embed.add_field(name="Reason", value=reason, inline=True)
    await interaction.response.send_message(embed=embed)
    await channel.send(embed=embed)
    await user.send(embed=embed)
    await user.ban(reason=reason)

async def setup(client):
  await client.add_cog(Ban(client))