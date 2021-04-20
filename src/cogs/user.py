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
from discord.ext import commands
import aiohttp

from src.utils import utils


class UserCommands(commands.Cog, name="Commands for Users Use"):
    """ User Commands """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="joke")
    async def get_random_joke(self, ctx):
        """ Get random jokes 

        command: !joke
        API: https://v2.jokeapi.dev/
        """
        joke_api = 'https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single'
        async with ctx.typing():
            async with aiohttp.ClientSession() as session:
                async with session.get(joke_api) as response:
                    if response.status == 200:
                        result = await response.json()
                        random_joke = result["joke"]
                        await ctx.send(random_joke)
                    else:
                        await ctx.send(f"API is not available, Status Code {response.status}")

    @commands.command(name="fact")
    async def get_random_fact(self, ctx):
        """ Get amazing random fact 

        command: !fact
        API: https://uselessfacts.jsph.pl
        """
        fact_api = 'https://uselessfacts.jsph.pl//random.json?language=en'
        async with ctx.typing():
            async with aiohttp.ClientSession() as session:
                async with session.get(fact_api) as response:
                    if response.status == 200:
                        result = await response.json()
                        radnom_fact = result['text']
                        await ctx.send(radnom_fact)
                    else:
                        await ctx.send(f"API is not available, Status Code {response.status}")

    @commands.command(name="gh")
    async def get_github_userdata(self, ctx, username: str):
        """ Get Github User Data Using 

        command: !gh <user_name>
        API: https://api.github.com
        """
        async with ctx.typing():
            git_api = f'https://api.github.com/users/{username}'
            async with aiohttp.ClientSession() as session:
                async with session.get(git_api) as response:
                    if response.status == 200:
                        user_data = await response.json()
                        await ctx.send(f'Name: {user_data["name"]}\n'
                                       f'Public Repo: {user_data["public_repos"]}\n'
                                       f'Followers: {user_data["followers"]}\n'
                                       f'Last Updated: {user_data["updated_at"]}')
                    else:
                        await ctx.send(f"{username} is not a github user.")

    @commands.command(name="ifsc")
    async def get_bankdata(self, ctx, ifsc_code: str):
        """ Get Indian Bank Details by IFSC Code

        command: !ifsc <ifsc_code>
        API: https://ifsc.razorpay.com
        """
        razorpay_api = f"https://ifsc.razorpay.com/{ifsc_code}"
        async with ctx.typing():
            async with aiohttp.ClientSession() as session:
                async with session.get(razorpay_api) as response:
                    if response.status == 200:
                        bank_data = await response.json()
                        await ctx.send(f'Branch: {bank_data["BRANCH"]}\n'
                                       f'Bank: {bank_data["BANK"]}\n'
                                       f'District: {bank_data["DISTRICT"]}\n'
                                       f'State: {bank_data["STATE"]}\n'
                                       f'Contact Number: {bank_data["CONTACT"]}')
                    else:
                        await ctx.send(f"{ifsc_code} is not a valid IFSC code.")

    @commands.command(name="weather")
    async def get_weather(self, ctx, *args):
        """ Get Your City weather

        command: !weather <city_name>
        API: https://openweathermap.org/
        """
        city_name = ' '.join(args)
        weather_api = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={utils.WEATHER_API_KEY}"
        async with ctx.typing():
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

    @commands.command(name="dog")
    async def get_random_dog_picture(self, ctx):
        """ Get Random Pictures Of Dogs

        command: !dog
        API: https://dog.ceo
        """
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

    @commands.command(name="fox")
    async def get_random_fox_picture(self, ctx):
        """ Get Random Picture of Foxes 

        command: !fox
        API: https://randomfox.ca
        """
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

    @commands.command(name="cat")
    async def get_random_cat_picture(self, ctx):
        """ Get Random Pictures of cats

        Command: !cat
        Api: https://thatcopy.pw/catapi/rest/
        """
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

    @commands.command(name="create_invite")
    async def create_invite(self, ctx):
        """ Create instant invite for Channel 

        command: !create_invite
        output: instant server invite
        """
        link = await ctx.channel.create_invite(max_age=0)
        current_user = ctx.author
        await ctx.send(f"Hi! {current_user.mention} \nHere is an instant invite to your server: \n{str(link)}")

    @commands.command(name="dice")
    async def roll_the_dice(self, ctx, dice: str):
        """Rolls a dice in NdN format.

        command: !dice NdN

        number of rolls-d-number of limit

        input: 6d5
        output example: 2, 1, 4, 3, 5
        """
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            return 'Format has to be in NdN!'

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

    @commands.command(name="flipcoin")
    async def flip_the_coin(self, ctx):
        """ Flip the coin randomly 

        command: !flipcoin
        output: Head/Tail
        """
        flip = "Head" if random.randint(0, 1) == 0 else "Tail"
        await ctx.send(flip)

    @commands.command(name="server")
    async def server_info(self, ctx):
        """ Get the server information 

        command: !server
        output: Embed server information
        """
        try:
            embed = discord.Embed(title=f"{ctx.guild.name}",
                                  timestamp=datetime.datetime.utcnow(),
                                  color=discord.Color.blue())
            embed.add_field(name="Server created at",
                            value=f"{ctx.guild.created_at}")
            embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
            embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
            embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
            embed.add_field(name="Bot Presense",
                            value=f"{len(bot.guilds)} Servers")
            embed.set_thumbnail(url=f"{ctx.guild.icon}")
            embed.set_thumbnail(
                url="https://cdn3.iconfinder.com/data/icons/chat-bot-emoji-filled-color/300/35618308Untitled-3-512.png")
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')


def setup(bot: commands.Bot):
    bot.add_cog(UserCommands(bot))
