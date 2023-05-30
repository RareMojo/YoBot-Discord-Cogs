import discord
from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        """A simple command that replies with a greeting."""
        await ctx.send("Hello, world!")

def setup(bot):
    bot.add_cog(MyCog(bot))