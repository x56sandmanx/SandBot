import discord
import os
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType, CommandOnCooldown
from discord.errors import Forbidden
import json
import random
import os
#from keep_alive import keep_alive

intents = discord.Intents().all()
client = commands.Bot(intents=intents, command_prefix='-')
client.remove_command('help')


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
                                 activity=discord.Game("-help | SandBot v1.3"))
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="welcome")
    await channel.send(
        f"Welcome to **{member.guild.name}** {member.mention}! Head over to <#797282653946642474> to be cool!"
    )
    role = discord.utils.get(member.guild.roles, name="Sandling")
    await member.add_roles(role)

@client.command()
async def bal(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await getBankData()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    em =discord.Embed(title=f"{ctx.author.name}'s balance",color=discord.Color.blue())
    em.add_field(name="Wallet",value=f"${wallet_amt}")
    em.add_field(name="Bank",value=f"${bank_amt}")
    await ctx.send(embed=em)

@client.command()
@commands.cooldown(1, 300, commands.BucketType.user)
async def beg(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await getBankData()

    earnings = random.randrange(101)
    await ctx.send(f"Someone gave you ${earnings}!")

    users[str(user.id)]["wallet"] += earnings

    with open("bank.json","w") as f:
        json.dump(users,f)


@client.command()
async def withdraw(ctx,amount=None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.sned("Please enter the amount")
        return
    bal = await updateBank(ctx.author)

    amount = int(amount)
    if amount>bal[1]:
        await ctx.send("You don't have that much money!")
        return
    if amount<0:
        await ctx.send("Amount must be positive!")
        return
    await updateBank(ctx.author,amount)
    await updateBank(ctx.author,-1*amount,"bank")
    await ctx.send(f"You withdrew {amount} dollars!")

@client.command()
async def deposit(ctx,amount=None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.sned("Please enter the amount")
        return
    bal = await updateBank(ctx.author)

    amount = int(amount)
    if amount>bal[0]:
        await ctx.send("You don't have that much money!")
        return
    if amount<0:
        await ctx.send("Amount must be positive!")
        return
    await updateBank(ctx.author,-1*amount)
    await updateBank(ctx.author,amount,"bank")
    await ctx.send(f"You deposited {amount} dollars!")

async def open_account(user):
    users = await getBankData()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)]={}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open("bank.json","w") as f:
        json.dump(users,f)
    return True

async def getBankData():
    with open("bank.json","r") as f:
        users = json.load(f)

    return users

async def updateBank(user,change=0,mode="wallet"):
    users = await getBankData()

    users[str(user.id)][mode] += change

    with open("bank.json","w") as f:
        json.dump(users,f)
    bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
    return bal

@client.event
async def on_command_error(ctx, exc):
    if isinstance(exc, CommandOnCooldown):
        await ctx.send(f"That command is on cooldown. Try again in {exc.retry_after//60+1:,.2f} minutes")
    elif isinstance(exc, Forbidden):
        await ctx.send("You do not have permission to do that.")


#with open('token.txt') as f:
 #   TOKEN = f.readline()
token = os.environ.get('TOKEN')
#keep_alive()
client.run(token)
