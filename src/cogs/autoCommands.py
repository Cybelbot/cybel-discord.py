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
from src.utils import utils


class AutoCommands(commands.Cog):
    """ These commands will fire automatically."""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Game(name="Fornite"))
        print(f'{self.bot.user.name} is Online...')

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        picture_api = 'http://shibe.online/api/shibes?count=1&urls=true'
        try:
            result = await utils._fetch(picture_api)

            random_picture = result[0]
            channel = member.guild.system_channel
            if channel is not None:
                welcome_msg = discord.Embed(title="Welcome",
                                            description=f"welcome {member.mention}, Introduce yourself to community.")
                welcome_msg.set_thumbnail(
                    url="https://cdn3.iconfinder.com/data/icons/chat-bot-emoji-filled-color/300/35618308Untitled-3-512.png")
                welcome_msg.set_image(url=random_picture)
                welcome_msg.set_footer(
                    text="Image credit: https://shibe.online/")
                await channel.send(embed=welcome_msg)
                await member.send("welcome to the Server!\nPlease introduce yourself in server.")
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')


def setup(bot: commands.Bot):
    bot.add_cog(AutoCommands(bot))
