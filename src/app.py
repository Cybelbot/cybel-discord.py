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
import utils

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

    if msg_content.startswith('ping'):
        await message.channel.send("Pong")
    if msg_content.startswith('pong'):
        await message.channel.send("Ping")
    
    curse_words = ["fuck"]
    if any(word in msg_content for word in curse_words):
        await message.delete()
        
    await bot.process_commands(message)


@bot.command(name="quote", help="get amazing random quote")
async def quote(ctx):
    """ Get amazing random quote """
    randomQuote = utils._getRandomQuote()
    await ctx.send(randomQuote)


@bot.command(name="joke", help="get random jokes")
async def joke(ctx):
    """ Get random jokes """
    randomJoke = utils._getRanomJoke()
    await ctx.send(randomJoke)


@bot.command(name="fact", help="get amazing random fact")
async def fact(ctx):
    """ Get amazing random fact """
    randomFact = utils._getRandomFact()
    await ctx.send(randomFact)


@bot.command(name="roll", help="roll a dice in NdN format. 5d5")
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    result = utils._rollTheDice(dice)
    await ctx.send(result)


@bot.command(name="weather", help="weather of world at your command")
async def weather(ctx, *args):
    """ Get Your City weather example:- !weather New Delhi"""
    city_name = ' '.join(args)
    openWeatherURL = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={WEATHER_API_KEY}"
    
    try:
        weather_data = requests.get(openWeatherURL).json()

        await ctx.send(f'{city_name.title()} - Country: {weather_data["city"]["country"]}')
        await ctx.send(f'Temp: {round(weather_data["list"][0]["main"]["temp"] -273.0)}')
        await ctx.send(f'temp_min: {round(weather_data["list"][0]["main"]["temp_min"] -273.0)}')
        await ctx.send(f'temp_max: {round(weather_data["list"][0]["main"]["temp_max"] -273.0)}')
        await ctx.send(f'pressure: {weather_data["list"][0]["main"]["pressure"]}')
        await ctx.send(f'humidity: {weather_data["list"][0]["main"]["humidity"]}')
        await ctx.send(f'sea_level:{weather_data["list"][0]["main"]["sea_level"]}')
                        
    except Exception:
        await ctx.send("I didn't find your City")


@bot.command(name="surl", help="shorten your url. use https/http")
async def shortenURL(ctx, website: str):
    """ Shorten Your Url using cleanURL API !surl <website> """
    shortURL = utils._UrlShortner(website)
    await ctx.send(f"Your Short URL is\n{shortURL}")


@bot.command(name="gh", help="get Github user data")
async def githubAPI(ctx, username: str):
    """ Get Github User Data Using !gh username """
    userData = utils._getGitUserData(username)
    await ctx.send(f'Name: {userData["name"]}\nPublic Repo: {userData["public_repos"]}\nFollowers: {userData["followers"]}\nLast Updated: {userData["updated_at"]}')


@bot.command(name="ifsc", help="Get Indian Bank Branch details by IFSC Code")
async def getBankDataByIFSC(ctx, ifsc_code: str):
    """ Get Bank Details by IFSC CODE In INdia !ifsc <ifsc_code> """
    bankData = utils._getIfscDetails(ifsc_code)
    await ctx.send(f'Branch: {bankData["BRANCH"]}\n\Bank: {bankData["BANK"]}\nDistrict: {bankData["DISTRICT"]}\nState: {bankData["STATE"]}\nContact Number: {bankData["CONTACT"]}')


@bot.command(name="dogs", help="Get Random Pictures of Dogs")
async def dogs(ctx):
    """ Get Random Dogs Picture """
    embed = utils._getRandomDogPicture()
    await ctx.send(embed=embed)


@bot.command(name="cats", help="Get Random Pictures of Cats")
async def cats(ctx):
    """ Get Random Cats Picture """
    embed = utils._getRandomCatPicture()
    await ctx.send(embed=embed)


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
