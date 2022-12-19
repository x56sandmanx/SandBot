import discord
from discord.ext import commands
from discord import app_commands
from discord import Embed
from datetime import datetime


class Userinfo(commands.Cog):

  def __init__(self, client):
    self.client = client

  @app_commands.command(name="userinfo",
                        description="Get info on a certain user!")
  @app_commands.describe(user="User to get info on")
  async def userInfo(self, interaction: discord.Interaction,
                     user: discord.Member):
    user = interaction.guild.get_member(user.id)

    embed = Embed(title="User information",
                  colour=user.colour,
                  timestamp=datetime.utcnow())

    embed.set_thumbnail(url=user.avatar)

    fields = [
      ("Name", str(user), True), ("ID", user.id, True),
      ("Bot?", user.bot, True), ("Top role", user.top_role.mention, True),
      ("Status", str(user.status).title(), True),
      ("Activity",
       f"{str(user.activity.type).split('.')[-1].title() if user.activity else 'N/A'} {user.activity.name if user.activity else ''}",
       True), ("Created on", user.created_at.strftime("%m/%d/%Y"), True),
      ("Joined on", user.joined_at.strftime("%m/%d/%Y"), True),
      ("Boosted", bool(user.premium_since), True)
    ]

    for name, value, inline in fields:
      embed.add_field(name=name, value=value, inline=inline)

    await interaction.response.send_message(embed=embed)


async def setup(client):
  await client.add_cog(Userinfo(client))
