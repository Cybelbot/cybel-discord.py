'''
MIT License

Copyright (c) 2021 Deepak Raj

Bot-Name:- Cybel
Github:- https://github.com/codePerfectPlus/Cybel
Invite-Link:-
https://discord.com/api/oauth2/authorize?client_id=832137823309004800&permissions=142337&scope=bot
'''

from discord import Intents
from discord.ext import commands

from src.utils import utils

intents = Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!',
                   intents=intents,
                   case_insensitive=True)

cog_dict = {
    'Auto Commands': 'src.cogs.autoCommands',
    'Admin Commands': 'src.cogs.adminCommands',
    'Experimental Commands': 'src.cogs.experimentalCommands',
    'API Based Commands': 'src.cogs.apiBasedCommands',
    'Other Commands': 'src.cogs.otherCommands'
}


for key, value in cog_dict.items():
    print(f'[INFO]: Loading... {key}')
    bot.load_extension(value)


if __name__ == '__main__':
    bot.run(utils.DISCORD_TOKEN)
