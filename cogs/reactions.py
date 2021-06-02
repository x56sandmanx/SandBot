import discord
from discord.ext import commands
from discord.utils import get

class Reaction(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id
        if message_id == 845362897592778813:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)
            if payload.emoji.name == 'nsfw':
                role = discord.utils.get(guild.roles, name='NSFW')
            elif payload.emoji.name =='boy':
                role = discord.utils.get(guild.roles, name='13-16')
            elif payload.emoji.name=='teen':
                role = discord.utils.get(guild.roles, name='17-19')
            elif payload.emoji.name=='man':
                role = discord.utils.get(guild.roles, name='20+')
            elif payload.emoji.name=='male_sign':
                role = discord.utils.get(guild.roles, name='Male')
            elif payload.emoji.name=='female_sign':
                role = discord.utils.get(guild.roles, name='Female')
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role is not None:
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
        
        if message_id == 849444754390646814:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)
            if payload.emoji.name == 'blue_color':
                role = discord.utils.get(guild.roles, name='blue')
            elif payload.emoji.name =='red_color':
                role = discord.utils.get(guild.roles, name='red')
            elif payload.emoji.name=='green_color':
                role = discord.utils.get(guild.roles, name='green')
            elif payload.emoji.name=='yellow_color':
                role = discord.utils.get(guild.roles, name='yellow')
            elif payload.emoji.name=='purple_color':
                role = discord.utils.get(guild.roles, name='purple')
            elif payload.emoji.name=='black_color':
                role = discord.utils.get(guild.roles, name='black')
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role is not None:
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        message_id = payload.message_id
        if message_id == 845362897592778813:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)

            if payload.emoji.name == 'nsfw':
                role = discord.utils.get(guild.roles, name='NSFW')
            elif payload.emoji.name =='boy':
                role = discord.utils.get(guild.roles, name='13-16')
            elif payload.emoji.name=='teen':
                role = discord.utils.get(guild.roles, name='17-19')
            elif payload.emoji.name=='man':
                role = discord.utils.get(guild.roles, name='20+')
            elif payload.emoji.name=='male_sign':
                role = discord.utils.get(guild.roles, name='Male')
            elif payload.emoji.name=='female_sign':
                role = discord.utils.get(guild.roles, name='Female')
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role is not None:
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
        
        if message_id == 849444754390646814:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)
            if payload.emoji.name == 'blue_color':
                role = discord.utils.get(guild.roles, name='blue')
            elif payload.emoji.name =='red_color':
                role = discord.utils.get(guild.roles, name='red')
            elif payload.emoji.name=='green_color':
                role = discord.utils.get(guild.roles, name='green')
            elif payload.emoji.name=='yellow_color':
                role = discord.utils.get(guild.roles, name='yellow')
            elif payload.emoji.name=='purple_color':
                role = discord.utils.get(guild.roles, name='purple')
            elif payload.emoji.name=='black_color':
                role = discord.utils.get(guild.roles, name='black')
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role is not None:
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
    
def setup(client):
    client.add_cog(Reaction(client))
