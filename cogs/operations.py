import discord
from discord.ext import commands

class Operations(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def add(self, ctx, left: int, right: int):
    await  ctx.send(left + right)

  @commands.command()
  async def sub(self, ctx, left: int, right: int):
    await  ctx.send(left - right)

  @commands.command()
  async def multi(self, ctx, left: int, right: int):
    await  ctx.send(left * right)

  @commands.command()
  async def div(self, ctx, left: int, right: int):
    await  ctx.send(left / right)

def setup(client):
  client.add_cog(Operations(client))