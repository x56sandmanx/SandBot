import discord
import os
import asyncio
import json
from discord import app_commands
from discord.ext import commands
from datetime import datetime
from dotenv import load_dotenv
from keep_alive import keep_alive

intents = discord.Intents().all()
intents.members = True
intents.presences = True
client = commands.Bot(intents=intents, command_prefix='-')
client.remove_command('help')


@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online,
                               activity=discord.Game("/help | SandBot v2.3.2"))
  print('We have logged in as {0.user}'.format(client))
  synced = await client.tree.sync()

async def load():
  for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
      await client.load_extension(f'cogs.{filename[:-3]}')



@client.event
async def on_member_join(member: discord.Member):
  channel = discord.utils.get(member.guild.channels, name="welcome👋")
  channel2 = discord.utils.get(member.guild.channels, name="roles🔧")
  channel3 = discord.utils.get(member.guild.channels, name="rules📜")
  embed = discord.Embed(
    title="The Sand Kingdom",
    description=
    f"Welcome to The Sand Kingdom {member.mention}, make sure to head to {channel2.mention} to get your roles and go to {channel3.mention} to check out the rules!",
    color=0xc2b280,
    timestamp=datetime.utcnow())
  embed.set_thumbnail(url=member.avatar)
  await channel.send(embed=embed)
  role = discord.utils.get(member.guild.roles, name="Sandling")
  await member.add_roles(role)

@client.event
async def on_message(message):
  words = message.content.lower().split()
  if 'colin' in words:
    await message.channel.send('colin!')
  if 'izzy' in words:
    await message.channel.send('izzy!')
  if 'sam' in words:
    await message.channel.send('sam!')
    
@client.event
async def on_message_delete(message):
  embed = discord.Embed(
    title=message.author.name,
    description=f"Message deleted in **{message.channel}**",
    color=0xc2b280,
    timestamp=datetime.utcnow())
  embed.set_thumbnail(url=message.author.avatar)
  embed.add_field(name=message.content, value="Deleted Message", inline="True")
  channel = discord.utils.get(message.author.guild.channels, name="logs📚")
  await channel.send(embed=embed)


@client.event
async def on_message_edit(message_before, message_after):
  if(message_before.author.bot):
    return
  else:
    embed = discord.Embed(
      title=message_before.author.name,
      description=f"Message changed in **{message_before.channel}**",
      color=0xc2b280,
      timestamp=datetime.utcnow())
    embed.set_thumbnail(url=message_before.author.avatar)
    embed.add_field(name=message_before.content,
                    value="The message before",
                    inline="True")
    embed.add_field(name=message_after.content,
                    value="The message after",
                    inline="True")
    channel = discord.utils.get(message_before.author.guild.channels, name="logs📚")
    await channel.send(embed=embed)


with open('reports.json', encoding='utf-8') as f:
  try:
    report = json.load(f)
  except ValueError:
    report = {}
    report['users'] = []


@client.tree.command(name="help", description="A list of all slash commands")
async def help(interaction: discord.Interaction):
  embed = discord.Embed(title="Help",
                        color=0xc2b280,
                        timestamp=datetime.utcnow())
  embed.add_field(name="/help",
                  value="Shows list of slash commands",
                  inline=False)
  embed.add_field(name="/warnings",
                  value="Shows a users warnings",
                  inline=False)
  embed.add_field(name="/rps",
                  value="Play RPS with the CPU!",
                  inline=False)
  embed.add_field(name="/userinfo",
                  value="Get info on a certain user!",
                  inline=False)
  embed.set_footer(text="Help page 1/1")
  await interaction.response.send_message(embed=embed)


@client.tree.command(name="modhelp",
                     description="A list of all slash commands for moderation")
async def modhelp(interaction: discord.Interaction):
  embed = discord.Embed(title="Mod Help",
                        color=0xc2b280,
                        timestamp=datetime.utcnow())
  embed.add_field(name="/warn", value="Warn a certain user", inline=False)
  embed.add_field(name="/mute", value="Mute a certain user", inline=False)
  embed.add_field(name="/tempmute",
                  value="Temporarily mute a user",
                  inline=False)
  embed.add_field(name="/unmute", value="Unmute a user", inline=False)
  embed.add_field(name="/kick", value="Kick a certain user", inline=False)
  embed.add_field(name="/ban", value="Ban a certain user", inline=False)
  embed.set_footer(text="Help page 1/1")
  await interaction.response.send_message(embed=embed)


@client.tree.command(name="warn", description="Warn a certain user")
@app_commands.describe(user="User to warn", reason="Reason for warn")
async def warn(interaction: discord.Interaction, user: discord.User,
               reason: str):
  if not reason:
    await interaction.response.send_message("Please provide a reason")
    return
  for current_user in report['users']:
    if current_user['name'] == user.name:
      current_user['reasons'].append(reason)

  else:
    report['users'].append({
      'name': user.name,
      'reasons': [
        reason,
      ]
    })
  with open('reports.json', 'w+') as f:
    json.dump(report, f)

  channel = discord.utils.get(user.guild.channels, name="command-logs📚")
  embed = discord.Embed(title="Warn",
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


@client.tree.command(name="warnings", description="Shows a users warnings")
@app_commands.describe(user="List of users warnings")
async def warnings(interaction: discord.Interaction, user: discord.User):
  for current_user in report['users']:
    if user.name == current_user['name']:
      embed = discord.Embed(title="Warnings",
                            color=0xc2b280,
                            timestamp=datetime.utcnow())
      embed.set_thumbnail(url=user.avatar)
      embed.add_field(name="User", value=user.mention, inline=True)
      embed.add_field(name="# of warns",
                      value=len(current_user['reasons']),
                      inline=True)
      embed.add_field(name="Reasons",
                      value=', '.join(current_user['reasons']),
                      inline=True)
      await interaction.response.send_message(embed=embed)
      break
  else:
    em = discord.Embed(title="Warnings",
                       color=0xc2b280,
                       timestamp=datetime.utcnow())
    em.set_thumbnail(url=user.avatar)
    em.add_field(name="User", value=user.mention, inline=True)
    em.add_field(name="# of warns", value=0, inline=True)
    await interaction.response.send_message(embed=em)

load_dotenv('loadenv.env')

token = os.getenv("DISCORD_TOKEN")
keep_alive()

async def main():
  await load()

asyncio.run(main())

try:
  client.run(token)
except discord.errors.HTTPException:
  print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
  os.system('kill 1')
  os.system("python restarter.py")
