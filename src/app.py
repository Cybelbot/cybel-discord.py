"""
MIT License

Copyright (c) 2021 Deepak Raj

Bot-Name:- Cybel
Github:- https://github.com/codePerfectPlus/Cybel
Invite-Link:-
https://discord.com/api/oauth2/authorize?client_id=832137823309004800&permissions=142337&scope=bot

"""
import re
import random
import discord
import datetime
from discord import Intents
from discord.ext import commands
import aiohttp
import json

from askme import askMe
import utils

intents = Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
BOTNAME= "Cybel"

@bot.event
async def on_ready():
	""" Change Bot Presense """
	await bot.change_presence(activity=discord.Game(name="Fornite"))
	print(f'{bot.user.name} is Online...')


""" @bot.event
async def on_message(message: str):
	if message.author.id == bot.user.id:
		return
	msg_content = message.content.lower()

	if msg_content.startswith('ping'):
		await message.channel.send("Pong")
	if msg_content.startswith('pong'):
		await message.channel.send("Ping")

	await bot.process_commands(message) """


@bot.command(name="server")
async def serverInfo(ctx):
	""" Get the server information """
	embed = discord.Embed(title=f"{ctx.guild.name}", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
	embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
	embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
	embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
	embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
	embed.add_field(name="Bot Presense", value=f"{len(bot.guilds)} Servers")
	# embed.set_thumbnail(url=f"{ctx.guild.icon}")
	embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")
	await ctx.send(embed=embed)


@bot.command(name="kick", help="Kick user")
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason=None):
	""" command to kick user. check !help kick """
	try:
		await user.kick(reason=reason)
		await ctx.message.delete()
		kick = discord.Embed(title=f":boot: Kicked {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
		await ctx.channel.send(embed=kick)
	except Exception:
		await ctx.channel.send(f"{BOTNAME} doesn't have enough permission to kick someone.")


@bot.command(name="ban", help="command to ban user")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
	""" command to ban user. Check !help ban """
	try:
		await member.ban(reason=reason)
		ban = discord.Embed(title=f":boom: Banned {member.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
		await ctx.message.delete()
		await ctx.channel.send(embed=ban)
	except Exception:
		await ctx.channel.send(f"{BOTNAME} doesn't have enough permission to ban someone.")


@bot.command(name="unban", help="command to unban user")
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member_id:int):
	""" command to unban user. check !help unban """
	await ctx.guild.unban(discord.Object(id=member_id))
	await ctx.send(f"Unban {member_id}")


@bot.command()
async def create_invite(ctx):
	""" Create instant invite for Channel """
	link = await ctx.channel.create_invite(max_age = 0)
	await ctx.send("Here is an instant invite to your server: " + str(link))


""" Commands using API """

@bot.command(name="joke", help="get random jokes")
async def getRandomJoke(ctx):
	""" Get random jokes """
	randomJokeURL = 'https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single'
	async with ctx.typing():
		async with aiohttp.ClientSession() as session:
			async with session.get(randomJokeURL) as response:
				if response.status == 200:
					result = await response.json()
					randomJoke = result["joke"]
					await ctx.send(randomJoke)
				else:
					await ctx.send(f"API is not available, Status Code {response.status}")


@bot.command(name="fact", help="get amazing random fact")
async def getRandomFact(ctx):
	""" Get amazing random fact """
	randomFactURL = 'https://uselessfacts.jsph.pl//random.json?language=en'
	async with ctx.typing():
		async with aiohttp.ClientSession() as session:
			async with session.get(randomFactURL) as response:
				if response.status == 200:
					result = await response.json()
					randomFact = result['text']
					await ctx.send(randomFact)
				else:
					await ctx.send(f"API is not available, Status Code {response.status}")


@bot.command(name="dice", help="roll a dice in NdN format. 5d5")
async def rollTheDice(ctx, dice: str):
	"""Rolls a dice in NdN format."""
	try:
		rolls, limit = map(int, dice.split('d'))
	except Exception:
		return 'Format has to be in NdN!'

	result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
	await ctx.send(result)


@bot.command(name="coinflip", help="flip a coin")
async def flipCoin(ctx, flip_number: int):
	pass


@bot.command(name="gh", help="get Github user data")
async def getGihubUserData(ctx, username: str):
	""" Get Github User Data Using !gh username """
	async with ctx.typing():
		gitAPIURL = f'https://api.github.com/users/{username}'
		async with aiohttp.ClientSession() as session:
			async with session.get(gitAPIURL) as response:
				if response.status == 200:
					userData = await response.json()
					await ctx.send(f'Name: {userData["name"]}\nPublic Repo: {userData["public_repos"]}\nFollowers: {userData["followers"]}\nLast Updated: {userData["updated_at"]}')
				else:
					await ctx.send(f"{username} is not a github user.")


@bot.command(name="ifsc", help="Get Indian Bank Branch details by IFSC Code")
async def getBankDataByIFSC(ctx, ifsc_code: str):
	""" Get Bank Details by IFSC CODE In INdia !ifsc <ifsc_code> """
	url = f"https://ifsc.razorpay.com/{ifsc_code}"
	async with ctx.typing():
		async with aiohttp.ClientSession() as session:
			async with session.get(url) as response:
				if response.status == 200:
					bankData = await response.json()
					await ctx.send(f'Branch: {bankData["BRANCH"]}\nBank: {bankData["BANK"]}\nDistrict: {bankData["DISTRICT"]}\nState: {bankData["STATE"]}\nContact Number: {bankData["CONTACT"]}')
				else:
					await ctx.send(f"{ifsc_code} is not a valid IFSC code.")


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
					await ctx.send(f"I can't find {city_name}.")


@bot.command(name="dog", help="Get Random picture of dogs.")
async def getRandomDogPicture(ctx):
	dogAPIURL = "https://dog.ceo/api/breeds/image/random"
	async with ctx.typing():
		async with aiohttp.ClientSession() as session:
			async with session.get(dogAPIURL) as response:
				if response.status == 200:
					result = await response.json()

					dogPictureURL = result["message"]
					embed = discord.Embed(title="bow! bow!")
					embed.set_image(url=dogPictureURL)
					embed.set_author(
						name="Dog API", url='https://dog.ceo/dog-api/')
					await ctx.send(embed=embed)
				else:
					await ctx.send(f"API is not available, Status Code {response.status}")


@bot.command(name="fox", help="Get Random Picture of FOx")
async def getRandomFoxPicture(ctx):
	foxAPIURL = 'https://randomfox.ca/floof/'
	async with ctx.typing():
		async with aiohttp.ClientSession() as session:
			async with session.get(foxAPIURL) as response:
				if response.status == 200:
					result = await response.json()

					foxPictureURL = result["image"]
					embed = discord.Embed(title="howls!")
					embed.set_image(url=foxPictureURL)
					embed.set_author(
						name="foxAPI", url='https://randomfox.ca/')
					await ctx.send(embed=embed)
				else:
					await ctx.send(f"API is not available, Status Code {response.status}")


@bot.command(name="cat", help="Get Random Pictures of Cats")
async def getRandomcCatPicture(ctx):
	""" Get Random Cats Picture """
	catAPIURL = "https://thatcopy.pw/catapi/rest/"
	async with ctx.typing():
		async with aiohttp.ClientSession() as session:
			async with session.get(catAPIURL) as response:
				if response.status == 200:
					result = await response.json()

					catPictureURL = result["url"]
					embed = discord.Embed(title="Meow! Meow!")
					embed.set_image(url=catPictureURL)
					embed.set_author(
						name='catAPI', url='https://thatcopy.pw/catapi/')
					await ctx.send(embed=embed)
				else:
					await ctx.send(f"API is not available, Status Code {response.status}")


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
