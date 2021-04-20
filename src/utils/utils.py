"""
MIT License

Copyright (c) 2021 Deepak Raj

Bot-Name:- Cybel
Github:- https://github.com/codePerfectPlus/Cybel
Invite-Link:-
https://discord.com/api/oauth2/authorize?client_id=832137823309004800&permissions=142337&scope=bot
"""

import os
import discord
import aiohttp
from dotenv import load_dotenv

load_dotenv()

BOTNAME = "Cybel"

print(f'Discord Version : {discord.__version__}')

# environment variables 
TOKEN = os.environ.get('DISCORD_TOKEN')
WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')

async def _fetch(url):
    """ function to fetch data from api in asynchronous way """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()