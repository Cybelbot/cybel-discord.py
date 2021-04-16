"""
MIT License

Copyright (c) 2021 Deepak Raj

Bot-Name:- Cybel
Github:- https://github.com/codePerfectPlus/Cybel
Invite-Link:-
https://discord.com/api/oauth2/authorize?client_id=832137823309004800&permissions=268446835&scope=bot

"""
import os
import random
import discord
from discord import Intents
from discord.ext import commands
import requests
from dotenv import load_dotenv

from askme import askMe
load_dotenv()
print(f'Discord Version : {discord.__version__}')

# environment variables 
TOKEN = os.environ.get('DISCORD_TOKEN')
WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')

intents = Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    """ Change Bot Presense """
    await bot.change_presence(activity=discord.Game(name="Fornite"))
    print(f'{bot.user.name} is Online...')


@bot.event
async def on_message(message):
    """ some on_message command """
    if message.author.id == bot.user.id:
        return
    msg_content = message.content.lower()

    if msg_content.startswith('!ping'):
        await message.channel.send("Pong")
    if msg_content.startswith('!pong'):
        await message.channel.send("Ping")

    greet_message = ["hi", 'hello', 'hey']
    if any(word in msg_content for word in greet_message):
        await message.channel.send(random.choice(greet_message))
    
    curse_words = ["fuck"]
    if any(word in msg_content for word in curse_words):
        await message.delete()
        
    await bot.process_commands(message)


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together. !add 5 5"""
    await ctx.send(left + right)


@bot.command()
async def quote(ctx):
    """ function to send random quote """
    try:
        randomQuoteURL = 'https://zenquotes.io/api/random'
        response = requests.get(randomQuoteURL)
        randomQuote = f'{response.json()[0]["q"]} \
                      - **{response.json()[0]["a"]}**'
        await ctx.send(randomQuote)
    except Exception as error:
        await ctx.send(error)


@bot.command()
async def joke(ctx):
    """ function to send random joke """
    try:
        randomJokeURL = 'https://v2.jokeapi.dev/joke/Any?type=single'
        randomJoke = requests.get(randomJokeURL)
        await ctx.send(randomJoke.json()['joke'])
    except Exception as error:
        await ctx.send(error)


@bot.command()
async def fact(ctx):
    """ function to send random fact """
    try:
        randomFactURL = 'https://uselessfacts.jsph.pl//random.json?language=en'
        randomFact = requests.get(randomFactURL)
        await ctx.send(randomFact.json()['text'])
    except Exception as error:
        await ctx.send(error)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command()
async def weather(ctx, *args):
    """ Get Your City weather example:- !weather New Delhi"""
    city_name = ' '.join(args)
    openWeatherURL = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={WEATHER_API_KEY}"
    
    try:
        weather_data = requests.get(openWeatherURL).json()

        await ctx.send(f'{city_name.title()} - "Country": {weather_data["city"]["country"]}')
        await ctx.send(f'"Temp": {round(weather_data["list"][0]["main"]["temp"] -273.0)}')
        await ctx.send(f'"temp_min": {round(weather_data["list"][0]["main"]["temp_min"] -273.0)}')
        await ctx.send(f'"temp_max": {round(weather_data["list"][0]["main"]["temp_max"] -273.0)}')
        await ctx.send(f'"pressure": {weather_data["list"][0]["main"]["pressure"]}')
        await ctx.send(f'"humidity": {weather_data["list"][0]["main"]["humidity"]}')
        await ctx.send(f'"sea_level":{weather_data["list"][0]["main"]["sea_level"]}')
                        
    except Exception:
        await ctx.send("I didn't find your City")


@bot.command(name="cybel")
async def cybel(ctx, *args):
    """ I am Cybel. Ask me question related of science, math and general conversation """
    userQuestion = ' '.join(args)
    print(userQuestion)
    botResponse = askMe(userQuestion)
    await ctx.send(botResponse)

@bot.command(name="q")
async def questionMe(ctx, *args):
    """ I am Cybel. Ask me question related of science, math and general conversation """
    userQuestion = ' '.join(args)
    print(userQuestion)
    botResponse = askMe(userQuestion)
    await ctx.send(botResponse)

""" Credits """
bot_details = f'''BotName:- Cybel\n\
Creator:- Deepak Raj\n\
Contact Email:- Deepak008@live.com\n\
Discord Server:- https://discord.gg/JfbK3bS\n\
GitHub:- https://github.com/codeperfectplus'''

@bot.command(name="info")
async def bot_info(ctx):
    """ Information about the Bot and credits """
    await ctx.send(bot_details)


if __name__ == '__main__':
    bot.run(TOKEN)
