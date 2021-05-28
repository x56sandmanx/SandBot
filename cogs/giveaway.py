import discord
from discord.ext import commands
from datetime import datetime, timedelta
from random import choice

numbers = ("1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟")
class Giveaway(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.giveaways = []

    @commands.command()
    @commands.has_any_role("Mod", "SandKnight (Admin)", "Sandman")
    async def giveaway(self, ctx, mins: int, *, description: str):
        embed = discord.Embed(title="Giveaway", description=description, colour = ctx.author.colour, timestamp=datetime.utcnow())
        fields = [("End time", f"{datetime.now()+timedelta(seconds=mins*60)} EST", False)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        message = await ctx.send(embed=embed)
        await message.add_reaction("✅")

        self.giveaways.append((message.channel.id, message.id))
        self.bot.scheduler.add_job(self.complete_giveaway, "date", run_date=datetime.now()+timedelta(seconds=mins), args=[message.channel.id, message.id])

    async def complete_giveaway(self, channel_id, message_id):
        message = await self.client.get_channel(channel_id).fetch_message(message_id)

        if len((entrants := [u for u in await message.reactions[0].users().flatten() if not u.client])) > 0:
            winner = choice(entrants)
            await message.channel.send(f"Congratulations {winner.mention} - you won the Giveaway!")
            self.giveaways.remove((message.channel.id, message.id))
        else:
            await message.channel.send("Giveaway ended - no one entered!")
            self.giveaways.remove((message.channel.id, message.id))

    
    
def setup(client):
    client.add_cog(Giveaway(client))