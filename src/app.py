"""
MIT License

Copyright (c) 2021 Deepak Raj

Bot-Name:- Cybel
Github:- https://github.com/codePerfectPlus/Cybel
Invite-Link:-
https://discord.com/api/oauth2/authorize?client_id=832137823309004800&permissions=268446835&scope=bot

"""
import re
import random
import discord
from discord import Intents
from discord.ext import commands
import aiohttp

from askme import askMe
import utils

intents = Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
	""" Change Bot Presense """
	await bot.change_presence(activity=discord.Game(name="Fornite"))
	print(f'{bot.user.name} is Online...')


@bot.event
async def on_message(message: str):
	""" on_message command """
	if message.author.id == bot.user.id:
		return
	msg_content = message.content.lower()

	if msg_content.startswith('ping'):
		await message.channel.send("Pong")
	if msg_content.startswith('pong'):
		await message.channel.send("Ping")

	await bot.process_commands(message)


@bot.command(name="quote", help="get amazing random quote")
async def getRandomQuote(ctx):
	""" Get amazing random quote """
	randomQuoteURL = 'https://zenquotes.io/api/random'
	async with ctx.typing():
		async with aiohttp.ClientSession() as session:
			async with session.get(randomQuoteURL) as response:
				result = await response.json()
				randomQuote = f'{result[0]["q"]} -**{result[0]["a"]}**'
				await ctx.send(randomQuote)


@bot.command(name="joke", help="get random jokes")
async def getRandomJoke(ctx):
	""" Get random jokes """
	randomJokeURL = 'https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single'
	async with ctx.typing():
		async with aiohttp.ClientSession() as session:
			async with session.get(randomJokeURL) as response:
				randomJoke = await response.json()["joke"]
				await ctx.send(randomJoke)


@bot.command(name="fact", help="get amazing random fact")
async def getRandomFact(ctx):
	""" Get amazing random fact """
	randomFactURL = 'https://uselessfacts.jsph.pl//random.json?language=en'
	async with ctx.typing():
		async with aiohttp.ClientSession() as session:
			async with session.get(randomFactURL) as response:
				randomFact = await response.json()['text']
				await ctx.send(randomFact)


@bot.command(name="cats", help="Get Random Pictures of Cats")
async def getRandomcCatPicture(ctx):
	""" Get Random Cats Picture """
	catAPIURL = "https://thatcopy.pw/catapi/rest/"
	async with ctx.typing():
		async with aiohttp.ClientSession() as session:
			async with session.get(catAPIURL) as response:
				result = await response.json()

				catPictureURL = result["url"]
				embed = discord.Embed(title="Meow")
				embed.set_image(url=catPictureURL)
				await ctx.send(embed=embed)


@bot.command(name="roll", help="roll a dice in NdN format. 5d5")
async def rollTheDice(ctx, dice: str):
	"""Rolls a dice in NdN format."""
	try:
		rolls, limit = map(int, dice.split('d'))
	except Exception:
		return 'Format has to be in NdN!'

	result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
	await ctx.send(result)


@bot.command(name="gh", help="get Github user data")
async def getGihubUserData(ctx, username: str):
	""" Get Github User Data Using !gh username """
	async with ctx.typing():
		gitAPIURL = f'https://api.github.com/users/{username}'
		async with aiohttp.ClientSession() as session:
			async with session.get(gitAPIURL) as response:
				userData = await response.json()
				await ctx.send(f'Name: {userData["name"]}\nPublic Repo: {userData["public_repos"]}\nFollowers: {userData["followers"]}\nLast Updated: {userData["updated_at"]}')


@bot.command(name="ifsc", help="Get Indian Bank Branch details by IFSC Code")
async def getBankDataByIFSC(ctx, ifsc_code: str):
	""" Get Bank Details by IFSC CODE In INdia !ifsc <ifsc_code> """
	url = f"https://ifsc.razorpay.com/{ifsc_code}"
	async with ctx.typing():
		async with aiohttp.ClientSession() as session:
			async with session.get(url) as response:
				bankData = await response.json()
				await ctx.send(f'Branch: {bankData["BRANCH"]}\nBank: {bankData["BANK"]}\nDistrict: {bankData["DISTRICT"]}\nState: {bankData["STATE"]}\nContact Number: {bankData["CONTACT"]}')


@bot.command(name="weather", help="weather of world at your command")
async def getWeather(ctx, *args):
	""" Get Your City weather example:- !weather New Delhi"""
	city_name = ' '.join(args)
	async with ctx.typing():
		openWeatherURL = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={utils.WEATHER_API_KEY}"
		async with aiohttp.ClientSession() as session:
			async with session.get(openWeatherURL) as response:
				if response.status == 200:
					weather_data = await response.json()

					await ctx.send(f'{city_name.title()} - Country: {weather_data["city"]["country"]}\n\
									Temp: {round(weather_data["list"][0]["main"]["temp"] -273.0)}\n\
									temp_min: {round(weather_data["list"][0]["main"]["temp_min"] -273.0)}\n\
									temp_max: {round(weather_data["list"][0]["main"]["temp_max"] -273.0)}\n\
									pressure: {weather_data["list"][0]["main"]["pressure"]}\n\
									humidity: {weather_data["list"][0]["main"]["humidity"]}\n\
									sea_level:{weather_data["list"][0]["main"]["sea_level"]}')
				else:
					await ctx.send(f"I can't find {city_name}")


@bot.command(name="dogs", help="Get Random picture of dogs.")
async def getRandomDogPicture():
	pass

""" Experimental Feature Related to Chatterbot Library """
@bot.command(name="cybel", help="General conversation command")
async def cybel(ctx, *args):
	""" I am Cybel. Ask me question related of science, math and general conversation """
	async with ctx.typing():
		userQuestion = ' '.join(args)
		botResponse = askMe(userQuestion)
		await ctx.send(botResponse)


if __name__ == '__main__':
	bot.run(utils.TOKEN)
