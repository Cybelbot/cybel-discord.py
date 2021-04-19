"""
MIT License

Copyright (c) 2021 Deepak Raj

Bot-Name:- Cybel
Github:- https://github.com/codePerfectPlus/Cybel
Invite-Link:-
https://discord.com/api/oauth2/authorize?client_id=832137823309004800&permissions=142337&scope=bot
"""

from discord import Intents
from discord.ext import commands

from src.utils import utils

TOKEN = utils.TOKEN

intents = Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!",
                   intents=intents,
                   case_insensitive=True)

# load cogs
bot.load_extension("src.cogs.admin")
bot.load_extension("src.cogs.user")
bot.load_extension("src.cogs.auto")

if __name__ == '__main__':
    bot.run(TOKEN)