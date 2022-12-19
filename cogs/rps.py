import discord
import random
from discord import app_commands
from discord.ext import commands
from discord.ui import Button, View
from datetime import datetime

class RPS(commands.Cog):
  def __init__(self, client):
    self.client = client

  @app_commands.command(name="rps", description="Play RPS with the CPU!")
  async def rps(self, interaction: discord.Interaction):
    button1 = Button(emoji="🪨", style=discord.ButtonStyle.blurple)
    button2 = Button(emoji="📄", style=discord.ButtonStyle.blurple)
    button3 = Button(emoji="✂️", style=discord.ButtonStyle.blurple)
  
    async def rock_callback(interaction):
      button1 = Button(emoji="🪨", style=discord.ButtonStyle.blurple)
      button2 = Button(emoji="📄", style=discord.ButtonStyle.blurple)
      button3 = Button(emoji="✂️", style=discord.ButtonStyle.blurple)
      view = View()
      view.add_item(button1)
      view.add_item(button2)
      view.add_item(button3)
      button1.callback = rock_callback
      button2.callback = paper_callback
      button3.callback = scissors_callback
      cpu = random.randint(0,2)
      if(cpu == 0):
        embed = discord.Embed(title="Results",
                          color=0xc2b280,
                          timestamp=datetime.utcnow())
        embed.add_field(name=f"{interaction.user.name}'s Pick",
                        value="🪨",
                        inline=False)
        embed.add_field(name="SandBot's Pick",
                        value="🪨",
                        inline=False)
        embed.add_field(name="Result",
                        value="We Tied!",
                        inline=False)
        await interaction.response.send_message(embed=embed, view=view)
      elif(cpu == 1):
        embed = discord.Embed(title="Results",
                          color=0xc2b280,
                          timestamp=datetime.utcnow())
        embed.add_field(name=f"{interaction.user.name}'s Pick",
                        value="🪨",
                        inline=False)
        embed.add_field(name="SandBot's Pick",
                        value="📄",
                        inline=False)
        embed.add_field(name="Result",
                        value="SandBot Wins!",
                        inline=False)
        await interaction.response.send_message(embed=embed, view=view)
      else:
        embed = discord.Embed(title="Results",
                          color=0xc2b280,
                          timestamp=datetime.utcnow())
        embed.add_field(name=f"{interaction.user.name}'s Pick",
                        value="🪨",
                        inline=False)
        embed.add_field(name="SandBot's Pick",
                        value="✂️",
                        inline=False)
        embed.add_field(name="Result",
                        value=f"{interaction.user.name} Wins!",
                        inline=False)
        await interaction.response.send_message(embed=embed, view=view)
  
    async def paper_callback(interaction):
      button1 = Button(emoji="🪨", style=discord.ButtonStyle.blurple)
      button2 = Button(emoji="📄", style=discord.ButtonStyle.blurple)
      button3 = Button(emoji="✂️", style=discord.ButtonStyle.blurple)
      view = View()
      view.add_item(button1)
      view.add_item(button2)
      view.add_item(button3)
      button1.callback = rock_callback
      button2.callback = paper_callback
      button3.callback = scissors_callback
      cpu = random.randint(0,2)
      if(cpu == 0):
        embed = discord.Embed(title="Results",
                          color=0xc2b280,
                          timestamp=datetime.utcnow())
        embed.add_field(name=f"{interaction.user.name}'s Pick",
                        value="📄",
                        inline=False)
        embed.add_field(name="SandBot's Pick",
                        value="🪨",
                        inline=False)
        embed.add_field(name="Result",
                        value=f"{interaction.user.name} Wins!",
                        inline=False)
        await interaction.response.send_message(embed=embed, view=view)
      elif(cpu == 1):
        embed = discord.Embed(title="Results",
                          color=0xc2b280,
                          timestamp=datetime.utcnow())
        embed.add_field(name=f"{interaction.user.name}'s Pick",
                        value="📄",
                        inline=False)
        embed.add_field(name="SandBot's Pick",
                        value="📄",
                        inline=False)
        embed.add_field(name="Result",
                        value="We Tied!",
                        inline=False)
        await interaction.response.send_message(embed=embed, view=view)
      else:
        embed = discord.Embed(title="Results",
                          color=0xc2b280,
                          timestamp=datetime.utcnow())
        embed.add_field(name=f"{interaction.user.name}'s Pick",
                        value="📄",
                        inline=False)
        embed.add_field(name="SandBot's Pick",
                        value="✂️",
                        inline=False)
        embed.add_field(name="Result",
                        value="SandBot Wins!",
                        inline=False)
        await interaction.response.send_message(embed=embed, view=view)
  
    async def scissors_callback(interaction):
      button1 = Button(emoji="🪨", style=discord.ButtonStyle.blurple)
      button2 = Button(emoji="📄", style=discord.ButtonStyle.blurple)
      button3 = Button(emoji="✂️", style=discord.ButtonStyle.blurple)
      view = View()
      view.add_item(button1)
      view.add_item(button2)
      view.add_item(button3)
      button1.callback = rock_callback
      button2.callback = paper_callback
      button3.callback = scissors_callback
      cpu = random.randint(0,2)
      if(cpu == 0):
        embed = discord.Embed(title="Results",
                          color=0xc2b280,
                          timestamp=datetime.utcnow())
        embed.add_field(name=f"{interaction.user.name}'s Pick",
                        value="✂️",
                        inline=False)
        embed.add_field(name="SandBot's Pick",
                        value="🪨",
                        inline=False)
        embed.add_field(name="Result",
                        value="SandBot Wins!",
                        inline=False)
        await interaction.response.send_message(embed=embed, view=view)
      elif(cpu == 1):
        embed = discord.Embed(title="Results",
                          color=0xc2b280,
                          timestamp=datetime.utcnow())
        embed.add_field(name=f"{interaction.user.name}'s Pick",
                        value="✂️",
                        inline=False)
        embed.add_field(name="SandBot's Pick",
                        value="📄",
                        inline=False)
        embed.add_field(name="Result",
                        value=f"{interaction.user.name} Wins!",
                        inline=False)
        await interaction.response.send_message(embed=embed, view=view)
      else:
        embed = discord.Embed(title="Results",
                          color=0xc2b280,
                          timestamp=datetime.utcnow())
        embed.add_field(name=f"{interaction.user.name}'s Pick",
                        value="✂️",
                        inline=False)
        embed.add_field(name="SandBot's Pick",
                        value="✂️",
                        inline=False)
        embed.add_field(name="Result",
                        value="We Tied!",
                        inline=False)
        await interaction.response.send_message(embed=embed, view=view)
  
    button1.callback = rock_callback
    button2.callback = paper_callback
    button3.callback = scissors_callback
    
    view = View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
  
    embed = discord.Embed(title="RPS",
                          color=0xc2b280,
                          timestamp=datetime.utcnow())
    embed.add_field(name="🪨",
                    value="Pick this for rock!",
                    inline=False)
    embed.add_field(name="📄",
                    value="Pick this for paper!",
                    inline=False)
    embed.add_field(name="✂️",
                    value="Pick this for scissors!",
                    inline=False)
    await interaction.response.send_message(embed=embed, view=view)

async def setup(client):
  await client.add_cog(RPS(client))