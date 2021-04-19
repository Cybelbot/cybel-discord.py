import os
import discord
from dotenv import load_dotenv

load_dotenv()

BOTNAME = "Cybel"

print(f'Discord Version : {discord.__version__}')

# environment variables 
TOKEN = os.environ.get('DISCORD_TOKEN')
WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')