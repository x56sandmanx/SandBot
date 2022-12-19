import discord
from discord import app_commands
from discord.ext import commands

class Purge(commands.Cog):
  def __init__(self, client):
    self.client = client

  @app_commands.command(name="purge", description="Delete certain amount of messages")
  @app_commands.describe(limit="Number of messages to be deleted")
  async def purge(self, interaction: discord.Interaction, limit: int):
    if(limit > 50):
      return await interaction.response.send_message("Cannot delete more than 50 messages at a time!")
    else:
      await interaction.response.defer()
      channel = interaction.channel
      await channel.purge(limit=limit)
    await channel.send(f"Purged {limit} messages")

async def setup(client):
  await client.add_cog(Purge(client))