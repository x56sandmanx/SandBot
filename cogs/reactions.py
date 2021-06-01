import discord
from discord.ext import commands

class Reaction(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id
        if message_id == 845362897592778813:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

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

    async def on_raw_reaction_remove(self, payload):
        message_id = payload.message_id
        if message_id == 845362897592778813:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

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
    
def setup(client):
    client.add_cog(Reaction(client))
