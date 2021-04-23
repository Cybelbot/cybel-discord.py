"""
MIT License

Copyright (c) 2021 Deepak Raj

Bot-Name:- Cybel
Github:- https://github.com/codePerfectPlus/Cybel
Invite-Link:-
https://discord.com/api/oauth2/authorize?client_id=832137823309004800&permissions=142337&scope=bot
"""

import os
import sys
import discord
import aiohttp
from dotenv import load_dotenv
import logging

load_dotenv()

BOTNAME = "Cybel"

logging.basicConfig(format='%(levelname)s: %(asctime)s %(message)s',
					datefmt='%d/%m/%Y %I:%M:%S %p',
					level=logging.INFO)

logging.info(f'Discord Version : {discord.__version__}')

# environment variables
def get_environment_variable(key: str):
	""" Get the Environment variables """
	value = os.environ.get(key)
	try:
		if value is not None:
			logging.info(f'Loading... {key}')
			return value
	except Exception:
		logging.critical(f"{key} is not found in environment variable.")

DISCORD_TOKEN = get_environment_variable('DISCORD_TOKEN') # API_KEY:- https://discord.com/developers/applications/
WEATHER_API_KEY = get_environment_variable('WEATHER_API_KEY') # API_KEY:- https://openweathermap.org/

async def _fetch(url: str):
	""" function to fetch data from api in asynchronous way """
	async with aiohttp.ClientSession() as session:
		async with session.get(url) as response:
			if response.status == 200:
				return await response.json()

# Weather image list used in weather embed to send random image 
weather_image_list = [
	'https://cdn.discordapp.com/attachments/831943037936467985/834165838545551380/image.jpg',
	'https://cdn.discordapp.com/attachments/831943037936467985/834166839264149504/2019mexicoweather-forecast-v02.jpg',
	'https://cdn.discordapp.com/attachments/831943037936467985/834166849309769758/Austria2020weather-forecast-v02.jpg',
	'https://cdn.discordapp.com/attachments/831943037936467985/834166850169471067/Germany_weather.jpg',
	'https://cdn.discordapp.com/attachments/831943037936467985/834166848202735657/image_2.jpg',
	'https://cdn.discordapp.com/attachments/831943037936467985/834166848404324379/image_1.jpg',
	'https://cdn.discordapp.com/attachments/831943037936467985/834166851226304552/image_3.jpg']