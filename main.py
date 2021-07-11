import discord
import os
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType, CommandOnCooldown
from discord.errors import Forbidden
from discord.utils import get
import json
import random
import os

intents = discord.Intents().all()
client = commands.Bot(intents=intents, command_prefix='-')
client.remove_command('help')

mainshop = [{"name":"Watch","price":100,"description":"A watch"},
            {"name":"Sandgun","price":1000,"description":"A tiny sandgun that probably couldn't even kill a fly..."},
            {"name":"Sand Dollar","price":99999999,"description":"A Sand Dollar.... that costs more than a dollar..."}]

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
                                 activity=discord.Game("-help | SandBot v1.6.2"))
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="welcome👋")
    await channel.send(
        f"Welcome to **{member.guild.name}** {member.mention}! Head over to <#797282653946642474> to be cool! Also go to <#845362775974477854> to get your roles!"
    )
    role = discord.utils.get(member.guild.roles, name="Sandling")
    await member.add_roles(role)

@client.command()
async def joblist(ctx):
    em=discord.Embed(title="The Sand Kingdom Joblist", color=discord.Color.blue())
    em.add_field(name="Sand Gatherer",value="Gather grains of sand | PAY: $50",inline=True)
    em.add_field(name="SandTuber",value="Upload videos of the Sand Kingdom and make money | PAY: $100",inline=True)
    await ctx.send(embed=em)

@client.command()
async def job(ctx):
    await ctx.send("What job would you like to apply for?")
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel
    
    user_input = await client.wait_for("message",check=check)
    if(user_input.content=="Sand Gatherer"):
        await ctx.send("Applied for Sand Gatherer!")
    if(user_input.content=="SandTuber"):
        await ctx.send("Applied for SandTuber!")
    else:
        await ctx.send("Input valid job!")

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
        await ctx.send("Please enter the amount")
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
        await ctx.send("Please enter the amount")
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

@client.command()
async def shop(ctx):
    em = discord.Embed(title = "The Sand Shop")

    for item in mainshop:
        name = item["name"]
        price = item["price"]
        description = item["description"]
        em.add_field(name = name, value = f"${price} | {description}", inline=False)

    await ctx.send(embed=em)

@client.command()
async def buy(ctx, item, amount=1):
    await open_account(ctx.author)

    res = await buy_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have enough money to buy {amount}")
            return

    await ctx.send(f"You just bought {amount} {item}")

@client.command()
async def bag(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await getBankData()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag=[]

    em = discord.Embed(title="Bag")
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name=name,value=amount)
    
    await ctx.send(embed=em)

async def buy_this(user, item_name,amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name==item_name:
            name_=name
            price=item["price"]
            break

    if name_==None:
        return [False, 1]

    cost = price*amount
    users = await getBankData()
    bal = await updateBank(user)
    if bal[0]<cost:
        return [False,2]

    try:
        index=0
        t=None
        for thing in users[str(user.id)]["bag"]:
            n=thing["item"]
            if n==item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t=1
                break
            index+=1
        if t == None:
            obj = {"item":item_name,"amount":amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item":item_name,"amount":amount}
        users[str(user.id)]["bag"]=[obj]

    with open("bank.json","w") as f:
        json.dump(users,f)

    await updateBank(user,cost*-1,"wallet")

    return [True,"Worked"]

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

token = os.environ.get('TOKEN')
client.run('ODE5NzI1ODQ4OTQ3OTgyNDQ2.YEqzMA.PMqLQGlgbfLoqczH7PhmgCzRSMk')
