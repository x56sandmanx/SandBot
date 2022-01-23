import discord
from discord.ext import commands
from datetime import datetime

class Help(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def help(self, ctx):
    embed=discord.Embed(title="Help", color=0xc2b280,timestamp=datetime.utcnow())
    embed.add_field(name="-serverInfo", value="Shows server info", inline=False)
    embed.add_field(name="-rps", value="Play rock, paper, scissors with the Bot", inline=False)
    embed.add_field(name="-add [value1] [value2]", value="add two numbers", inline=False)
    embed.add_field(name="-sub [value1] [value2]", value="subtract two numbers", inline=False)
    embed.add_field(name="-multi [value1] [value2]", value="multiply two numbers", inline=False)
    embed.add_field(name="-div [value1] [value2]", value="divide two numbers", inline=False)
    embed.add_field(name="-roll", value="roll off with the bot", inline=False)
    embed.set_footer(text="Help page 1/2")
    await ctx.send(embed=embed)
  
  @commands.command()
  async def help2(self, ctx):
    embed=discord.Embed(title="Help", color=0xc2b280,timestamp=datetime.utcnow())
    embed.add_field(name="-kiss [@person]", value="kiss someone in the server", inline=False)
    embed.add_field(name="-userInfo / -userInfo [@person]", value="get information on you or a user", inline=False)
    embed.add_field(name="-bal / -bal", value="check your balance", inline=False)
    embed.add_field(name="-beg / -beg", value="beg for money", inline=False)
    embed.set_footer(text="Help page 2/2")
    await ctx.send(embed=embed)

  @commands.command()
  @commands.has_any_role("Mod", "SandKnight (Admin)", "Sandman")
  async def adminhelp(self, ctx):
    embed=discord.Embed(title="Admin Help", color=0xc2b280,timestamp=datetime.utcnow())
    embed.add_field(name="-warn [@person] [reason]", value="Warn a user Ex: -warn @x56sandmanx spam",inline=False)
    embed.add_field(name="-tempmute [@person] [length] [time] [reason]", value="Temporarily mute a user Ex: -tempmute @x56sandmanx 10 s spam 5 times",inline=False)
    embed.add_field(name="-mute [@person] [reason]", value="Permanently mute a user Ex: -mute @x56sandmanx wall spam", inline=False)
    embed.add_field(name="-unmute [@person]", value="Unmute a user", inline=False)
    embed.add_field(name="-kick [@person] [reason]", value="Kick a user Ex: -kick @x56sandmanx breaking rules", inline=False)
    embed.add_field(name="-ban [@person] [reason]", value="Ban a member (Admins only) Ex: -ban @x56sandmanx broke all rules", inline=False)
    embed.set_footer(text="Help page 1/1")
    await ctx.send(embed=embed)


def setup(client):
  client.add_cog(Help(client))