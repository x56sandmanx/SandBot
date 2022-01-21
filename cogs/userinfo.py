import discord
from discord.ext import commands
from discord import Embed, Member
from typing import Optional
from datetime import datetime

class Userinfo(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def userInfo(self, ctx, target: Optional[Member]):
	  target = target or ctx.author

	  embed = Embed(title="User information",
					  colour=target.colour,
					  timestamp=datetime.utcnow())

	  embed.set_thumbnail(url=target.avatar_url)

	  fields = [("Name", str(target), True),
				  ("ID", target.id, True),
				  ("Bot?", target.bot, True),
				  ("Top role", target.top_role.mention, True),
				  ("Status", str(target.status).title(), True),
				  ("Activity", f"{str(target.activity.type).split('.')[-1].title() if target.activity else 'N/A'} {target.activity.name if target.activity else ''}", True),
				  ("Created on", target.created_at.strftime("%m/%d/%Y"), True),
				  ("Joined on", target.joined_at.strftime("%m/%d/%Y"), True),
				  ("Boosted", bool(target.premium_since), True)]

	  for name, value, inline in fields:
		  embed.add_field(name=name, value=value, inline=inline)

	  await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Userinfo(client))