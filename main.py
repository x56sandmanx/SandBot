import discord
import os
from discord import member
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType, CommandOnCooldown
from discord.ext.commands import MissingPermissions
from discord.errors import Forbidden
from discord.utils import get
from datetime import datetime
from discord import Member
from typing import Optional
import json
intents = discord.Intents().all()
client = commands.Bot(intents=intents, command_prefix='-')
client.remove_command('help')

illegal_words = ["nigger", "nigga", "fag", "faggot", "retard"]

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game("-help | SandBot v1.6.4"))
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member:discord.Member):
    channel=client.get_channel(797284193621114900)
    channel2=client.get_channel(845362775974477854)
    channel3=client.get_channel(797282913187659796)
    embed=discord.Embed(title="The Sand Kingdom", description= f"Welcome to The Sand Kingdom {member.mention}, make sure to head to {channel2.mention} to get your roles and go to {channel3.mention} to check out the rules!",color=discord.Color.blue(),timestamp=datetime.utcnow())
    embed.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed)
    role = discord.utils.get(member.guild.roles, name="Sandling")
    await member.add_roles(role)

@client.event
async def on_message(message):
    if any(word in message.content.lower().replace(' ', '') for word in illegal_words):
        await message.delete()
    else:
        await client.process_commands(message)
    
@client.event
async def on_message_delete(message):
    embed=discord.Embed(title=message.author.name, description=f"Message deleted in **{message.channel}**", color=discord.Color.blue(),timestamp=datetime.utcnow())
    embed.add_field(name = message.content, value="Deleted Message", inline="True")
    channel=client.get_channel(799074188039946250)
    await channel.send(embed=embed)

@client.event
async def on_message_edit(message_before, message_after):
    embed=discord.Embed(title=message_before.author.name, description=f"Message changed in **{message_before.channel}**", color=discord.Color.blue(),timestamp=datetime.utcnow())
    embed.add_field(name=message_before.content, value="The message before",inline="True")
    embed.add_field(name=message_after.content, value="The message after",inline="True")
    channel=client.get_channel(799074188039946250)
    await channel.send(embed=embed)

@client.event
async def on_command_error(ctx, exc):
    if isinstance(exc, CommandOnCooldown):
        await ctx.send(f"That command is on cooldown. Try again in {exc.retry_after//60+1:,.2f} minutes")
    elif isinstance(exc, Forbidden):
        await ctx.send("You do not have permission to do that.")

with open('reports.json', encoding='utf-8') as f:
  try:
    report = json.load(f)
  except ValueError:
    report = {}
    report['users'] = []

@client.command(pass_context = True)
@commands.has_any_role("SandGuard (Mod)", "SandKnight (Admin)", "Sandman")
async def warn(ctx,user:discord.User,*reason:str):
    if not reason:
        await ctx.send("Please provide a reason")
        return
    reason = ' '.join(reason)
    for current_user in report['users']:
        if current_user['name'] == user.name:
            current_user['reasons'].append(reason)
        
    else:
        report['users'].append({
        'name':user.name,
        'reasons': [reason,]
    })
    with open('reports.json','w+') as f:
        json.dump(report,f)

    channel = client.get_channel(886329173877080144)
    embed=discord.Embed(title="Warn", color=discord.Color.blue(),timestamp=datetime.utcnow())
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="User", value=user.mention, inline=True)
    embed.add_field(name="Moderator", value=ctx.message.author.mention, inline=True)
    embed.add_field(name="Reason", value=reason, inline=True)
    await channel.send(embed=embed)

@client.command(pass_context = True)
async def warnings(ctx,user:discord.User):
    for current_user in report['users']:
        if user.name == current_user['name']:
            embed=discord.Embed(title="Warnings", color=discord.Color.blue(), timestamp=datetime.utcnow())
            embed.set_thumbnail(url=user.avatar_url)
            embed.add_field(name="User", value=user.mention, inline=True)
            embed.add_field(name="# of warns", value=len(current_user['reasons']), inline=True)
            embed.add_field(name="Reasons", value=','.join(current_user['reasons']), inline=True)
            await ctx.send(embed=embed)
            break
    else:
        em=discord.Embed(title="Warnings", color=discord.Color.blue(), timestamp=datetime.utcnow())
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="User", value=user.mention, inline=True)
        em.add_field(name="# of warns", value=0, inline=True)
        await ctx.send(embed=em)

@warn.error
async def kick_error(error, ctx):
  if isinstance(error, MissingPermissions):
      text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
      await client.send_message(ctx.message.channel, text)

token = os.environ.get('TOKEN')
client.run('ODE5NzI1ODQ4OTQ3OTgyNDQ2.YEqzMA.PMqLQGlgbfLoqczH7PhmgCzRSMk')
