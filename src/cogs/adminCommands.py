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


class AdminCommands(commands.Cog, name="Commands for Server Management: Admin Commands"):
    """ Admin Level Commands
    
    Some commands May Require administrator access.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """ command to kick user
        
        command: !kick <member_name> <reason_to_kick>
        output: function will remove user from server with embed message.
        """
        await ctx.message.delete()
        try:
            await member.kick(reason=reason)
            kick = discord.Embed(title=f":boot: Kicked {member.name}!",
                                 description=f"Reason: {reason}\nBy: {ctx.author.mention}")
            await ctx.send(embed=kick)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member: discord.Member):
        """ Mute the user for voice activity 
        
        command: !mute <member_name>
        output: It will mute the voice channel connected memeber.
        user should be connected to the voice channel.

        Cybel Need administrator access for mute command.
        """
        await ctx.message.delete()
        try:
            await member.edit(mute=True)
            await ctx.send(f'{member.mention} is muted.')
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, member: discord.Member):
        """ Unmute the user for voice activity 
        
        command: !unmute <member_name>
        output: It will unmute the voice channel connected memeber.

        Cybel Need administrator access for mute command.
        """
        await ctx.message.delete()
        try:
            await member.edit(unmute=True)
            await ctx.send(f'{member.mention} is unmuted')
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """ command to ban user
        
        command: !ban <member> <reason>
        Cybel Need ban_members access for ban command.
        """
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
        """ command to unban user.
        
        command: !unban <member_id>
        Cybel Need administrator access for Unban command.
        """
        await ctx.message.delete()
        try:
            await ctx.guild.unban(discord.Object(id=member_id))
            await ctx.send(f"Unban {member_id}")
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')

    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    async def chnick(self, ctx, member: discord.Member, nick):
        """ Change nicknames of the servers'members 
        
        command: !chnick <member> <new_nickname>
        Cybel Need administrator access for change Nicknames.
        """
        await ctx.message.delete()
        try:
            await member.edit(nick=nick)
            await ctx.send(f'Nickname was changed for {member.mention} ')
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')


def setup(bot: commands.Bot):
    bot.add_cog(AdminCommands(bot))
