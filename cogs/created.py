import discord
from discord.ext import commands
from datetime import datetime

class CreatedAt(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def created_at(self, message, id):
        user = await self.client.fetch_user(id)
        await message.channel.send(datetime.fromtimestamp(user.created_at.timestamp()).strftime("%A, %B %d, %Y %I:%M:%S"))


async def setup(bot):
    await bot.add_cog(CreatedAt(bot))
