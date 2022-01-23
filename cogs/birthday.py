import discord
from discord.ext import commands
import json
import datetime
import asyncio

class Birthday(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def setbirthday(self, ctx):
        member = ctx.message.author.id
        await ctx.send("Please enter the month of your birthday in MM format")
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel
        month = await self.client.wait_for("message", check=check)
        if int(month.content) > 13 or int(month.content) < 1:
            await ctx.send("Invalid month")
            return
        else:
            pass
        
        await ctx.send("Please enter the day of your birthday in DD format")
        day = await self.client.wait_for("message", check=check)
        if int(month.content) == 1 or int(month.content) == 3 or int(month.content) == 5 or int(month.content) == 7 or int(month.content) == 8 or int(month.content) == 10 or int(month.content) == 12:
            if int(day.content) > 31 or int(day.content) < 1:
                await ctx.send("Invalid day for the month")
                return
            else:
                dict={"member": member,
                      "month": int(month.content),
                      "day": int(day.content)}
                with open("birthday.json","a") as f:
                    json.dump(dict,f)
                await ctx.send(f"Your birthday is now set on {int(month.content)}/{int(day.content)}!")
        elif int(month.content) == 4 or int(month.content) == 6 or int(month.content) == 9 or int(month.content) == 11:
            if int(day.content) > 30 or int(day.content) < 1:
                await ctx.send("Invalid day for the month")
                return
            else:
                dict={"member": member,
                      "month": month.content,
                      "day": day.content}
                with open("birthday.json","a") as f:
                    json.dump(dict,f)
                await ctx.send(f"Your birthday is now set on {int(month.content)}/{int(day.content)}!")
        elif int(month.content) == 2:
            if int (day.content) > 28 or int(day.content) < 1:
                await ctx.send("Invalid day for the month")
                return
            else:
                dict={"member": member,
                      "month": month.content,
                      "day": day.content}
                with open("birthday.json","a") as f:
                    json.dump(dict,f)
                await ctx.send(f"Your birthday is now set on {int(month.content)}/{int(day.content)}!")
        else:
            await ctx.send("Invalid input")
    
    @commands.command()
    async def birthday(self,ctx):
        now = datetime.datetime.now()
        currmonth = now.month
        currday = now.day
        
        with open("birthday.json","r") as f:
            var = json.loads(f)
            for member in var:
                if member['month'] == currmonth:
                    if member['day'] == currday:
                        await ctx.send("it is ur bday bro")
                    else:
                        await ctx.send("it no bday today")
            


def setup(client):
  client.add_cog(Birthday(client))