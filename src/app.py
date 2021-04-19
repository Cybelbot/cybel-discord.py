"""
MIT License

Copyright (c) 2021 Deepak Raj

Bot-Name:- Cybel
Github:- https://github.com/codePerfectPlus/Cybel
Invite-Link:-
https://discord.com/api/oauth2/authorize?client_id=832137823309004800&permissions=142337&scope=bot

"""
import random
import discord
import datetime
from discord import Intents
from discord.ext import commands
import aiohttp

# local imports
from askme import askMe
import utils

intents = Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!",
                   intents=intents,
                   case_insensitive=True)

BOTNAME = utils.BOTNAME


@bot.event
async def on_ready():
    """ Define the bot activity """
    await bot.change_presence(activity=discord.Game(name="Fornite"))
    print(f'{bot.user.name} is Online...')


""" @bot.event
async def on_message(message: str):
	# custom command to trigger on message
	if message.author.id == bot.user.id:
		return
	msg_content = message.contesnt.lower()

	if msg_content.startswith('ping'):
		await message.channel.send("Pong")
	if msg_content.startswith('pong'):
		await message.channel.send("Ping")

	await bot.process_commands(message) """


@bot.command(name="server")
async def server_info(ctx):
    """ Get the server information """
    embed = discord.Embed(title=f"{ctx.guild.name}",
                          timestamp=datetime.datetime.utcnow(),
                          color=discord.Color.blue())
    embed.add_field(name="Server created at", value=ctx.guild.created_at)
    embed.add_field(name="Server Owner", value=ctx.guild.owner)
    embed.add_field(name="Server Region", value=ctx.guild.region)
    embed.add_field(name="Server ID", value=ctx.guild.id)
    embed.add_field(name="Bot Presense", value=f"{len(bot.guilds)} Servers")
    embed.set_thumbnail(url=ctx.guild.icon)
    embed.set_thumbnail(
        url="https://cdn3.iconfinder.com/data/icons/chat-bot-emoji-filled-color/300/35618308Untitled-3-512.png")
    await ctx.send(embed=embed)


@bot.event
async def on_member_join(member: discord.Member):
    await member.send("welcome to Server!")


# Admin Level Commands for manage server
# Kick, Ban, Unban, create_invite
# some of the may require admin_permission

@bot.command(name="kick", help="Kick user")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    """ command to kick user. check !help kick """
    await ctx.message.delete()
    try:
        await member.kick(reason=reason)
        kick = discord.Embed(title=f":boot: Kicked {member.name}!",
                             description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.send(embed=kick)
    except Exception as error:
        await ctx.send(error)


@bot.command(name="mute", help="mute user in server")
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member):
    await ctx.message.delete()
    try:
        await member.edit(mute=True)
        await ctx.send(f'{member.mention} is muted.')
    except Exception as error:
        await ctx.send(error)


@bot.command(name='unmute', help='unmute user in server')
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member):
    await ctx.message.delete()
    try:
        await member.edit(unmute=True)
        await ctx.send(f'{member.mention} is unmuted')
    except Exception as error:
        await ctx.send(error)


@bot.command(name="ban", help="command to ban user")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    """ command to ban user. Check !help ban """
    await ctx.message.delete()
    try:
        await member.ban(reason=reason)
        ban = discord.Embed(
            title=f":boom: Banned {member.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.send(embed=ban)
    except Exception as error:
        await ctx.send(error)


@bot.command(name="unban", help="command to unban user")
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member_id: int):
    """ command to unban user. check !help unban """
    await ctx.message.delete()
    try:
        await ctx.guild.unban(discord.Object(id=member_id))
        await ctx.send(f"Unban {member_id}")
    except Exception as error:
        await ctx.send(error)


@bot.command(name="chnick", help="change nickname to users")
@commands.has_permissions(administrator=True)
async def chnick(ctx, member: discord.Member, nick):
    """ Change nicknames of the servers'members """
    await ctx.message.delete()
    try:
        await member.edit(nick=nick)
        await ctx.send(f'Nickname was changed for {member.mention} ')
    except Exception as error:
        await ctx.send(error)


@bot.command(name="create_invite", help='create instant invite')
async def create_invite(ctx):
    """ Create instant invite for Channel """
    link = await ctx.channel.create_invite(max_age=0)
    current_user = ctx.author
    await ctx.send(f"Hi! {current_user.mention} \nHere is an instant invite to your server: \n{str(link)}")


# Command using external APIs
# using aiohttp librarby for async functions

@bot.command(name="joke", help="get random jokes")
async def get_random_joke(ctx):
    """ Get random jokes """
    randomJokeURL = 'https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single'
    async with ctx.typing():
        async with aiohttp.ClientSession() as session:
            async with session.get(randomJokeURL) as response:
                if response.status == 200:
                    result = await response.json()
                    random_joke = result["joke"]
                    await ctx.send(random_joke)
                else:
                    await ctx.send(f"API is not available, Status Code {response.status}")


@bot.command(name="fact", help="get amazing random fact")
async def get_random_fact(ctx):
    """ Get amazing random fact """
    randomFactURL = 'https://uselessfacts.jsph.pl//random.json?language=en'
    async with ctx.typing():
        async with aiohttp.ClientSession() as session:
            async with session.get(randomFactURL) as response:
                if response.status == 200:
                    result = await response.json()
                    radnom_fact = result['text']
                    await ctx.send(radnom_fact)
                else:
                    await ctx.send(f"API is not available, Status Code {response.status}")


@bot.command(name="gh", help="get Github user data")
async def get_github_userdata(ctx, username: str):
    """ Get Github User Data Using !gh username """
    async with ctx.typing():
        gitAPIURL = f'https://api.github.com/users/{username}'
        async with aiohttp.ClientSession() as session:
            async with session.get(gitAPIURL) as response:
                if response.status == 200:
                    user_data = await response.json()
                    await ctx.send(f'Name: {user_data["name"]}\n'
                                   f'Public Repo: {user_data["public_repos"]}\n'
                                   f'Followers: {user_data["followers"]}\n'
                                   f'Last Updated: {user_data["updated_at"]}')
                else:
                    await ctx.send(f"{username} is not a github user.")


@bot.command(name="ifsc", help="Get Indian Bank Branch details by IFSC Code")
async def get_bankdata(ctx, ifsc_code: str):
    """ Get Bank Details by IFSC CODE In INdia !ifsc <ifsc_code> """
    url = f"https://ifsc.razorpay.com/{ifsc_code}"
    async with ctx.typing():
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    bank_data = await response.json()
                    await ctx.send(f'Branch: {bank_data["BRANCH"]}\n'
                                   f'Bank: {bank_data["BANK"]}\n'
                                   f'District: {bank_data["DISTRICT"]}\n'
                                   f'State: {bank_data["STATE"]}\n'
                                   f'Contact Number: {bank_data["CONTACT"]}')
                else:
                    await ctx.send(f"{ifsc_code} is not a valid IFSC code.")


@bot.command(name="weather", help="weather of world at your command")
async def get_weather(ctx, *args):
    """ Get Your City weather example:- !weather New Delhi"""
    city_name = ' '.join(args)
    async with ctx.typing():
        weather_api = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={utils.WEATHER_API_KEY}"
        async with aiohttp.ClientSession() as session:
            async with session.get(weather_api) as response:
                if response.status == 200:
                    weather_data = await response.json()

                    await ctx.send(f'{city_name.title()} - Country: {weather_data["city"]["country"]}\n'
                                   f'Temp: {round(weather_data["list"][0]["main"]["temp"] -273.0)}\n'
                                   f'Minimum Temp: {round(weather_data["list"][0]["main"]["temp_min"] -273.0)}\n'
                                   f'Maximum Temp: {round(weather_data["list"][0]["main"]["temp_max"] -273.0)}\n'
                                   f'Pressure: {weather_data["list"][0]["main"]["pressure"]}\n'
                                   f'Humidity: {weather_data["list"][0]["main"]["humidity"]}\n'
                                   f'Sea-Level:{weather_data["list"][0]["main"]["sea_level"]}')
                else:
                    await ctx.send(f"I can't find {city_name}.")


@bot.command(name="dog", help="Get Random picture of dogs.")
async def get_random_dog_picture(ctx):
    dog_api = "https://dog.ceo/api/breeds/image/random"
    async with ctx.typing():
        async with aiohttp.ClientSession() as session:
            async with session.get(dog_api) as response:
                if response.status == 200:
                    result = await response.json()

                    dog_picture_url = result["message"]
                    embed = discord.Embed(title="bow! bow!")
                    embed.set_image(url=dog_picture_url)
                    embed.set_author(
                        name="Dog API", url='https://dog.ceo/dog-api/')
                    await ctx.send(embed=embed)
                else:
                    await ctx.send(f"API is not available, Status Code {response.status}")


@bot.command(name="fox", help="Get Random Picture of FOx")
async def get_random_fox_picture(ctx):
    fox_api = 'https://randomfox.ca/floof/'
    async with ctx.typing():
        async with aiohttp.ClientSession() as session:
            async with session.get(fox_api) as response:
                if response.status == 200:
                    result = await response.json()

                    fox_picture_url = result["image"]
                    embed = discord.Embed(title="howls!")
                    embed.set_image(url=fox_picture_url)
                    embed.set_author(
                        name="foxAPI", url='https://randomfox.ca/')
                    await ctx.send(embed=embed)
                else:
                    await ctx.send(f"API is not available, Status Code {response.status}")


@bot.command(name="cat", help="Get Random Pictures of Cats")
async def get_random_cat_picture(ctx):
    """ Get Random Cats Picture """
    cat_api = "https://thatcopy.pw/catapi/rest/"
    async with ctx.typing():
        async with aiohttp.ClientSession() as session:
            async with session.get(cat_api) as response:
                if response.status == 200:
                    result = await response.json()

                    cat_picture_url = result["url"]
                    embed = discord.Embed(title="Meow! Meow!")
                    embed.set_image(url=cat_picture_url)
                    embed.set_author(
                        name='catAPI', url='https://thatcopy.pw/catapi/')
                    await ctx.send(embed=embed)
                else:
                    await ctx.send(f"API is not available, Status Code {response.status}")


@bot.command(name="dice", help="roll a dice in NdN format. 5d5")
async def roll_the_dice(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        return 'Format has to be in NdN!'

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(name="flipcoin", help="flip a coin")
async def flip_the_coin(ctx):
    flip = "Head" if random.randint(0, 1) == 0 else "Tail"
    await ctx.send(flip)


@bot.command(name="cybel", help="General conversation command")
async def cybel(ctx, *args):
    """ I am Cybel. Ask me question related of science, math and general conversation """
    async with ctx.typing():
        user_question = ' '.join(args)
        bot_response = askMe(user_question)
        await ctx.send(bot_response)


if __name__ == '__main__':
    bot.run(utils.TOKEN)
