"""
MIT License

Copyright (c) 2021 Deepak Raj

Bot-Name:- Cybel
Github:- https://github.com/codePerfectPlus/Cybel
Invite-Link:-
https://discord.com/api/oauth2/authorize?client_id=832137823309004800&permissions=142337&scope=bot
"""
from discord.ext import commands
import discord
import random
import datetime

class OtherCommands(commands.Cog, name="User Useful Commands"):
    def __init__(self, bot):
        self.bot = bot

    """ @commands.command()
    async def take_picture(self, ctx, url=None):
        if not url:
            url = ctx.message.attachments[0].url

        print(url)
        await ctx.send(embed=discord.Embed().set_image(url=url)) """

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
            embed = discord.Embed(title=ctx.guild.name,
                                  timestamp=datetime.datetime.utcnow(),
                                  color=discord.Color.blue())
            embed.add_field(name="Server created at",
                            value=ctx.guild.created_at)
            embed.add_field(name="Server Owner", value=ctx.guild.owner)
            embed.add_field(name="Server Region", value=ctx.guild.region)
            embed.add_field(name="Server ID", value=ctx.guild.id)
            embed.add_field(name="Bot Presense",
                            value=f"{len(self.bot.guilds)} Servers")
            embed.set_thumbnail(
                url="https://cdn3.iconfinder.com/data/icons/chat-bot-emoji-filled-color/300/35618308Untitled-3-512.png")
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')


def setup(bot: commands.Bot):
    bot.add_cog(OtherCommands(bot))
