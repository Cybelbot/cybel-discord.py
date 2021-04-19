"""
MIT License

Copyright (c) 2021 Deepak Raj

Bot-Name:- Cybel
Github:- https://github.com/codePerfectPlus/Cybel
Invite-Link:-
https://discord.com/api/oauth2/authorize?client_id=832137823309004800&permissions=142337&scope=bot

"""
import discord
from discord.ext import commands

from src.utils import askme

class ExperimentalCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="cybel", help="General conversation command")
    async def cybel(self, ctx, *args):
        """ I am Cybel. Ask me question related of science, math and general conversation """
        async with ctx.typing():
            user_question = ' '.join(args)
            bot_response = askme.askMe(user_question)
            await ctx.send(bot_response)


def setup(bot: commands.Bot):
    bot.add_cog(ExperimentalCommands(bot))
