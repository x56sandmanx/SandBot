import discord
import asyncio
from discord import app_commands
from discord.ext import commands
from datetime import datetime


class Mute(commands.Cog):

  def __init__(self, client):
    self.client = client

  @app_commands.command(name="mute", description="Mute a certain user")
  @app_commands.describe(user="User to mute", reason="Reason of mute")
  async def mute(self, interaction: discord.Interaction, user: discord.Member,
                 reason: str):
    role = discord.utils.get(interaction.guild.roles, name="Muted")
    await user.add_roles(role)
    channel = discord.utils.get(user.guild.channels, name="command-logs📚")
    embed = discord.Embed(title="Mute",
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

  @app_commands.command(name="tempmute",
                        description="Temporarily mute a certain user")
  @app_commands.describe(user="User to tempmute",
                         time="Amount of time for mute (ex: 5m,10d,7s,etc)",
                         reason="Reason of mute")
  async def tempmute(self, interaction: discord.Interaction,
                     user: discord.Member, time: str, reason: str):
    guild = interaction.guild
    dayTime = time[-1]
    numTime = time[:-1]
    for role in guild.roles:
      if role.name == "Muted":
        await user.add_roles(role)
        channel = discord.utils.get(user.guild.channels, name="command-logs📚")
        embed = discord.Embed(title="Temp Mute",
                              color=0xc2b280,
                              timestamp=datetime.utcnow())
        embed.set_thumbnail(url=user.avatar)
        embed.add_field(name="User", value=user.mention, inline=True)
        embed.add_field(name="Moderator",
                        value=interaction.user.mention,
                        inline=True)
        embed.add_field(name="Time", value=f"{time}", inline=False)
        embed.add_field(name="Reason", value=reason, inline=True)
        await interaction.response.send_message(embed=embed)
        await channel.send(embed=embed)
        await user.send(embed=embed)

        if dayTime == "s":
          await asyncio.sleep(int(numTime))
        if dayTime == "m":
          await asyncio.sleep(int(numTime) * 60)
        if dayTime == "h":
          await asyncio.sleep(int(numTime) * 60 * 60)
        if dayTime == "d":
          await asyncio.sleep(int(numTime) * 60 * 60 * 24)

        await user.remove_roles(role)

        embed = discord.Embed(title="Unmute",
                              color=0xc2b280,
                              timestamp=datetime.utcnow())
        embed.add_field(name="User", value=f"{user.mention}")
        await channel.send(embed=embed)
        await user.send(embed=embed)

  @app_commands.command(name="unmute", description="Unmute a certain user")
  @app_commands.describe(user="User to unmute")
  async def unmute(self, interaction: discord.Interaction,
                   user: discord.Member):
    role = discord.utils.get(interaction.guild.roles, name="Muted")
    await user.remove_roles(role)
    channel = discord.utils.get(user.guild.channels, name="command-logs📚")
    embed = discord.Embed(title="Unmute",
                          color=0xc2b280,
                          timestamp=datetime.utcnow())
    embed.set_thumbnail(url=user.avatar)
    embed.add_field(name="User", value=user.mention, inline=True)
    embed.add_field(name="Moderator",
                    value=interaction.user.mention,
                    inline=True)
    await interaction.response.send_message(embed=embed)
    await channel.send(embed=embed)


async def setup(client):
  await client.add_cog(Mute(client))
