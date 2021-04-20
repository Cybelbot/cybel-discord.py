"""
MIT License

Copyright (c) 2021 Deepak Raj

Bot-Name:- Cybel
Github:- https://github.com/codePerfectPlus/Cybel
Invite-Link:-
https://discord.com/api/oauth2/authorize?client_id=832137823309004800&permissions=142337&scope=bot

"""
import discord
from discord.ext import commands
import aiohttp


class AutoCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Game(name="Fornite"))
        print(f'{self.bot.user.name} is Online...')

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        picture_api = 'http://shibe.online/api/shibes?count=1&urls=true'
        async with aiohttp.ClientSession() as session:
            async with session.get(picture_api) as response:
                if response.status == 200:
                    result = await response.json()

                    random_picture = result[0]
                    channel = member.guild.system_channel
                    if channel is not None:
                        welcome_msg = discord.Embed(title="Welcome",
                                                    description=f"welcome {member.mention}, Introduce yourself to community.")
                        welcome_msg.set_thumbnail(
                            url="https://cdn3.iconfinder.com/data/icons/chat-bot-emoji-filled-color/300/35618308Untitled-3-512.png")
                        welcome_msg.set_image(url=random_picture)
                        welcome_msg.set_footer(text="Image credit: https://shibe.online/")
                        await channel.send(embed=welcome_msg)
                        await member.send("welcome to the Server!\nPlease introduce yourself in server.")


def setup(bot: commands.Bot):
    bot.add_cog(AutoCommands(bot))
