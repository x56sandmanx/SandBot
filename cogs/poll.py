import discord
from discord.ext import commands
from datetime import datetime, timedelta

numbers = ("1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟")
class Poll(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.polls=[]

    @commands.command()
    @commands.has_any_role("Mod", "SandKnight (Admin)", "Sandman")
    async def poll(self, ctx, hours: int, question: str, *options):
        if len(options) > 10:
            await ctx.send("You can only supply a maximum of 10 options!")
        else:
            embed = discord.Embed(title="Poll", description=question, colour=ctx.author.colour, timestamp=datetime.utcnow())
            fields =[("Options", "\n".join([f"{numbers[idx]} {option}" for idx, option in enumerate(options)]), False),
                    ("Instructions", "React to cast a vote!", False), ("End time", f"{datetime.now()+timedelta(seconds=hours)} EST", False)]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            
            message = await ctx.send(embed=embed)

            for emoji in numbers[:len(options)]:
                await message.add_reaction(emoji)

            self.polls.append((message.channel.id, message.id))

            self.client.scheduler.add_job(self.complete_poll, "date", run_date=datetime.now()+timedelta(seconds=hours), args=[message.channel.id, message.id])

    async def complete_poll(self, channel_id, message_id):
        message = await self.client.get_channel(channel_id).fetch_message(message_id)
        most_voted = max(message.reactions, key=lambda r: r.count)

        await message.channel.send(f"The results are in and option {most_voted.emoji} was the most popular vote with {most_voted.count-1:,} votes!")
        self.polls.remove((message.channel.id, message.id))
    
def setup(client):
    client.add_cog(Poll(client))
