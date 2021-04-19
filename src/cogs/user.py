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
from src.utils import askme


class UserCommands(commands.Cog):
    """ User Commands """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="joke", help="get random jokes")
    async def get_random_joke(self, ctx):
        """ Get random jokes """
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

    @commands.command(name="fact", help="get amazing random fact")
    async def get_random_fact(self, ctx):
        """ Get amazing random fact """
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

    @commands.command(name="gh", help="get Github user data")
    async def get_github_userdata(self, ctx, username: str):
        """ Get Github User Data Using !gh username """
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

    @commands.command(name="ifsc", help="Get Indian Bank Branch details by IFSC Code")
    async def get_bankdata(self, ctx, ifsc_code: str):
        """ Get Bank Details by IFSC CODE In INdia !ifsc <ifsc_code> """
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

    @commands.command(name="weather", help="weather of world at your command")
    async def get_weather(self, ctx, *args):
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

    @commands.command(name="dog", help="Get Random picture of dogs.")
    async def get_random_dog_picture(self, ctx):
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

    @commands.command(name="fox", help="Get Random Picture of FOx")
    async def get_random_fox_picture(self, ctx):
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

    @commands.command(name="cat", help="Get Random Pictures of Cats")
    async def get_random_cat_picture(self, ctx):
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

    @commands.command(name="create_invite", help="create server invite")
    async def create_invite(self, ctx):
        """ Create instant invite for Channel """
        link = await ctx.channel.create_invite(max_age=0)
        current_user = ctx.author
        await ctx.send(f"Hi! {current_user.mention} \nHere is an instant invite to your server: \n{str(link)}")

    @commands.command(name="dice", help="roll a dice in NdN format. 5d5")
    async def roll_the_dice(self, ctx, dice: str):
        """Rolls a dice in NdN format."""
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            return 'Format has to be in NdN!'

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

    @commands.command(name="flipcoin", help="flip a coin")
    async def flip_the_coin(self, ctx):
        flip = "Head" if random.randint(0, 1) == 0 else "Tail"
        await ctx.send(flip)

    @commands.command(name="cybel", help="General conversation command")
    async def cybel(self, ctx, *args):
        """ I am Cybel. Ask me question related of science, math and general conversation """
        async with ctx.typing():
            user_question = ' '.join(args)
            bot_response = askme.askMe(user_question)
            await ctx.send(bot_response)


def setup(bot: commands.Bot):
    bot.add_cog(UserCommands(bot))
