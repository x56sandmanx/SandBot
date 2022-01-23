import discord
import random
from discord.ext import commands

intents = discord.Intents().all()
client = commands.Bot(intents=intents, command_prefix='-')

class Roll(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def roll(self, ctx):
    user_choice = random.randint(1,9)
    comp_choice = random.randint(1,9)

    if user_choice > comp_choice:
      await ctx.send(f'Your roll: **{user_choice}**\nMy roll: **{comp_choice}**\nYou win')
    elif user_choice < comp_choice:
      await ctx.send(f'Your roll: **{user_choice}**\nMy roll: **{comp_choice}**\nYou lose')
    elif user_choice == comp_choice:
      await ctx.send(f'Your roll: **{user_choice}**\nMy roll: **{comp_choice}**\nTie')

def setup(client):
  client.add_cog(Roll(client))