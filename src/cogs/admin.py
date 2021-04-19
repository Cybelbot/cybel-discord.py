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


class AdminCommands(commands.Cog):
    """ Admin Level Commands """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """ command to kick user."""
        await ctx.message.delete()
        try:
            await member.kick(reason=reason)
            kick = discord.Embed(title=f":boot: Kicked {member.name}!",
                                 description=f"Reason: {reason}\nBy: {ctx.author.mention}")
            await ctx.send(embed=kick)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, member: discord.Member):
        """ Mute the user for voice activity """
        await ctx.message.delete()
        try:
            await member.edit(mute=True)
            await ctx.send(f'{member.mention} is muted.')
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, member: discord.Member):
        """ Unmute the user for voice activity """
        await ctx.message.delete()
        try:
            await member.edit(unmute=True)
            await ctx.send(f'{member.mention} is unmuted')
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """ command to ban user. Check !help ban """
        await ctx.message.delete()
        try:
            await member.ban(reason=reason)
            ban = discord.Embed(
                title=f":boom: Banned {member.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
            await ctx.send(embed=ban)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member_id: int):
        """ command to unban user. check !help unban """
        await ctx.message.delete()
        try:
            await ctx.guild.unban(discord.Object(id=member_id))
            await ctx.send(f"Unban {member_id}")
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def chnick(self, ctx, member: discord.Member, nick):
        """ Change nicknames of the servers'members """
        await ctx.message.delete()
        try:
            await member.edit(nick=nick)
            await ctx.send(f'Nickname was changed for {member.mention} ')
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')


def setup(bot: commands.Bot):
    bot.add_cog(AdminCommands(bot))
