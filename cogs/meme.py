import discord
import praw
import random
from discord.ext import commands

reddit = praw.Reddit(client_id="5Sdfrb3Nyeb03w", client_secret = "HGGh6bCcWwR3N2Li7_Ul2OS8_3-fhA", username="xx56sandmanxx", password="SnareDrummer123", user_agent="pythonpraw")

class Meme(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def meme(self, ctx):
    subreddit = reddit.subreddit("memes")
    all_subs = []
    top = subreddit.top(limit = 50)
    for submission in top:
      all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    em = discord.Embed(title = name)
    em.set_image(url = url)

    await ctx.send(embed=em)

def setup(client):
  client.add_cog(Meme(client))